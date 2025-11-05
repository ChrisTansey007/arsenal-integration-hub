# 📋 How to Add Arsenal Rules & Workflows to Your Project

**Universal guide for adding any Arsenal rules, workflows, and memories to your Windsurf project**

---

## 🎯 What This Guide Is

This guide shows you how to **add Arsenal content to your project** so Windsurf's Cascade AI can use it to help you code better.

**Works for:**
- ✅ Any Arsenal rules from ai-rules-arsenal
- ✅ Any workflows from ai-workflows-arsenal  
- ✅ Any memories from windsurf-memories-arsenal
- ✅ Any project (Next.js, React, Python, etc.)
- ✅ Windows, macOS, or Linux

---

## 📋 Prerequisites

Before starting, make sure you have:

1. **Arsenal repositories installed** (typically in `~/arsenals/`)
   ```bash
   # Check if arsenals are installed
   ls ~/arsenals/
   # Should see: ai-rules-arsenal, ai-workflows-arsenal, etc.
   ```

2. **If not installed**, run:
   ```bash
   # Install all Arsenal repos
   curl -sSL https://raw.githubusercontent.com/ChrisTansey007/arsenal-integration-hub/main/scripts/install-all.sh | bash
   ```

3. **Windsurf IDE** with Cascade enabled

---

## 🚀 Method 1: Quick Setup Script (Recommended)

### **Create a simple setup script for your project:**

**For Linux/macOS (bash):**

```bash
#!/bin/bash
# Arsenal Setup Script - Customize for your project

set -e

echo "🔧 Setting up Arsenal for this project..."

# ============================================
# 1. Create .windsurf directory structure
# ============================================

if [ ! -d ".windsurf" ]; then
    echo "📁 Creating .windsurf directory..."
    mkdir -p .windsurf/{memories,rules,workflows}
    echo "   ✅ Directory structure created"
else
    echo "📁 .windsurf directory already exists"
fi

# ============================================
# 2. Check Arsenal installation
# ============================================

if [ ! -d "$HOME/arsenals" ]; then
    echo "❌ Arsenal repositories not found."
    echo "   Please install: curl -sSL https://[install-url] | bash"
    exit 1
fi

# ============================================
# 3. Copy Rules (CUSTOMIZE THIS SECTION)
# ============================================

echo ""
echo "📋 Copying Arsenal rules..."

# Example: Copy a Next.js rule
if [ -f "$HOME/arsenals/ai-rules-arsenal/windsurf/by-framework/nextjs-15-app-router.md" ]; then
    echo "  ✅ Next.js 15 App Router"
    cp "$HOME/arsenals/ai-rules-arsenal/windsurf/by-framework/nextjs-15-app-router.md" .windsurf/rules/
fi

# Example: Copy a TypeScript rule
if [ -f "$HOME/arsenals/ai-rules-arsenal/windsurf/by-domain/typescript-strict-development.md" ]; then
    echo "  ✅ TypeScript Strict Development"
    cp "$HOME/arsenals/ai-rules-arsenal/windsurf/by-domain/typescript-strict-development.md" .windsurf/rules/
fi

# Add more rules as needed...

# ============================================
# 4. Copy Workflows (CUSTOMIZE THIS SECTION)
# ============================================

echo ""
echo "🔄 Copying Arsenal workflows..."

# Example: Copy a code review workflow
if [ -f "$HOME/arsenals/ai-workflows-arsenal/windsurf/development/code-review-process.md" ]; then
    echo "  ✅ Code Review Process"
    cp "$HOME/arsenals/ai-workflows-arsenal/windsurf/development/code-review-process.md" .windsurf/workflows/
fi

# Add more workflows as needed...

# ============================================
# 5. Copy Memories (OPTIONAL)
# ============================================

echo ""
echo "💭 Copying Arsenal memories (optional)..."

# Example: Copy a Next.js memory
if [ -f "$HOME/arsenals/windsurf-memories-arsenal/frameworks/nextjs-app-router.md" ]; then
    echo "  ✅ Next.js App Router Memory"
    cp "$HOME/arsenals/windsurf-memories-arsenal/frameworks/nextjs-app-router.md" .windsurf/memories/
fi

# Add more memories as needed...

# ============================================
# 6. Summary
# ============================================

rule_count=$(ls -1 .windsurf/rules/*.md 2>/dev/null | wc -l)
workflow_count=$(ls -1 .windsurf/workflows/*.md 2>/dev/null | wc -l)
memory_count=$(ls -1 .windsurf/memories/*.md 2>/dev/null | wc -l)

echo ""
echo "✅ Arsenal setup complete!"
echo ""
echo "📊 Summary:"
echo "   - Rules installed: $rule_count"
echo "   - Workflows installed: $workflow_count"
echo "   - Memories installed: $memory_count"
echo ""
echo "🔄 Next steps:"
echo "   1. Reload Windsurf to activate new rules"
echo "   2. Test with: 'Hey Cascade, what rules are active?'"
echo "   3. Start coding with AI superpowers! 🚀"
echo ""
```

