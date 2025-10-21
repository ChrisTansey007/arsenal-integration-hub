#!/usr/bin/env python3
"""
Generate Arsenal items from extracted insights data.
Creates prompt files, updates patterns library, and tracking logs.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Set
from datetime import datetime
from collections import defaultdict

# Configuration
EXTRACTED_DATA_FILE = r"C:\Users\theca\CascadeProjects\arsenal-integration-hub\scripts\all-extracted-data.json"
PROMPT_ARSENAL_DIR = r"C:\Users\theca\CascadeProjects\prompt-arsenal"
PATTERNS_LIBRARY_FILE = r"C:\Users\theca\CascadeProjects\windsurf-memories-arsenal\prompt-engineering\prompt-patterns-library.md"
TRACKING_LOG_FILE = r"C:\Users\theca\CascadeProjects\arsenal-integration-hub\examples\meta-prompting\insights-tracking-log.md"

# Domain to directory mapping for prompts
DOMAIN_DIRS = {
    'automation': 'automation/workflow',
    'api-development': 'development/api',
    'web-development': 'development/web',
    'database': 'development/database',
    'documentation': 'development/documentation',
    'business-process': 'business/process-automation',
    'data-analysis': 'development/data',
    'devops': 'development/devops',
    'ai-ml': 'ai-prompting/analysis',
    'testing': 'development/testing',
    'general': 'meta-prompting'
}

def load_extraction_data() -> Dict:
    """Load the extracted insights JSON."""
    with open(EXTRACTED_DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def deduplicate_quick_wins(all_files: List[Dict]) -> List[Dict]:
    """Deduplicate quick win patterns across all files."""
    print("🔄 Deduplicating Quick Win patterns...")
    
    # Group similar patterns
    pattern_groups = defaultdict(list)
    
    for file_data in all_files:
        if not file_data.get('extraction_success'):
            continue
        
        for qw in file_data.get('quick_wins', []):
            pattern = qw['pattern'].lower().strip('"')
            
            # Normalize for comparison
            normalized = re.sub(r'\{[^}]+\}', '{VAR}', pattern)
            normalized = re.sub(r'\s+', ' ', normalized)
            
            pattern_groups[normalized].append({
                'pattern': qw['pattern'],
                'category': qw.get('category'),
                'source_file': file_data['filename'],
                'original': qw['original']
            })
    
    # Select best version of each pattern
    unique_patterns = []
    for normalized, instances in pattern_groups.items():
        # Prefer patterns with category
        with_category = [p for p in instances if p['category']]
        if with_category:
            best = with_category[0]
        else:
            best = instances[0]
        
        # Add source count
        best['occurrence_count'] = len(instances)
        best['source_files'] = [p['source_file'] for p in instances]
        unique_patterns.append(best)
    
    print(f"   {len(pattern_groups)} unique patterns from {sum(len(g) for g in pattern_groups.values())} total")
    print(f"   Reduction: {100 - (len(pattern_groups) / sum(len(g) for g in pattern_groups.values()) * 100):.0f}% deduplication\n")
    
    # Sort by occurrence count
    unique_patterns.sort(key=lambda x: x['occurrence_count'], reverse=True)
    
    return unique_patterns

def categorize_pattern(pattern: str, existing_category: str = None) -> str:
    """Categorize a pattern if not already categorized."""
    if existing_category:
        return existing_category
    
    pattern_lower = pattern.lower()
    
    # Pattern category detection
    if any(kw in pattern_lower for kw in ['clarify', 'confirm', 'what', 'which', 'scope']):
        return 'Clarify'
    elif any(kw in pattern_lower for kw in ['format', 'output', 'structure', 'markdown', 'table']):
        return 'Constrain'
    elif any(kw in pattern_lower for kw in ['score', 'check', 'verify', 'validate', 'review']):
        return 'Evaluate'
    elif any(kw in pattern_lower for kw in ['refactor', 'improve', 'enhance', 'upgrade']):
        return 'Refine'
    elif any(kw in pattern_lower for kw in ['citation', 'source', 'reference', 'evidence']):
        return 'Verify'
    elif any(kw in pattern_lower for kw in ['compare', 'contrast', 'difference', 'alternative']):
        return 'Compare'
    elif any(kw in pattern_lower for kw in ['export', 'save', 'output', 'generate file']):
        return 'Export'
    elif any(kw in pattern_lower for kw in ['prioritize', 'order', 'rank', 'sort']):
        return 'Prioritize'
    elif any(kw in pattern_lower for kw in ['safety', 'warn', 'flag', 'caution']):
        return 'Safety'
    else:
        return 'Other'

def generate_prompt_filename(title: str, domain: str) -> str:
    """Generate appropriate filename for a prompt."""
    # Clean title
    title_clean = re.sub(r'[^\w\s-]', '', title.lower())
    title_clean = re.sub(r'\s+', '-', title_clean)
    title_clean = re.sub(r'-+', '-', title_clean)
    title_clean = title_clean.strip('-')
    
    # Limit length
    if len(title_clean) > 50:
        title_clean = title_clean[:50].rsplit('-', 1)[0]
    
    return f"{title_clean}.md"

def create_prompt_file(file_data: Dict, output_dir: Path) -> Path:
    """Generate a prompt file from extracted super-prompt."""
    super_prompt = file_data['super_prompt']
    
    # Generate prompt ID
    prompt_id = f"prm.{file_data['file_id'][:8]}"
    
    # Determine appropriate directory
    domain = file_data.get('domain', 'general')
    subdir = DOMAIN_DIRS.get(domain, 'meta-prompting')
    prompt_dir = output_dir / subdir
    prompt_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate filename from title
    filename = generate_prompt_filename(file_data['title'], domain)
    filepath = prompt_dir / filename
    
    # Extract variables from inputs
    variables = []
    for inp in super_prompt.get('inputs', []):
        # Look for {VAR} or {{VAR}} patterns
        var_matches = re.findall(r'\{([A-Z_]+)\}', inp)
        for var in var_matches:
            if not any(v['name'] == var.lower() for v in variables):
                variables.append({
                    'name': var.lower(),
                    'required': 'optional' not in inp.lower(),
                    'description': f"Extracted from: {inp[:50]}"
                })
    
    # Build prompt content
    content = f"""---
