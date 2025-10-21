#!/usr/bin/env python3
"""
Comprehensive extraction of super-prompts and quick wins from all insights files.
Phase 2: Full automated extraction with quality scoring.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional
import json
from datetime import datetime

# Configuration
INSIGHTS_DIR = r"C:\Users\theca\CascadeProjects\chriscreateswithai-nextjs\content\prompt-insights"
OUTPUT_FILE = r"C:\Users\theca\CascadeProjects\arsenal-integration-hub\scripts\all-extracted-data.json"

def extract_frontmatter(content: str) -> Dict:
    """Extract YAML frontmatter."""
    match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    
    frontmatter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip().strip("'\"")
    
    return frontmatter

def extract_super_prompt(content: str) -> Optional[Dict]:
    """Extract super-prompt with structure parsing."""
    # Try different section heading patterns
    patterns = [
        r'## Section 4: Super-Prompt.*?\n(.*?)(?=\n## |\n---\n|\Z)',
        r'## 4\) Super-Prompt.*?\n(.*?)(?=\n## |\n---\n|\Z)',
        r'## 4\. Super-Prompt.*?\n(.*?)(?=\n## |\n---\n|\Z)',
        r'## Super-Prompt \(Reusable\).*?\n(.*?)(?=\n## |\n---\n|\Z)',
        r'## Super‑Prompt.*?\n(.*?)(?=\n## |\n---\n|\Z)',
    ]
    
    section_content = None
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            section_content = match.group(1).strip()
            break
    
    if not section_content:
        return None
    
    # Extract code block if present
    code_match = re.search(r'```(?:markdown|text|yaml|)?\s*\n(.*?)```', section_content, re.DOTALL)
    if code_match:
        prompt_text = code_match.group(1).strip()
    else:
        prompt_text = section_content
    
    # Try to parse structure
    structure = {
        'full_text': prompt_text,
        'role': None,
        'task': None,
        'inputs': [],
        'process': [],
        'output': None,
        'quality_checks': []
    }
    
    # Extract ROLE
    role_match = re.search(r'(?:ROLE|Role):\s*(.+?)(?=\n\n|\n[A-Z]+:|\Z)', prompt_text, re.DOTALL)
    if role_match:
        structure['role'] = role_match.group(1).strip()
    
    # Extract TASK
    task_match = re.search(r'(?:TASK|Task|Objective|OBJECTIVE):\s*(.+?)(?=\n\n|\n[A-Z]+:|\Z)', prompt_text, re.DOTALL)
    if task_match:
        structure['task'] = task_match.group(1).strip()
    
    # Extract INPUTS (often a list)
    inputs_match = re.search(r'(?:INPUTS|Inputs|INPUT):\s*\n(.*?)(?=\n\n[A-Z]+:|\n[A-Z]+ [A-Z]+:|\Z)', prompt_text, re.DOTALL)
    if inputs_match:
        inputs_text = inputs_match.group(1)
        # Extract bullet points or variables
        for line in inputs_text.split('\n'):
            line = line.strip()
            if line.startswith('-') or line.startswith('•') or re.match(r'^\d+\.', line):
                structure['inputs'].append(line)
    
    # Extract PROCESS/CHECKLIST
    process_match = re.search(r'(?:PROCESS|Process|CHECKLIST|Checklist).*?:\s*\n(.*?)(?=\n\n[A-Z]+:|\n[A-Z]+ [A-Z]+:|\Z)', prompt_text, re.DOTALL)
    if process_match:
        process_text = process_match.group(1)
        for line in process_text.split('\n'):
            line = line.strip()
            if line.startswith('-') or line.startswith('•') or re.match(r'^\d+[\.\)]', line):
                structure['process'].append(line)
    
    # Extract OUTPUT
    output_match = re.search(r'(?:OUTPUT|Output|OUTPUT SPEC|Output Format).*?:\s*\n(.*?)(?=\n\n[A-Z]+:|\n[A-Z]+ [A-Z]+:|\Z)', prompt_text, re.DOTALL)
    if output_match:
        structure['output'] = output_match.group(1).strip()
    
    # Extract QUALITY CHECKS
    quality_match = re.search(r'(?:QUALITY|Quality).*?:\s*\n(.*?)(?=\n\n|\Z)', prompt_text, re.DOTALL)
    if quality_match:
        quality_text = quality_match.group(1)
        for line in quality_text.split('\n'):
            line = line.strip()
            if line.startswith('-') or line.startswith('•'):
                structure['quality_checks'].append(line)
    
    return structure

def extract_quick_wins(content: str) -> List[Dict]:
    """Extract quick wins with categorization."""
    # Find Section 9
    patterns = [
        r'## Section 9: Quick Wins.*?\n(.*?)(?=\n## |\n---\n|\Z)',
        r'## 9\) Quick Wins.*?\n(.*?)(?=\n## |\n---\n|\Z)',
        r'## 9\. Quick Wins.*?\n(.*?)(?=\n## |\n---\n|\Z)',
        r'## Quick Wins Library.*?\n(.*?)(?=\n## |\n---\n|\Z)',
    ]
    
    section_content = None
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            section_content = match.group(1).strip()
            break
    
    if not section_content:
        return []
    
    quick_wins = []
    
    # Extract from code block
    code_match = re.search(r'```[^\n]*\n(.*?)```', section_content, re.DOTALL)
    if code_match:
        text = code_match.group(1)
    else:
        text = section_content
    
    # Parse patterns
    for line in text.split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        # Detect category (if present)
        category = None
        pattern_text = line
        
        # Format: "Category → pattern"
        if '→' in line:
            parts = line.split('→', 1)
            category = parts[0].strip().strip('-•').strip()
            pattern_text = parts[1].strip()
        # Format: "Category: pattern"
        elif ':' in line and not line.startswith('"'):
            parts = line.split(':', 1)
            potential_category = parts[0].strip().strip('-•').strip()
            # Check if it looks like a category
            if len(potential_category.split()) <= 3 and potential_category[0].isupper():
                category = potential_category
                pattern_text = parts[1].strip()
        
        # Remove leading bullets
        pattern_text = pattern_text.lstrip('-•').strip()
        
        if pattern_text:
            quick_wins.append({
                'category': category,
                'pattern': pattern_text,
                'original': line
            })
    
    return quick_wins

def extract_lessons(content: str) -> List[str]:
    """Extract lessons learned from Section 8."""
    patterns = [
        r'## Section 8: Lessons.*?\n(.*?)(?=\n## |\n---\n|\Z)',
        r'## 8\) Lessons.*?\n(.*?)(?=\n## |\n---\n|\Z)',
        r'## 8\. Lessons.*?\n(.*?)(?=\n## |\n---\n|\Z)',
    ]
    
    section_content = None
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            section_content = match.group(1).strip()
            break
    
    if not section_content:
        return []
    
    lessons = []
    for line in section_content.split('\n'):
        line = line.strip()
        if line.startswith('-') or line.startswith('•') or re.match(r'^\d+\.', line):
            lesson = line.lstrip('-•0123456789.').strip()
            if lesson:
                lessons.append(lesson)
    
    return lessons

def detect_domain(frontmatter: Dict, content: str) -> str:
    """Detect primary domain/topic."""
    title = frontmatter.get('title', '').lower()
    tags = str(frontmatter.get('tags', '')).lower()
    combined = f"{title} {tags}".lower()
    
    # Check in priority order
    if any(kw in combined for kw in ['zapier', 'automation', 'workflow', 'process']):
        return 'automation'
    elif any(kw in combined for kw in ['api', 'rest', 'fastapi', 'endpoint', 'backend']):
        return 'api-development'
    elif any(kw in combined for kw in ['nextjs', 'next.js', 'react', 'frontend', 'ui', 'web']):
        return 'web-development'
    elif any(kw in combined for kw in ['database', 'chroma', 'sql', 'postgres', 'persistence']):
        return 'database'
    elif any(kw in combined for kw in ['documentation', 'docs', 'readme', 'agents.md']):
        return 'documentation'
    elif any(kw in combined for kw in ['business', 'consulting', 'interview', 'process-automation']):
        return 'business-process'
    elif any(kw in combined for kw in ['data', 'analysis', 'viz', 'chart', 'visualization']):
        return 'data-analysis'
    elif any(kw in combined for kw in ['docker', 'deployment', 'devops', 'ci/cd', 'infrastructure']):
        return 'devops'
    elif any(kw in combined for kw in ['ai', 'ml', 'llm', 'model', 'prompt', 'meta-prompting']):
        return 'ai-ml'
    elif any(kw in combined for kw in ['test', 'tdd', 'testing', 'quality']):
        return 'testing'
    else:
        return 'general'

def score_quality(super_prompt: Optional[Dict], quick_wins: List[Dict], lessons: List[str]) -> str:
    """Score extraction quality: HIGH, MEDIUM, or LOW."""
    score = 0
    
    # Super-prompt scoring
    if super_prompt:
        score += 3
        if super_prompt.get('role') and super_prompt.get('task'):
            score += 2
        if len(super_prompt.get('inputs', [])) >= 3:
            score += 1
        if len(super_prompt.get('process', [])) >= 3:
            score += 1
        if super_prompt.get('quality_checks'):
            score += 1
    
    # Quick wins scoring
    if len(quick_wins) >= 5:
        score += 2
    elif len(quick_wins) >= 3:
        score += 1
    
    # Lessons scoring
    if len(lessons) >= 3:
        score += 1
    
    if score >= 8:
        return 'HIGH'
    elif score >= 4:
        return 'MEDIUM'
    else:
        return 'LOW'

def process_file(filepath: Path) -> Dict:
    """Process a single insights file."""
    print(f"  Processing: {filepath.name}")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract all components
        frontmatter = extract_frontmatter(content)
        super_prompt = extract_super_prompt(content)
        quick_wins = extract_quick_wins(content)
        lessons = extract_lessons(content)
        domain = detect_domain(frontmatter, content)
        quality = score_quality(super_prompt, quick_wins, lessons)
        
        return {
            'filename': filepath.name,
            'file_id': frontmatter.get('thread_fingerprint', filepath.stem),
            'title': frontmatter.get('title', 'Unknown'),
            'date': frontmatter.get('date', 'Unknown'),
            'tags': frontmatter.get('tags', []),
            'domain': domain,
            'quality_score': quality,
            'super_prompt': super_prompt,
            'quick_wins': quick_wins,
            'lessons': lessons,
            'extraction_success': True,
            'word_count': len(content.split())
        }
    
    except Exception as e:
        print(f"    ⚠️  Error: {str(e)}")
        return {
            'filename': filepath.name,
            'extraction_success': False,
            'error': str(e)
        }

def main():
    """Main extraction pipeline."""
    print("🔄 FULL EXTRACTION PIPELINE")
    print("=" * 70)
    print()
    
    insights_path = Path(INSIGHTS_DIR)
    md_files = sorted(list(insights_path.glob("*.md")))
    
    print(f"📁 Found {len(md_files)} files to process")
    print(f"📂 Directory: {INSIGHTS_DIR}")
    print()
    
    # Process all files
    print("⚙️  Extracting content...\n")
    all_data = []
    
    for filepath in md_files:
        data = process_file(filepath)
        all_data.append(data)
    
    print()
    
    # Calculate statistics
    successful = [d for d in all_data if d.get('extraction_success')]
    with_super_prompt = [d for d in successful if d.get('super_prompt')]
    with_quick_wins = [d for d in successful if d.get('quick_wins')]
    
    high_quality = [d for d in successful if d.get('quality_score') == 'HIGH']
    medium_quality = [d for d in successful if d.get('quality_score') == 'MEDIUM']
    low_quality = [d for d in successful if d.get('quality_score') == 'LOW']
    
    # Domain breakdown
    domains = {}
    for d in successful:
        domain = d.get('domain', 'unknown')
        domains[domain] = domains.get(domain, 0) + 1
    
    # Statistics
    print("📊 EXTRACTION RESULTS")
    print("=" * 70)
    print(f"✅ Successfully processed:    {len(successful)}/{len(all_data)}")
    print(f"📝 With Super-Prompts:        {len(with_super_prompt)} files")
    print(f"⚡ With Quick Wins:           {len(with_quick_wins)} files")
    print()
    
    total_quick_wins = sum(len(d.get('quick_wins', [])) for d in successful)
    print(f"🎯 Total Quick Win patterns:  {total_quick_wins}")
    print(f"📚 Total Lessons:             {sum(len(d.get('lessons', [])) for d in successful)}")
    print()
    
    print("🏆 QUALITY DISTRIBUTION")
    print("=" * 70)
    print(f"HIGH   (8+ points):   {len(high_quality):2d} files  ← Create standalone prompts")
    print(f"MEDIUM (4-7 points):  {len(medium_quality):2d} files  ← Add to patterns library")
    print(f"LOW    (0-3 points):  {len(low_quality):2d} files  ← Reference only")
    print()
    
    print("🏷️  DOMAIN BREAKDOWN")
    print("=" * 70)
    for domain, count in sorted(domains.items(), key=lambda x: x[1], reverse=True):
        print(f"{domain:20s} {count:3d} files")
    print()
    
    # Save results
    output_data = {
        'extraction_date': datetime.now().isoformat(),
        'summary': {
            'total_files': len(all_data),
            'successful': len(successful),
            'with_super_prompts': len(with_super_prompt),
            'with_quick_wins': len(with_quick_wins),
            'total_quick_wins': total_quick_wins,
            'high_quality_count': len(high_quality),
            'medium_quality_count': len(medium_quality),
            'low_quality_count': len(low_quality)
        },
        'quality_tiers': {
            'high': [d['filename'] for d in high_quality],
            'medium': [d['filename'] for d in medium_quality],
            'low': [d['filename'] for d in low_quality]
        },
        'domains': domains,
        'files': all_data
    }
    
    output_path = Path(OUTPUT_FILE)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"💾 Complete extraction data saved to:")
    print(f"   {OUTPUT_FILE}")
    print()
    
    # Next steps
    print("✅ EXTRACTION COMPLETE!")
    print()
    print("📋 NEXT STEPS:")
    print(f"1. Review {len(high_quality)} HIGH-quality files for prompt creation")
    print(f"2. Process {total_quick_wins} Quick Win patterns (deduplicate)")
    print(f"3. Run generation script to create Arsenal items")
    print()
    print("🚀 Ready for Phase 3: Generation")

if __name__ == "__main__":
    main()