**Save as:** `setup-arsenal.sh` in your project root

**Run it:**
```bash
chmod +x setup-arsenal.sh
./setup-arsenal.sh
```

---

**For Windows (PowerShell):**

```powershell
# Arsenal Setup Script - Customize for your project

Write-Host "🔧 Setting up Arsenal for this project..." -ForegroundColor Cyan

# ============================================
# 1. Create .windsurf directory structure
# ============================================

if (-not (Test-Path ".windsurf")) {
    Write-Host "📁 Creating .windsurf directory..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Force -Path .windsurf\rules | Out-Null
    New-Item -ItemType Directory -Force -Path .windsurf\workflows | Out-Null
    New-Item -ItemType Directory -Force -Path .windsurf\memories | Out-Null
    Write-Host "   ✅ Directory structure created" -ForegroundColor Green
} else {
    Write-Host "📁 .windsurf directory already exists" -ForegroundColor Yellow
}

# ============================================
# 2. Check Arsenal installation
# ============================================

$arsenalPath = "$env:USERPROFILE\arsenals"
if (-not (Test-Path $arsenalPath)) {
    Write-Host "❌ Arsenal repositories not found at $arsenalPath" -ForegroundColor Red
    Write-Host "   Please install Arsenal repos first" -ForegroundColor Red
    exit 1
}

# ============================================
# 3. Copy Rules (CUSTOMIZE THIS SECTION)
# ============================================

Write-Host "`n📋 Copying Arsenal rules..." -ForegroundColor Cyan

# Example: Copy a Next.js rule
$rule1 = "$arsenalPath\ai-rules-arsenal\windsurf\by-framework\nextjs-15-app-router.md"
if (Test-Path $rule1) {
    Write-Host "  ✅ Next.js 15 App Router" -ForegroundColor Green
    Copy-Item -Path $rule1 -Destination .windsurf\rules\
}

# Example: Copy a TypeScript rule
$rule2 = "$arsenalPath\ai-rules-arsenal\windsurf\by-domain\typescript-strict-development.md"
if (Test-Path $rule2) {
    Write-Host "  ✅ TypeScript Strict Development" -ForegroundColor Green
    Copy-Item -Path $rule2 -Destination .windsurf\rules\
}

# Add more rules as needed...

# ============================================
# 4. Copy Workflows (CUSTOMIZE THIS SECTION)
# ============================================

Write-Host "`n🔄 Copying Arsenal workflows..." -ForegroundColor Cyan

# Example: Copy a workflow
$workflow1 = "$arsenalPath\ai-workflows-arsenal\windsurf\development\code-review-process.md"
if (Test-Path $workflow1) {
    Write-Host "  ✅ Code Review Process" -ForegroundColor Green
    Copy-Item -Path $workflow1 -Destination .windsurf\workflows\
}

# Add more workflows as needed...

# ============================================
# 5. Copy Memories (OPTIONAL)
# ============================================

Write-Host "`n💭 Copying Arsenal memories (optional)..." -ForegroundColor Cyan

# Example: Copy a memory
$memory1 = "$arsenalPath\windsurf-memories-arsenal\frameworks\nextjs-app-router.md"
if (Test-Path $memory1) {
    Write-Host "  ✅ Next.js App Router Memory" -ForegroundColor Green
    Copy-Item -Path $memory1 -Destination .windsurf\memories\
}

