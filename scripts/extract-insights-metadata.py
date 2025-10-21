#!/usr/bin/env python3
"""
Extract metadata, super-prompts, and quick wins from all prompt-insights files.
Phase 1: Assessment - understand what we have before bulk processing.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple
import json

# Configuration
INSIGHTS_DIR = r"C:\Users\theca\CascadeProjects\chriscreateswithai-nextjs\content\prompt-insights"
OUTPUT_FILE = r"C:\Users\theca\CascadeProjects\arsenal-integration-hub\scripts\insights-summary.json"

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

def extract_section(content: str, section_patterns: List[str]) -> str:
    """Extract content from a section using multiple possible heading patterns."""
    for pattern in section_patterns:
        # Try to find the section
        match = re.search(
            rf'{pattern}.*?\n(.*?)(?=\n## |\n---\n|\Z)',
            content,
            re.DOTALL | re.IGNORECASE
        )
        if match:
            return match.group(1).strip()
    
    return ""

def extract_quick_wins(content: str) -> List[str]:
    """Extract individual quick win patterns from Section 9."""
    quick_wins_section = extract_section(
        content,
        [
            r'## Section 9: Quick Wins',
            r'## 9\) Quick Wins',
            r'## 9\. Quick Wins'
        ]
    )
    
    if not quick_wins_section:
        return []
    
    # Extract patterns - they're usually in a code block or as bullets
    patterns = []
    
    # Try code block first
    code_match = re.search(r'```[^\n]*\n(.*?)```', quick_wins_section, re.DOTALL)
    if code_match:
        for line in code_match.group(1).split('\n'):
            line = line.strip()
            if line and not line.startswith('#'):
                patterns.append(line)
    else:
        # Try bullet points
        for line in quick_wins_section.split('\n'):
            line = line.strip()
            if line.startswith('-') or line.startswith('•'):
                patterns.append(line[1:].strip())
    
    return patterns

def analyze_file(filepath: Path) -> Dict:
    """Analyze a single insights file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata
        frontmatter = extract_frontmatter(content)
        
        # Extract super-prompt
        super_prompt = extract_section(
            content,
            [
                r'## Section 4: Super-Prompt',
                r'## 4\) Super-Prompt',
                r'## 4\. Super-Prompt',
                r'## Super-Prompt'
            ]
        )
        
        # Extract quick wins
        quick_wins = extract_quick_wins(content)
        
        # Calculate metrics
        word_count = len(content.split())
        has_super_prompt = bool(super_prompt)
        has_quick_wins = bool(quick_wins)
        super_prompt_length = len(super_prompt.split()) if super_prompt else 0
        
        return {
            'filename': filepath.name,
            'title': frontmatter.get('title', 'Unknown'),
            'date': frontmatter.get('date', 'Unknown'),
            'tags': frontmatter.get('tags', ''),
            'thread_id': frontmatter.get('thread_fingerprint', ''),
            'word_count': word_count,
            'has_super_prompt': has_super_prompt,
            'super_prompt_length': super_prompt_length,
            'has_quick_wins': has_quick_wins,
            'quick_wins_count': len(quick_wins),
            'quick_wins': quick_wins[:3],  # First 3 for preview
            'super_prompt_preview': super_prompt[:300] if super_prompt else ""
        }
    
    except Exception as e:
        return {
            'filename': filepath.name,
            'error': str(e)
        }

def categorize_by_domain(files_data: List[Dict]) -> Dict[str, List[str]]:
    """Categorize files by detected domain/topic."""
    domains = {
        'API Development': [],
        'Web Development': [],
        'Database': [],
        'Automation': [],
        'Documentation': [],
        'Business Process': [],
        'Data Analysis': [],
        'DevOps/Infrastructure': [],
        'AI/ML': [],
        'Other': []
    }
    
    for file_data in files_data:
        if 'error' in file_data:
            continue
        
        title = file_data['title'].lower()
        tags = str(file_data['tags']).lower()
        combined = f"{title} {tags}"
        
        categorized = False
        
        if any(kw in combined for kw in ['api', 'rest', 'fastapi', 'endpoint']):
            domains['API Development'].append(file_data['filename'])
            categorized = True
        elif any(kw in combined for kw in ['nextjs', 'react', 'frontend', 'ui', 'web']):
            domains['Web Development'].append(file_data['filename'])
            categorized = True
        elif any(kw in combined for kw in ['database', 'chroma', 'sql', 'postgres']):
            domains['Database'].append(file_data['filename'])
            categorized = True
        elif any(kw in combined for kw in ['automation', 'zapier', 'workflow', 'process']):
            domains['Automation'].append(file_data['filename'])
            categorized = True
        elif any(kw in combined for kw in ['documentation', 'docs', 'readme']):
            domains['Documentation'].append(file_data['filename'])
            categorized = True
        elif any(kw in combined for kw in ['business', 'consulting', 'interview']):
            domains['Business Process'].append(file_data['filename'])
            categorized = True
        elif any(kw in combined for kw in ['data', 'analysis', 'viz', 'chart']):
            domains['Data Analysis'].append(file_data['filename'])
            categorized = True
        elif any(kw in combined for kw in ['docker', 'deployment', 'devops', 'ci/cd']):
            domains['DevOps/Infrastructure'].append(file_data['filename'])
            categorized = True
        elif any(kw in combined for kw in ['ai', 'ml', 'llm', 'model']):
            domains['AI/ML'].append(file_data['filename'])
            categorized = True
        
        if not categorized:
            domains['Other'].append(file_data['filename'])
    
    # Remove empty domains
    return {k: v for k, v in domains.items() if v}