id: {prompt_id}
type: prompt
title: {file_data['title']}
tags: [{', '.join(file_data.get('tags', [])[:5])}]
role: user
summary: Extracted from conversation analysis - {file_data['title']}
vars:"""
    
    if variables:
        for var in variables[:5]:  # Limit to 5 variables
            content += f"\n  - {{ name: {var['name']}, required: {str(var['required']).lower()}, description: \"{var['description']}\" }}"
    else:
        content += "\n  []"
    
    content += f"""
version: 1
source_insights: {file_data['filename']}
---

# {file_data['title']}

**Extracted from conversation analysis on {file_data.get('date', 'Unknown')}.**

---

## 🎯 The Complete Prompt

```markdown
{super_prompt['full_text']}
```

---

## 📋 When to Use

**Apply this prompt when:**
{chr(10).join('- ✅ ' + lesson for lesson in file_data.get('lessons', [])[:5])}

---

## 🔧 Prompt Structure

"""
    
    if super_prompt.get('role'):
        content += f"**Role:** {super_prompt['role']}\n\n"
    
    if super_prompt.get('task'):
        content += f"**Task:** {super_prompt['task']}\n\n"
    
    if super_prompt.get('inputs'):
        content += "**Inputs:**\n"
        for inp in super_prompt['inputs'][:7]:
            content += f"{inp}\n"
        content += "\n"
    
    if super_prompt.get('process'):
        content += "**Process:**\n"
        for step in super_prompt['process'][:7]:
            content += f"{step}\n"
        content += "\n"
    
    if super_prompt.get('quality_checks'):
        content += "**Quality Checks:**\n"
        for check in super_prompt['quality_checks']:
            content += f"{check}\n"
        content += "\n"
    
    content += """---

## 🔗 Related Arsenal Items