# Add more memories as needed...

# ============================================
# 6. Summary
# ============================================

$ruleCount = (Get-ChildItem .windsurf\rules\*.md -ErrorAction SilentlyContinue).Count
$workflowCount = (Get-ChildItem .windsurf\workflows\*.md -ErrorAction SilentlyContinue).Count
$memoryCount = (Get-ChildItem .windsurf\memories\*.md -ErrorAction SilentlyContinue).Count

Write-Host "`n✅ Arsenal setup complete!" -ForegroundColor Green
Write-Host "`n📊 Summary:" -ForegroundColor Cyan
Write-Host "   - Rules installed: $ruleCount" -ForegroundColor White
Write-Host "   - Workflows installed: $workflowCount" -ForegroundColor White
Write-Host "   - Memories installed: $memoryCount" -ForegroundColor White
Write-Host "`n🔄 Next steps:" -ForegroundColor Cyan
Write-Host "   1. Reload Windsurf to activate new rules" -ForegroundColor White
Write-Host "   2. Test with: 'Hey Cascade, what rules are active?'" -ForegroundColor White
Write-Host "   3. Start coding with AI superpowers! 🚀" -ForegroundColor White
Write-Host ""
```

**Save as:** `setup-arsenal.ps1` in your project root

**Run it:**
```powershell
.\setup-arsenal.ps1
```

---

## 🖱️ Method 2: Manual Setup (Using File Explorer/Finder)

### **Step-by-Step:**

#### **1. Create Directory Structure**

In your project root, create:
```
your-project/
└── .windsurf/
    ├── rules/
    ├── workflows/
    └── memories/
```

#### **2. Browse Arsenal Repository**

Open your file explorer and navigate to:
- **Windows:** `C:\Users\[YourUsername]\arsenals\`
- **macOS/Linux:** `~/arsenals/`

#### **3. Copy Files You Need**

**For Rules:**
- Browse: `arsenals/ai-rules-arsenal/windsurf/`
- Find rules you want (see catalog below)
- Copy `.md` files to your project's `.windsurf/rules/`

**For Workflows:**
- Browse: `arsenals/ai-workflows-arsenal/windsurf/`
- Find workflows you want
- Copy `.md` files to your project's `.windsurf/workflows/`

**For Memories:**
- Browse: `arsenals/windsurf-memories-arsenal/`
- Find memories you want
- Copy `.md` files to your project's `.windsurf/memories/`

#### **4. Reload Windsurf**

- Close and reopen Windsurf, OR
- Click the refresh button in the Rules/Workflows panel

---

## 🎨 Method 3: Using Windsurf UI

### **Step-by-Step:**

#### **1. Open Customizations Panel**

- In Windsurf, click the **Settings icon** (bottom left)
- Select **"Rules, Memories & Workflows"**
- OR use keyboard shortcut: `Ctrl+Shift+P` → "Open Customizations"

#### **2. Add Rules**

1. Click the **"Rules"** tab
2. Click **"+ Project"** button (for project-specific) OR **"+ Global"** (for all projects)
3. File browser opens
4. Navigate to: `arsenals/ai-rules-arsenal/windsurf/[category]/`
5. Select the `.md` files you want
6. Click **"Open"**

#### **3. Add Workflows**

1. Click the **"Workflows"** tab
2. Click **"+ Project"** or **"+ Global"**
3. Navigate to: `arsenals/ai-workflows-arsenal/windsurf/[category]/`
4. Select workflow files
5. Click **"Open"**

#### **4. Add Memories**

1. Click the **"Memories"** tab
2. Click **"+ Project"** or **"+ Global"**
3. Navigate to: `arsenals/windsurf-memories-arsenal/[category]/`
4. Select memory files
5. Click **"Open"**

#### **5. Verify**

- Rules, workflows, and memories should now appear in their respective tabs
- Click on any item to preview its content

---

## 📚 Arsenal Content Catalog

### **Available Rules (ai-rules-arsenal)**

**By Framework:**
```
windsurf/by-framework/
├── nextjs-15-app-router.md          # Next.js 15 patterns
├── mdx-content-management.md        # MDX content systems
├── react-patterns.md                # React best practices
├── fastapi-patterns.md              # FastAPI development
└── vite-esm-modules.md             # Vite ESM handling
```

**By Domain:**
```
windsurf/by-domain/
├── frontend-ux-patterns.md          # UX and styling
├── typescript-strict-development.md # TypeScript standards
├── complete-problem-solving.md      # Problem-solving methodology
├── closure-audit.md                 # Task completion audits
└── code-style.md                   # Code style standards
```

**Platform-Specific:**
```
windsurf/platform-specific/
└── windows-powershell-git.md       # Windows Git commands
```

**Arsenal Meta:**
```
windsurf/arsenal-meta/
├── rule-writing-standards.md        # How to write rules
├── integration-example-standards.md # How to create examples
└── documentation-update-checklist.md # How to update docs
```

### **Available Workflows (ai-workflows-arsenal)**

**Arsenal Management:**
```
windsurf/arsenal-management/
└── integrate-ruleminer-output.md    # RuleMiner integration workflow
```

**Development:**
```
windsurf/development/
├── code-review-process.md           # Code review workflow
├── testing-workflow.md              # Testing procedures
└── git-commit-workflow.md          # Git commit standards
```

### **Available Memories (windsurf-memories-arsenal)**

**Frameworks:**
```
frameworks/
├── nextjs-app-router.md            # Next.js context
├── react-patterns.md               # React patterns
├── fastapi-structure.md            # FastAPI structure
└── react-native-setup.md           # React Native setup
```

---

## 🎯 Choosing What to Install

### **Start Small**

Don't install everything! Start with:
- **2-3 rules** for your main framework/domain
- **1-2 workflows** for common tasks
- **1 memory** for your project context

### **Common Combinations**

**For Next.js 15 Projects:**
```bash
Rules:
- nextjs-15-app-router.md
- typescript-strict-development.md
- frontend-ux-patterns.md

