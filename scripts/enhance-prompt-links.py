#!/usr/bin/env python3
"""
Enhance auto-generated prompts with richer cross-links and related items.
"""

import re
from pathlib import Path
from typing import Dict, List

PROMPT_ARSENAL = Path(r"C:\Users\theca\CascadeProjects\prompt-arsenal")

# Prompts to enhance (12 auto-generated ones)
AUTO_GENERATED_PROMPTS = [
    "automation/workflow/prompt-insights-zapier-mcp-tools-thread.md",
    "automation/workflow/prompt-insights-n8n-workflow-programmatic-thread.md",
    "ai-prompting/analysis/prompt-insights-seo-faq-ranking-thread.md",
    "ai-prompting/analysis/prompt-insights-refactoring-a-pine-script-v6.md",
    "ai-prompting/analysis/prompt-insights-forensics-chainmining-and-upgrades.md",
    "ai-prompting/analysis/prompt-insights-anydoc-studio-thread.md",
    "ai-prompting/analysis/prompt-insights-croquet-venture-thread.md",
    "ai-prompting/analysis/prompt-insights-port-city-fence-seoaeo-agent.md",
    "ai-prompting/analysis/prompt-forensics-chainminer-opportunity-hunter.md",
    "ai-prompting/analysis/prompt-forensics-report-prior-thread-audit.md",
    "ai-prompting/analysis/prompt-forensics-report-repo-audit-prompt-design.md",
    "ai-prompting/analysis/super-prompt-forensics-opportunity-audit.md",
]

# Related prompts by category
RELATED_PROMPTS = {
    "automation": [
        ("Zapier MCP Tools", "automation/workflow/prompt-insights-zapier-mcp-tools-thread.md"),
        ("N8N Workflow Builder", "automation/workflow/prompt-insights-n8n-workflow-programmatic-thread.md"),
    ],
    "meta-prompting": [
        ("Prompt Forensics Analyzer", "meta-prompting/prompt-forensics-analyzer.md"),
        ("Insights Intake Processor", "meta-prompting/insights-intake-processor.md"),
        ("Opportunity Hunter", "ai-prompting/analysis/prompt-forensics-chainminer-opportunity-hunter.md"),
        ("Thread Audit Report", "ai-prompting/analysis/prompt-forensics-report-prior-thread-audit.md"),
        ("Super-Prompt Forensics", "ai-prompting/analysis/super-prompt-forensics-opportunity-audit.md"),
    ],
    "documentation": [
        ("Structured Document Architect", "development/documentation/structured-document-architect.md"),
        ("Add Citations", "development/documentation/add-citations-to-output.md"),
        ("Extract Template", "development/documentation/extract-reusable-template.md"),
    ],
}

def get_related_prompts(prompt_path: str) -> List[tuple]:
    """Get related prompts based on the prompt's category."""
    related = []
    
    if "automation" in prompt_path:
        related.extend(RELATED_PROMPTS["automation"])
        related.extend(RELATED_PROMPTS["documentation"][:1])  # Add one doc prompt
    elif "forensics" in prompt_path or "insights" in prompt_path:
        related.extend(RELATED_PROMPTS["meta-prompting"])
        related.extend(RELATED_PROMPTS["documentation"])
    
    # Remove self from related
    related = [(name, path) for name, path in related if path != prompt_path]
    
    return related[:4]  # Max 4 related prompts

def create_enhanced_related_section(prompt_path: str) -> str:
    """Create enhanced 'Related Arsenal Items' section."""
    
    related_prompts = get_related_prompts(prompt_path)
    
    section = """

## 🔗 Related Arsenal Items

### 📝 Related Prompts
"""
    
    for name, path in related_prompts:
        section += f"- **[{name}](https://github.com/ChrisTansey007/prompt-arsenal/blob/main/{path})** - Complementary prompt pattern\n"
    
    section += """
### 💭 Memories
- **[Prompt Patterns Library](https://github.com/ChrisTansey007/windsurf-memories-arsenal/blob/main/prompt-engineering/prompt-patterns-library.md)** - Pattern catalog and techniques

### ⚙️ Rules
- **[Prompt Quality Standards](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/prompt-design/prompt-quality-standards.md)** - 5-D framework for prompts

### 🔄 Workflows
- **[Meta-Prompting Workflow](https://github.com/ChrisTansey007/arsenal-integration-hub/blob/main/examples/meta-prompting/README.md)** - Complete prompt extraction pipeline

### 🛠️ Tools
- **[Arsenal CLI](https://github.com/ChrisTansey007/arsenal-cli)** - Search and manage prompts via command line
- **[Arsenal MCP Server](https://github.com/ChrisTansey007/arsenal-mcp-server)** - Access prompts via Model Context Protocol
"""
    
    return section

def enhance_prompt(prompt_path: Path) -> bool:
    """Enhance a single prompt file with richer links."""
    
    if not prompt_path.exists():
        return False
    
    with open(prompt_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has enhanced section
    if "### 📝 Related Prompts" in content:
        print(f"   ⏭️  Already enhanced: {prompt_path.name}")
        return False
    
    # Find the existing "Related Arsenal Items" section
    pattern = r'## 🔗 Related Arsenal Items.*?(?=\n---|\n## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        # No existing section, add at end before final notes
        pattern = r'(---\n\n\*\*Result:.*?\*\* 🚀)'
        replacement = create_enhanced_related_section(str(prompt_path.relative_to(PROMPT_ARSENAL))) + r'\n\n---\n\n\1'
        content = re.sub(pattern, replacement, content)
    else:
        # Replace existing section
        enhanced_section = create_enhanced_related_section(str(prompt_path.relative_to(PROMPT_ARSENAL)))
        content = re.sub(pattern, enhanced_section.strip(), content, flags=re.DOTALL)
    
    # Write back
    with open(prompt_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Enhance all auto-generated prompts."""
    print("🔗 ENHANCING AUTO-GENERATED PROMPTS")
    print("=" * 70)
    print(f"📁 Processing {len(AUTO_GENERATED_PROMPTS)} prompts...\n")
    
    enhanced_count = 0
    skipped_count = 0
    
    for rel_path in AUTO_GENERATED_PROMPTS:
        prompt_path = PROMPT_ARSENAL / rel_path
        print(f"📝 {rel_path}")
        
        if enhance_prompt(prompt_path):
            enhanced_count += 1
            print(f"   ✅ Enhanced with richer cross-links\n")
        else:
            skipped_count += 1
            print()
    
    print("=" * 70)
    print(f"✅ Enhanced: {enhanced_count}")
    print(f"⏭️  Skipped: {skipped_count}")
    print(f"\n📋 Next steps:")
    print(f"1. Review enhanced prompts in prompt-arsenal")
    print(f"2. Commit changes:")
    print(f"   cd {PROMPT_ARSENAL}")
    print(f"   git add .")
    print(f"   git commit -m 'feat: enhance 12 prompts with richer cross-links'")
    print(f"   git push origin main")

if __name__ == '__main__':
    main()