def main():
    """Main extraction and analysis."""
    print("🔍 Phase 1: Assessing Prompt Insights Files")
    print("=" * 60)
    
    insights_path = Path(INSIGHTS_DIR)
    md_files = list(insights_path.glob("*.md"))
    
    print(f"\n📁 Found {len(md_files)} markdown files")
    print(f"📂 Directory: {INSIGHTS_DIR}\n")
    
    # Analyze all files
    print("📊 Analyzing files...")
    all_data = []
    for filepath in md_files:
        data = analyze_file(filepath)
        all_data.append(data)
        
        # Progress indicator
        if len(all_data) % 10 == 0:
            print(f"   Processed {len(all_data)}/{len(md_files)} files...")
    
    print(f"✅ Analyzed {len(all_data)} files\n")
    
    # Generate statistics
    total_files = len(all_data)
    with_super_prompt = sum(1 for d in all_data if d.get('has_super_prompt'))
    with_quick_wins = sum(1 for d in all_data if d.get('has_quick_wins'))
    avg_word_count = sum(d.get('word_count', 0) for d in all_data) / total_files
    total_quick_wins = sum(d.get('quick_wins_count', 0) for d in all_data)
    
    print("📈 SUMMARY STATISTICS")
    print("=" * 60)
    print(f"Total files:              {total_files}")
    print(f"With Super-Prompts:       {with_super_prompt} ({with_super_prompt/total_files*100:.0f}%)")
    print(f"With Quick Wins:          {with_quick_wins} ({with_quick_wins/total_files*100:.0f}%)")
    print(f"Average word count:       {avg_word_count:.0f} words")
    print(f"Total Quick Win patterns: {total_quick_wins}")
    print(f"Avg Quick Wins per file:  {total_quick_wins/with_quick_wins:.1f}\n")
    
    # Categorize by domain
    domains = categorize_by_domain(all_data)
    
    print("🏷️  DOMAIN BREAKDOWN")
    print("=" * 60)
    for domain, files in sorted(domains.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"{domain:25s} {len(files):3d} files")
    print()
    
    # Identify high-value candidates
    print("⭐ HIGH-VALUE CANDIDATES (for priority extraction)")
    print("=" * 60)
    
    high_value = [
        d for d in all_data 
        if d.get('has_super_prompt') 
        and d.get('quick_wins_count', 0) >= 5
        and d.get('super_prompt_length', 0) > 100
    ]
    
    high_value.sort(key=lambda x: x.get('quick_wins_count', 0), reverse=True)
    
    for i, file_data in enumerate(high_value[:10], 1):
        print(f"{i:2d}. {file_data['filename']}")
        print(f"    {file_data['title']}")
        print(f"    Quick Wins: {file_data['quick_wins_count']}, "
              f"Super-Prompt: {file_data['super_prompt_length']} words\n")
    
    # Save detailed results
    output_data = {
        'summary': {
            'total_files': total_files,
            'with_super_prompt': with_super_prompt,
            'with_quick_wins': with_quick_wins,
            'avg_word_count': avg_word_count,
            'total_quick_wins': total_quick_wins
        },
        'domains': domains,
        'high_value_files': [d['filename'] for d in high_value[:15]],
        'all_files': all_data
    }
    
    output_path = Path(OUTPUT_FILE)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"💾 Detailed results saved to: {OUTPUT_FILE}")
    print(f"\n✅ Phase 1 Assessment Complete!")
    print("\n📋 NEXT STEPS:")
    print("1. Review high-value candidates above")
    print("2. Decide: Extract all or focus on top domains?")
    print("3. Run Phase 2 extraction script")

if __name__ == "__main__":
    main()