Workflows:
- code-review-process.md

Memories:
- nextjs-app-router.md
```

**For Python/FastAPI Projects:**
```bash
Rules:
- fastapi-patterns.md
- complete-problem-solving.md

Workflows:
- testing-workflow.md

Memories:
- fastapi-structure.md
```

**For Arsenal Content Creation:**
```bash
Rules:
- rule-writing-standards.md
- integration-example-standards.md
- documentation-update-checklist.md

Workflows:
- integrate-ruleminer-output.md
```

---

## 💡 Pro Tips

### **1. Project vs Global**

**Project-Specific (`.windsurf/` in project):**
- ✅ Rules specific to this project
- ✅ Can commit to Git (share with team)
- ✅ Keeps other projects uncluttered
- ✅ Easy to customize per project

**Global (Windsurf settings):**
- ✅ Rules apply to ALL projects
- ✅ Universal patterns (TypeScript, Git, etc.)
- ✅ Always available
- ❌ Can't commit to Git
- ❌ Same rules for everything

**Recommendation:** Start with project-specific, move to global if you use everywhere.

### **2. Update Regularly**

Arsenal repos are updated frequently:
```bash
# Pull latest Arsenal content
cd ~/arsenals
for repo in */; do
  cd "$repo" && git pull && cd ..
done

# Re-run your setup script to get updates
./setup-arsenal.sh
```

### **3. Customize Rules**

You can edit rules after copying:
```bash
# Edit to fit your needs
code .windsurf/rules/nextjs-15-app-router.md

# Add project-specific patterns
# Adjust activation modes
# Add your own examples
```

### **4. Use .gitignore**

Decide if you want to commit `.windsurf/`:

**Commit it (recommended for teams):**
```bash
# Everyone gets same Arsenal setup
git add .windsurf/
git commit -m "Add Arsenal rules and workflows"
```

**Don't commit (personal preference):**
```bash
# Add to .gitignore
echo ".windsurf/" >> .gitignore
```

### **5. Test After Installation**

In Cascade, test that rules work:
```
Hey Cascade, what rules are currently active?

OR