**💭 Memories:**
- [Prompt Patterns Library](https://github.com/ChrisTansey007/windsurf-memories-arsenal/blob/main/prompt-engineering/prompt-patterns-library.md) - Pattern catalog

**⚙️ Rules:**
- [Prompt Quality Standards](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/prompt-design/prompt-quality-standards.md) - 5-D framework

---

## 📖 Source

**Extracted from:** {file_data['filename']}  
**Original conversation:** {file_data.get('date', 'Unknown')}  
**Domain:** {domain}  
**Quality score:** {file_data.get('quality_score', 'Unknown')}

---

**Result: Production-ready prompt from analyzed conversation!** 🚀
"""
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath

def update_patterns_library(unique_patterns: List[Dict]) -> None:
    """Append unique patterns to the patterns library."""
    print("📚 Updating Patterns Library...")
    
    # Read current library
    with open(PATTERNS_LIBRARY_FILE, 'r', encoding='utf-8') as f:
        library_content = f.read()
    
    # Group patterns by category
    categorized = defaultdict(list)
    for pattern in unique_patterns:
        category = categorize_pattern(pattern['pattern'], pattern.get('category'))
        categorized[category].append(pattern)
    
    # Find insertion point (before "Contributing New Patterns" section)
    insertion_marker = "## 🌱 Contributing New Patterns"
    if insertion_marker not in library_content:
        print("   ⚠️  Could not find insertion point in patterns library")
        return
    
    # Build new patterns section
    new_content = "\n\n## 🆕 Patterns from Bulk Extraction (2025-10-21)\n\n"
    new_content += f"**Source:** 43 analyzed conversation threads  \n"
    new_content += f"**Extracted:** {len(unique_patterns)} unique patterns after deduplication  \n\n"
    
    # Add top patterns by occurrence
    top_patterns = sorted(unique_patterns, key=lambda x: x['occurrence_count'], reverse=True)[:20]
    
    for i, pattern in enumerate(top_patterns, 1):
        category = categorize_pattern(pattern['pattern'], pattern.get('category'))
        content += f"\n### Pattern {i}: {pattern['pattern'][:60]}...\n"
        content += f"```\n{pattern['pattern']}\n```\n"
        content += f"- **Category:** {category}\n"
        content += f"- **Occurrences:** {pattern['occurrence_count']} threads\n"
        content += f"- **Source threads:** {len(pattern['source_files'])}\n\n"
    
    # Insert before the contributing section
    updated_content = library_content.replace(
        insertion_marker,
        new_content + insertion_marker
    )
    
    # Write back
    with open(PATTERNS_LIBRARY_FILE, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"   ✅ Added {len(top_patterns)} top patterns to library\n")

def main():
    """Main generation pipeline."""
    print("🚀 ARSENAL GENERATION PIPELINE")
    print("=" * 70)
    print()
    
    # Load data
    print("📂 Loading extraction data...")
    data = load_extraction_data()
    all_files = data['files']
    high_quality = [f for f in all_files if f.get('quality_score') == 'HIGH']
    
    print(f"   {len(all_files)} files loaded")
    print(f"   {len(high_quality)} HIGH-quality files to process\n")
    
    # Deduplicate quick wins
    unique_patterns = deduplicate_quick_wins(all_files)
    
    # Generate prompt files for HIGH-quality items
    print(f"📝 Generating {len(high_quality)} prompt files...\n")
    
    prompt_arsenal_path = Path(PROMPT_ARSENAL_DIR)
    created_files = []
    
    for file_data in high_quality:
        if not file_data.get('super_prompt'):
            print(f"   ⚠️  Skipping {file_data['filename']} - no super-prompt")
            continue
        
        try:
            filepath = create_prompt_file(file_data, prompt_arsenal_path)
            created_files.append({
                'path': filepath,
                'title': file_data['title'],
                'domain': file_data.get('domain')
            })
            print(f"   ✅ Created: {filepath.relative_to(prompt_arsenal_path)}")
        except Exception as e:
            print(f"   ❌ Error creating {file_data['filename']}: {e}")
    
    print(f"\n✅ Created {len(created_files)} prompt files\n")
    
    # Update patterns library
    # update_patterns_library(unique_patterns[:20])  # Top 20 patterns
    
    # Summary
    print("📊 GENERATION SUMMARY")
    print("=" * 70)
    print(f"Prompt files created:     {len(created_files)}")
    print(f"Unique patterns found:    {len(unique_patterns)}")
    print(f"Total source threads:     {len(all_files)}")
    print()
    
    print("✅ GENERATION COMPLETE!")
    print()
    print("📋 MANUAL NEXT STEPS:")
    print("1. Review generated prompt files for quality")
    print("2. Edit/improve as needed")
    print("3. Update prompt-arsenal README (count + new prompts)")
    print("4. Update tracking log with all 43 files")
    print("5. Commit and push in batches")

if __name__ == "__main__":
    main()
