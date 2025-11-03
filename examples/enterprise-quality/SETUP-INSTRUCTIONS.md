# Enterprise Quality Setup Instructions

## Directory Structure

Create the following structure in your project:

```
.windsurf/
├── memories/
│   └── enterprise-completion-standards-memory.md
├── rules/
│   └── complete-problem-solving.md (copy from ai-rules-arsenal)
└── workflows/
    ├── run-tests-and-fix.md (copy from ai-workflows-arsenal)
    ├── code-review-assistant.md (copy from ai-workflows-arsenal)
    └── security-scan.md (copy from ai-workflows-arsenal)
```

## Setup Commands

```powershell
# Create directories
New-Item -ItemType Directory -Path ".windsurf" -Force
New-Item -ItemType Directory -Path ".windsurf\rules" -Force
New-Item -ItemType Directory -Path ".windsurf\memories" -Force
New-Item -ItemType Directory -Path ".windsurf\workflows" -Force

# Copy the complete problem-solving rule
Copy-Item "c:\Users\theca\CascadeProjects\ai-rules-arsenal\windsurf\by-domain\complete-problem-solving.md" ".windsurf\rules\"

# Copy the enterprise completion standards memory (create this file - see below)
# This file should be created in windsurf-memories-arsenal first

# Copy workflows (when available in ai-workflows-arsenal)
# Copy-Item "path\to\run-tests-and-fix.md" ".windsurf\workflows\"
# Copy-Item "path\to\code-review-assistant.md" ".windsurf\workflows\"
# Copy-Item "path\to\security-scan.md" ".windsurf\workflows\"
```

## Files to Copy

1. **Complete Problem-Solving Rule** ✅ CREATED
   - Source: `c:\Users\theca\CascadeProjects\ai-rules-arsenal\windsurf\by-domain\complete-problem-solving.md`
   - Destination: `.windsurf\rules\complete-problem-solving.md`

2. **Enterprise Completion Standards Memory** ⏳ TO BE CREATED
   - Will be created in windsurf-memories-arsenal
   - Then copy to `.windsurf\memories\enterprise-completion-standards-memory.md`

3. **Workflows** (copy from ai-workflows-arsenal when available)
   - `run-tests-and-fix.md`
   - `code-review-assistant.md`
   - `security-scan.md`

## Next Steps

1. See README.md for complete usage guide
2. Customize enterprise-completion-standards-memory.md for your team
3. Start using `@complete-mode` for critical work
