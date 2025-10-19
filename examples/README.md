# 🔗 Arsenal Integration Hub - Examples

**Complete setup examples showing how to use all Arsenal tools together**

---

## 📚 Available Examples

### ✅ 1. [Solo Developer](./solo-developer/)
**Best for:** Individual developers, side projects, personal work

**What it includes:**
- Next.js App Router setup
- Basic workflows (code review, testing)
- Minimal memory configuration
- Single-developer optimizations

**Arsenal Items Used:**
- 1 Memory (Next.js App Router)
- 1 Rule (Next.js App Router)
- 3 Workflows (Code Review, Run Tests, Commit & PR)

**Time to set up:** 5 minutes

---

### ✅ 2. [Team Setup](./team-setup/)
**Best for:** Small to medium teams, collaborative projects

**What it includes:**
- Code review standards
- Git workflow conventions
- Team onboarding guide
- Shared configurations

**Arsenal Items Used:**
- 1 Memory (Code Review Standards)
- Multiple Workflows (Code Review, Address PR Comments, Commit & PR)
- Team collaboration patterns

**Time to set up:** 10 minutes

---

### ✅ 3. [Full-Stack Next.js App](./fullstack-nextjs-app/)
**Best for:** Complete web applications with frontend + backend

**What it includes:**
- Next.js 14 App Router frontend
- FastAPI Python backend
- PostgreSQL database
- Complete testing setup
- Deployment configuration

**Arsenal Items Used:**
- 2 Memories (Next.js, FastAPI)
- 2 Rules (Next.js, FastAPI)
- 5+ Workflows (Testing, Security, Code Review, etc.)

**Time to set up:** 15 minutes

---

### ✅ 4. [API Service](./api-service/)
**Best for:** Standalone API services, microservices

**What it includes:**
- FastAPI backend
- PostgreSQL database
- API documentation
- Security scanning
- Testing automation

**Arsenal Items Used:**
- 1 Memory (FastAPI)
- 1 Rule (FastAPI)
- 4 Workflows (Security Scan, Run Tests, Code Review, Commit & PR)

**Time to set up:** 10 minutes

---

### ✅ 5. [React Native App](./react-native-app/)
**Best for:** Mobile applications, cross-platform development

**What it includes:**
- React Native + Expo setup
- Navigation configuration
- State management
- Testing setup
- Deployment guides

**Arsenal Items Used:**
- Mobile development memories (coming soon)
- React workflows
- Mobile-specific patterns

**Time to set up:** 15 minutes

---

## 🎯 Quick Comparison

| Example | Complexity | Arsenal Items | Time | Best For |
|---------|-----------|---------------|------|----------|
| **Solo Developer** | ⭐ Simple | 5 items | 5 min | Personal projects |
| **Team Setup** | ⭐⭐ Moderate | 4 items | 10 min | Team collaboration |
| **Full-Stack App** | ⭐⭐⭐ Complex | 9+ items | 15 min | Complete web apps |
| **API Service** | ⭐⭐ Moderate | 6 items | 10 min | Backend services |
| **React Native** | ⭐⭐ Moderate | 5 items | 15 min | Mobile apps |

---

## 🚀 How to Use These Examples

### Step 1: Install Arsenal Repos

```bash
# Option A: Use our installation script
curl -sSL https://raw.githubusercontent.com/ChrisTansey007/arsenal-integration-hub/main/scripts/install-all.sh | bash

# Option B: Manual installation
git clone https://github.com/ChrisTansey007/windsurf-memories-arsenal.git ~/arsenals/windsurf-memories-arsenal
git clone https://github.com/ChrisTansey007/ai-rules-arsenal.git ~/arsenals/ai-rules-arsenal
git clone https://github.com/ChrisTansey007/ai-workflows-arsenal.git ~/arsenals/ai-workflows-arsenal
git clone https://github.com/ChrisTansey007/prompt-arsenal.git ~/arsenals/prompt-arsenal
git clone https://github.com/ChrisTansey007/ai-scripts-arsenal.git ~/arsenals/ai-scripts-arsenal
```

### Step 2: Choose an Example

Browse the examples above and choose the one that matches your project type.

### Step 3: Follow the Setup Guide

Each example has a detailed README with:
- ✅ Prerequisites
- ✅ Step-by-step setup
- ✅ Arsenal items to copy
- ✅ Verification steps
- ✅ Next steps

### Step 4: Customize

Copy the Arsenal items to your project and customize them to match your specific needs.

---

## 📖 Example Structure

Each example follows this structure:

```
example-name/
├── README.md           # Complete setup guide
├── .windsurf/         # Example Windsurf configuration
│   ├── memories/      # Memory files to use
│   ├── rules/         # Rule files to use
│   └── workflows/     # Workflow files to use
└── setup-commands.sh  # Quick setup script
```

---

## 🔗 Arsenal Ecosystem

### What Each Repository Does

**💭 [windsurf-memories-arsenal](https://github.com/ChrisTansey007/windsurf-memories-arsenal)**  
What Cascade remembers - Project context, tech stack, conventions

**⚙️ [ai-rules-arsenal](https://github.com/ChrisTansey007/ai-rules-arsenal)**  
How Cascade behaves - Framework-specific development rules

**🔄 [ai-workflows-arsenal](https://github.com/ChrisTansey007/ai-workflows-arsenal)**  
What Cascade does - Multi-step automation workflows

**📝 [prompt-arsenal](https://github.com/ChrisTansey007/prompt-arsenal)**  
What you ask - Reusable prompts and agent configurations

**🤖 [ai-scripts-arsenal](https://github.com/ChrisTansey007/ai-scripts-arsenal)**  
How to automate - Setup and management scripts

---

## 💡 Tips for Success

### 1. Start Small
Begin with the **Solo Developer** example and add more Arsenal items as needed.

### 2. Mix and Match
Don't feel limited to one example. Take memories from one, rules from another, and workflows from a third.

### 3. Customize
Arsenal items are templates. Adjust them to match your team's conventions and preferences.

### 4. Keep Updated
Arsenal repositories are actively maintained. Pull updates regularly:

```bash
cd ~/arsenals
for repo in */; do
  cd "$repo" && git pull && cd ..
done
```

### 5. Contribute Back
Found a useful pattern? Contribute it back to help others!

---

## ❓ FAQ

### Which example should I start with?

- **Just me coding?** → Solo Developer
- **Working with a team?** → Team Setup
- **Building a web app?** → Full-Stack Next.js App
- **Building an API?** → API Service
- **Building mobile?** → React Native App

### Can I combine examples?

Absolutely! Mix memories from one example with workflows from another.

### How do I update Arsenal items?

```bash
cd ~/arsenals/[repo-name]
git pull
# Copy updated files to your project
```

### What if I need different frameworks?

Check the Arsenal repositories for other framework support, or contribute your own!

---

## 🆘 Need Help?

- **Issues:** [Open an issue](https://github.com/ChrisTansey007/arsenal-integration-hub/issues)
- **Discussions:** [GitHub Discussions](https://github.com/ChrisTansey007/arsenal-integration-hub/discussions)
- **Website:** [chriscreateswithai.com](https://chriscreateswithai.com)

---

## 🎉 Ready to Start?

1. Pick an example above
2. Click the link to see the full setup guide
3. Follow the steps
4. Start coding with AI superpowers! 🚀

---

[← Back to Integration Hub](../README.md)
