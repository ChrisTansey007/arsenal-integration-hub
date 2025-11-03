#!/usr/bin/env python3
"""
Update all Arsenal READMEs with ecosystem links
"""

import re
from pathlib import Path
from typing import Dict

# Repository paths
REPOS = {
    'ai-rules-arsenal': r'C:\Users\theca\CascadeProjects\ai-rules-arsenal',
    'ai-workflows-arsenal': r'C:\Users\theca\CascadeProjects\ai-workflows-arsenal',
    'ai-scripts-arsenal': r'C:\Users\theca\CascadeProjects\ai-scripts-arsenal',
}

ECOSYSTEM_SECTION = """
---

## 🔗 Arsenal Ecosystem

**This repository is part of the complete Arsenal ecosystem for AI-powered development.**

### Content Repositories
- **[Windsurf Memories Arsenal](https://github.com/ChrisTansey007/windsurf-memories-arsenal)** - What Cascade remembers
- **[Prompt Arsenal](https://github.com/ChrisTansey007/prompt-arsenal)** - What to ask/build (26 prompts)
- **[AI Rules Arsenal](https://github.com/ChrisTansey007/ai-rules-arsenal)** - How Cascade behaves{rules_marker}
- **[AI Workflows Arsenal](https://github.com/ChrisTansey007/ai-workflows-arsenal)** - Multi-step processes{workflows_marker}
- **[AI Scripts Arsenal](https://github.com/ChrisTansey007/ai-scripts-arsenal)** - Automation scripts{scripts_marker}

### Integration & Tooling
- **[Arsenal Integration Hub](https://github.com/ChrisTansey007/arsenal-integration-hub)** - How to use them together
- **[Arsenal Context Server](https://github.com/ChrisTansey007/arsenal-context-server)** - MCP context delivery
- **[Arsenal CLI](https://github.com/ChrisTansey007/arsenal-cli)** - Command-line management
- **[Arsenal MCP Server](https://github.com/ChrisTansey007/arsenal-mcp-server)** - Model Context Protocol server

### 🚀 Get Started

```bash
# Install complete Arsenal ecosystem
curl -sSL https://raw.githubusercontent.com/ChrisTansey007/arsenal-integration-hub/main/scripts/install-all.sh | bash

# Or use Arsenal CLI
npm install -g arsenal-cli
arsenal install all
```

**See [Arsenal Integration Hub](https://github.com/ChrisTansey007/arsenal-integration-hub) for complete guides!**
"""

def update_readme(repo_name: str, repo_path: str):
    """Update README for a specific repository."""
    print(f"\n📝 Updating {repo_name}...")
    
    readme_path = Path(repo_path) / 'README.md'
    
    if not readme_path.exists():
        print(f"   ⚠️  README.md not found at {readme_path}")
        return False
    
    # Read current content
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add marker for current repo
    markers = {
        'rules_marker': '',
        'workflows_marker': '',
        'scripts_marker': ''
    }
    
    if repo_name == 'ai-rules-arsenal':
        markers['rules_marker'] = ' ← YOU ARE HERE'
    elif repo_name == 'ai-workflows-arsenal':
        markers['workflows_marker'] = ' ← YOU ARE HERE'
    elif repo_name == 'ai-scripts-arsenal':
        markers['scripts_marker'] = ' ← YOU ARE HERE'
    
    ecosystem_text = ECOSYSTEM_SECTION.format(**markers)
    
    # Check if ecosystem section already exists
    if '## 🔗 Arsenal Ecosystem' in content:
        print(f"   ℹ️  Ecosystem section already exists, replacing...")
        # Replace existing section (find everything between the section and next ## or end)
        pattern = r'---\s*\n\n## 🔗 Arsenal Ecosystem.*?(?=\n---\n\n##|\Z)'
        content = re.sub(pattern, ecosystem_text.strip(), content, flags=re.DOTALL)
    else:
        print(f"   ➕ Adding new ecosystem section...")
        # Find a good place to insert (before ## License or at the end)
        if '## License' in content or '## 📝 License' in content:
            # Insert before license
            content = re.sub(
                r'(---\s*\n\n## (?:📝 )?License)',
                ecosystem_text + r'\n\n\1',
                content
            )
        else:
            # Append at end
            content += '\n' + ecosystem_text
    
    # Write back
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"   ✅ Updated {repo_name}/README.md")
    return True

def main():
    """Update all repository READMEs."""
    print("🔗 UPDATING ARSENAL ECOSYSTEM LINKS")
    print("=" * 70)
    
    success_count = 0
    
    for repo_name, repo_path in REPOS.items():
        if update_readme(repo_name, repo_path):
            success_count += 1
    
    print(f"\n{'=' * 70}")
    print(f"✅ Updated {success_count}/{len(REPOS)} repositories")
    print(f"\n📋 Next steps:")
    print(f"1. Review changes in each repository")
    print(f"2. Commit and push:")
    for repo_name in REPOS.keys():
        print(f"   cd {REPOS[repo_name]}")
        print(f"   git add README.md")
        print(f"   git commit -m 'docs: add ecosystem section with new repos'")
        print(f"   git push origin main")
        print()

if __name__ == '__main__':
    main()
