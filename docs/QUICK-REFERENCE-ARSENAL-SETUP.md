# ⚡ Arsenal Setup Quick Reference

**One-page cheatsheet for adding Arsenal rules & workflows to your project**

---

## 🚀 Fastest Setup (3 Commands)

```bash
# 1. Create structure
mkdir -p .windsurf/{rules,workflows,memories}

# 2. Copy what you need (example: Next.js)
cp ~/arsenals/ai-rules-arsenal/windsurf/by-framework/nextjs-15-app-router.md .windsurf/rules/
cp ~/arsenals/ai-rules-arsenal/windsurf/by-domain/typescript-strict-development.md .windsurf/rules/

# 3. Reload Windsurf (close & reopen)
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force -Path .windsurf\rules,.windsurf\workflows,.windsurf\memories
Copy-Item "$env:USERPROFILE\arsenals\ai-rules-arsenal\windsurf\by-framework\nextjs-15-app-router.md" .windsurf\rules\
```

---

## 📋 Popular Setups

### **Next.js 15 Project**
```bash
# Rules
cp ~/arsenals/ai-rules-arsenal/windsurf/by-framework/nextjs-15-app-router.md .windsurf/rules/
cp ~/arsenals/ai-rules-arsenal/windsurf/by-framework/mdx-content-management.md .windsurf/rules/
cp ~/arsenals/ai-rules-arsenal/windsurf/by-domain/frontend-ux-patterns.md .windsurf/rules/
cp ~/arsenals/ai-rules-arsenal/windsurf/by-domain/typescript-strict-development.md .windsurf/rules/

# Memory
cp ~/arsenals/windsurf-memories-arsenal/frameworks/nextjs-app-router.md .windsurf/memories/
```

### **Python/FastAPI Project**
```bash
# Rules
cp ~/arsenals/ai-rules-arsenal/windsurf/by-framework/fastapi-patterns.md .windsurf/rules/
cp ~/arsenals/ai-rules-arsenal/windsurf/by-domain/complete-problem-solving.md .windsurf/rules/

# Memory
cp ~/arsenals/windsurf-memories-arsenal/frameworks/fastapi-structure.md .windsurf/memories/
```

### **Arsenal Content Creation**
```bash
# Rules
cp ~/arsenals/ai-rules-arsenal/windsurf/arsenal-meta/rule-writing-standards.md .windsurf/rules/
cp ~/arsenals/ai-rules-arsenal/windsurf/arsenal-meta/integration-example-standards.md .windsurf/rules/
cp ~/arsenals/ai-rules-arsenal/windsurf/arsenal-meta/documentation-update-checklist.md .windsurf/rules/

# Workflow
cp ~/arsenals/ai-workflows-arsenal/windsurf/arsenal-management/integrate-ruleminer-output.md .windsurf/workflows/
```

---

## 📂 Arsenal Content Locations

### **Rules**
```
~/arsenals/ai-rules-arsenal/windsurf/
├── by-framework/        # Next.js, React, FastAPI, etc.
├── by-domain/          # Frontend, TypeScript, Problem-solving
├── platform-specific/  # Windows, macOS, Linux
└── arsenal-meta/       # Arsenal management rules
```

### **Workflows**
```
~/arsenals/ai-workflows-arsenal/windsurf/
├── arsenal-management/ # RuleMiner integration, etc.
└── development/       # Code review, testing, Git
```

### **Memories**
```
~/arsenals/windsurf-memories-arsenal/
└── frameworks/        # Next.js, React, FastAPI, etc.
```

---

## 🎨 Windsurf UI Method

1. **Open Customizations:** Settings → "Rules, Memories & Workflows"
2. **Click "+ Project"** (or "+ Global")
3. **Navigate to:** `arsenals/ai-rules-arsenal/windsurf/[category]/`
4. **Select files** you want
5. **Click "Open"**
6. **Done!** ✅

---

## 💡 Common Commands

### **Check Installation**
```bash
ls ~/arsenals/                    # See installed repos
ls .windsurf/rules/              # See project rules
ls .windsurf/workflows/          # See project workflows
```

### **Update Arsenal Repos**
```bash
cd ~/arsenals
for repo in */; do cd "$repo" && git pull && cd ..; done
```

### **Test Rules Active**
```
Hey Cascade, what rules are currently active?
```

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Rules not appearing | Reload Windsurf (close & reopen) |
| Files not copied | Check path: `~/arsenals/` or `$env:USERPROFILE\arsenals\` |
| Rules not activating | Check activation mode (Always On, Glob, Manual) |
| Permission errors | Run PowerShell as Administrator (Windows) |

---

## 📝 Template Setup Script

```bash
#!/bin/bash
# Customize for your project

mkdir -p .windsurf/{rules,workflows,memories}

# Add your rules here:
cp ~/arsenals/ai-rules-arsenal/windsurf/by-framework/YOUR-RULE.md .windsurf/rules/

# Count and report
echo "✅ Installed: $(ls .windsurf/rules/*.md | wc -l) rules"
```

---

## 🎯 Best Practices

✅ **Start small** - 2-3 rules max  
✅ **Project-specific** - Use `.windsurf/` in project  
✅ **Commit to Git** - Share with team  
✅ **Update regularly** - Pull Arsenal repos monthly  
✅ **Test after install** - Ask Cascade what's active  

---

## 🔗 Full Documentation

**Detailed guide:** [SETUP-ARSENAL-RULES-WORKFLOWS.md](./SETUP-ARSENAL-RULES-WORKFLOWS.md)

**Arsenal repos:** [Arsenal Integration Hub](https://github.com/ChrisTansey007/arsenal-integration-hub)

---

**Last Updated:** 2025-11-05  
**Version:** 1.0.0