@nextjs-15-app-router
Show me the async params pattern
```

---

## 🔍 Troubleshooting

### **Rules Not Appearing?**

1. **Reload Windsurf** (close and reopen)
2. **Check file location:** Files must be in `.windsurf/rules/` or `.windsurf/workflows/`
3. **Check file extension:** Must be `.md` files
4. **Check Customizations panel:** Click refresh icon

### **Rules Not Activating?**

1. **Check activation mode** in rule's YAML front matter
2. **Manual rules** need @mention (e.g., `@mobile-overlay`)
3. **Glob rules** only activate for matching files
4. **Always On** rules should work everywhere

### **Arsenal Repos Not Found?**

```bash
# Check installation
ls ~/arsenals/

# If empty, install:
curl -sSL https://raw.githubusercontent.com/ChrisTansey007/arsenal-integration-hub/main/scripts/install-all.sh | bash
```

### **Permission Errors (Windows)?**

Run PowerShell as Administrator:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\setup-arsenal.ps1
```

---

## 📖 Example: Complete Next.js 15 Setup

Here's a complete real-world example:

```bash
#!/bin/bash
# Next.js 15 + Arsenal Setup

set -e

echo "🔧 Setting up Arsenal for Next.js 15 project..."

# Create structure
mkdir -p .windsurf/{rules,workflows,memories}

# Copy Next.js rules
cp ~/arsenals/ai-rules-arsenal/windsurf/by-framework/nextjs-15-app-router.md .windsurf/rules/
cp ~/arsenals/ai-rules-arsenal/windsurf/by-framework/mdx-content-management.md .windsurf/rules/

# Copy domain rules
cp ~/arsenals/ai-rules-arsenal/windsurf/by-domain/frontend-ux-patterns.md .windsurf/rules/
cp ~/arsenals/ai-rules-arsenal/windsurf/by-domain/typescript-strict-development.md .windsurf/rules/

# Copy platform rule (if Windows)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    cp ~/arsenals/ai-rules-arsenal/windsurf/platform-specific/windows-powershell-git.md .windsurf/rules/
fi

# Copy workflows
cp ~/arsenals/ai-workflows-arsenal/windsurf/development/code-review-process.md .windsurf/workflows/

# Copy memory
cp ~/arsenals/windsurf-memories-arsenal/frameworks/nextjs-app-router.md .windsurf/memories/

# Summary
echo ""
echo "✅ Arsenal setup complete for Next.js 15!"
echo "   - 4-5 rules installed"
echo "   - 1 workflow installed"
echo "   - 1 memory installed"
echo ""
echo "🚀 Ready to build!"
```

---

## 🎓 Next Steps

After setting up Arsenal:

1. **Test in Cascade:**
   ```
   Hey Cascade, show me the active rules for this project
   ```

2. **Try a workflow:**
   - Open Workflows tab
   - Click on a workflow
   - Follow the steps

3. **Use @mentions for manual rules:**
   ```
   @mobile-overlay
   I need to create a mobile drawer menu
   ```

4. **Read the docs:**
   - [Arsenal Ecosystem Analysis](../ARSENAL-ECOSYSTEM-ANALYSIS.md)
   - [Integration Examples](../examples/)
   - [Arsenal Integration Hub](../README.md)

---

## 🔗 Additional Resources

- **Installation Guide:** [Install Arsenal Repos](https://github.com/ChrisTansey007/arsenal-integration-hub)
- **Examples:** [Complete Integration Examples](../examples/)
- **Rules Catalog:** [ai-rules-arsenal](https://github.com/ChrisTansey007/ai-rules-arsenal)
- **Workflows:** [ai-workflows-arsenal](https://github.com/ChrisTansey007/ai-workflows-arsenal)
- **Prompts:** [prompt-arsenal](https://github.com/ChrisTansey007/prompt-arsenal)

---

## 💬 Need Help?

- **Issues:** [GitHub Issues](https://github.com/ChrisTansey007/arsenal-integration-hub/issues)
- **Discussions:** [GitHub Discussions](https://github.com/ChrisTansey007/arsenal-integration-hub/discussions)

---

## 🎉 You're Ready!

You now know how to add any Arsenal content to any project. Start small, experiment, and expand as you discover what helps you most!

**Happy coding with AI superpowers!** 🚀

---

**Last Updated:** 2025-11-05  
**Maintained by:** Arsenal Ecosystem
