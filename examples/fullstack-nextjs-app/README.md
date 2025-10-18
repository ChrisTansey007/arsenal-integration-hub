# Full-Stack Next.js + FastAPI Integration Example

**Complete Arsenal integration for a modern full-stack application**

---

## 🎯 What You'll Build

A complete SaaS application with:
- **Frontend:** Next.js 14 App Router + TypeScript + Tailwind
- **Backend:** FastAPI + PostgreSQL + Prisma
- **Auth:** JWT authentication
- **Testing:** Jest + Pytest
- **Deployment:** Docker + GitHub Actions

**With full Arsenal integration for maximum productivity!**

---

## 📊 Arsenal Components Used

### Memories (4 files)
- `nextjs-app-router-memory.md` - Frontend context
- `fastapi-memory.md` - Backend context
- `code-review-standards-memory.md` - Team standards
- `project-architecture-memory.md` - System design

### Rules (3 files)
- `nextjs-app-router.md` - Frontend development rules
- `fastapi-dev.md` - Backend development rules
- `typescript-strict.md` - TypeScript conventions

### Workflows (6 files)
- `address-pr-comments.md` - PR feedback automation
- `run-tests-and-fix.md` - Test automation
- `code-review-assistant.md` - Pre-review checks
- `commit-and-pr.md` - Standardized commits
- `security-scan.md` - Security checks
- `deploy-staging.md` - Deployment automation

### Prompts (from prompt-arsenal)
- Use as needed for specific tasks
- Browse [prompt-arsenal](https://github.com/ChrisTansey007/prompt-arsenal)

### Scripts
- `setup-project.sh` - Initial setup
- `dev.sh` - Start development servers
- `test-all.sh` - Run all tests
- `deploy.sh` - Deploy to production

---

## 🚀 Quick Start

### Prerequisites

- **Windsurf IDE** installed
- **Node.js 18+** and **Python 3.10+**
- **PostgreSQL** database
- **Git** for version control

### Step 1: Clone and Setup

```bash
# Clone this example
git clone https://github.com/ChrisTansey007/arsenal-integration-hub.git
cd arsenal-integration-hub/examples/fullstack-nextjs-app

# Run setup script
./setup.sh

# This will:
# - Clone all Arsenal repos
# - Set up project structure
# - Copy Arsenal files
# - Install dependencies
# - Initialize database
```

### Step 2: Configure Arsenal

```bash
# Project structure after setup:
my-saas-app/
├── .windsurf/
│   ├── memories/           # ✅ Pre-configured
│   ├── rules/              # ✅ Pre-configured
│   └── workflows/          # ✅ Pre-configured
├── frontend/               # Next.js app
├── backend/                # FastAPI service
└── scripts/                # Automation scripts
```

### Step 3: Start Development

```bash
# Start both servers
./scripts/dev.sh

# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Step 4: Open in Windsurf

```bash
# Open project in Windsurf
windsurf my-saas-app

# Cascade will automatically load:
# ✅ All Memories
# ✅ All Rules
# ✅ All Workflows
```

---

## 📁 Project Structure

```
my-saas-app/
│
├── .windsurf/                          # Arsenal configuration
│   ├── memories/
│   │   ├── nextjs-app-router-memory.md
│   │   ├── fastapi-memory.md
│   │   ├── code-review-standards-memory.md
│   │   └── project-architecture-memory.md
│   │
│   ├── rules/
│   │   ├── nextjs-app-router.md
│   │   ├── fastapi-dev.md
│   │   └── typescript-strict.md
│   │
│   └── workflows/
│       ├── address-pr-comments.md
│       ├── run-tests-and-fix.md
│       ├── code-review-assistant.md
│       ├── commit-and-pr.md
│       ├── security-scan.md
│       └── deploy-staging.md
│
├── frontend/                           # Next.js application
│   ├── app/
│   │   ├── (auth)/
│   │   │   ├── login/
│   │   │   └── signup/
│   │   ├── (dashboard)/
│   │   │   ├── dashboard/
│   │   │   └── profile/
│   │   ├── api/
│   │   └── layout.tsx
│   ├── components/
│   ├── lib/
│   ├── package.json
│   └── tsconfig.json
│
├── backend/                            # FastAPI service
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   ├── auth.py
│   │   │       │   └── users.py
│   │   │       └── __init__.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── db/
│   │   │   ├── models/
│   │   │   └── schemas/
│   │   └── main.py
│   ├── tests/
│   ├── requirements.txt
│   └── pyproject.toml
│
├── scripts/                            # Automation
│   ├── setup.sh
│   ├── dev.sh
│   ├── test-all.sh
│   └── deploy.sh
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
│
├── docker-compose.yml
└── README.md
```

---

## 💡 How Arsenal Integration Works

### Scenario 1: Building a New Feature

**Task:** Add user profile management

**Step 1: Ask Cascade**
```
"Create a user profile management system with:
- Profile page with editable fields
- API endpoint to update profile
- Image upload for avatar
- Form validation
- Error handling"
```

**What Happens:**
1. **Memory provides context:**
   - Cascade knows the project structure
   - Understands Next.js App Router patterns
   - Knows FastAPI conventions

2. **Rules guide implementation:**
   - Uses Server Components where possible
   - Implements proper TypeScript types
   - Follows API design patterns

3. **Cascade generates code:**
   - Frontend: `app/(dashboard)/profile/page.tsx`
   - Backend: `app/api/v1/endpoints/profile.py`
   - Tests: Frontend and backend test files
   - Types: Shared TypeScript/Pydantic schemas

**Step 2: Run Tests**
```bash
# Or use workflow
/run-tests-and-fix
```

**What Happens:**
- Runs frontend tests (Jest)
- Runs backend tests (Pytest)
- If failures, automatically fixes
- Shows you what was fixed

**Step 3: Review Code**
```bash
/code-review-assistant
```

**What Happens:**
- Checks code quality
- Looks for security issues
- Verifies best practices
- Provides suggestions

**Step 4: Create PR**
```bash
/commit-and-pr
```

**What Happens:**
- Generates conventional commit message
- Creates comprehensive PR description
- Links related issues
- Adds labels
- Requests reviewers

**Result:** Complete feature implemented in minutes, not hours! ✨

---

### Scenario 2: Handling PR Feedback

**PR Comments:**
```
Reviewer: "Can you add loading states to the profile page?"
Reviewer: "The avatar upload needs error handling"
Reviewer: "Add TypeScript types for the API response"
```

**Solution:**
```bash
/address-pr-comments
```

**What Happens:**
1. Cascade reads PR comments
2. Understands what needs to change
3. Makes the modifications
4. Adds tests for new logic
5. Updates documentation
6. Creates commit with changes

**Result:** PR feedback addressed automatically! 🎉

---

### Scenario 3: Security Audit

**Before Deployment:**
```bash
/security-scan
```

**What Happens:**
1. **Dependency scan:**
   - Checks npm packages
   - Checks Python packages
   - Reports vulnerabilities

2. **Code analysis:**
   - SQL injection risks
   - XSS vulnerabilities
   - Hardcoded secrets
   - Auth issues

3. **Configuration check:**
   - CORS settings
   - Security headers
   - Environment variables

4. **Report generated:**
   - Critical issues (fix now)
   - Warnings (fix soon)
   - Suggestions (nice to have)

**Result:** Ship secure code with confidence! 🔒

---

## 🎓 Development Workflow

### Daily Development Flow

```bash
# 1. Start your day
./scripts/dev.sh

# 2. Open Windsurf
windsurf .

# 3. Check tasks
# Read GitHub issues or your TODO

# 4. Request feature in Cascade
"Build [feature description]"

# 5. Cascade generates code
# Using Memories for context
# Following Rules for style
# Creating tests automatically

# 6. Review and test
/run-tests-and-fix
/code-review-assistant

# 7. Commit and push
/commit-and-pr

# 8. Deploy to staging
/deploy-staging

# 9. Repeat!
```

### Before PR Workflow

```bash
# Complete pre-PR checklist
/code-review-assistant      # Review code
/run-tests-and-fix          # Ensure tests pass
/security-scan              # Check security
/commit-and-pr              # Create PR
```

### After PR Feedback

```bash
# Address feedback automatically
/address-pr-comments

# Re-run checks
/run-tests-and-fix
/code-review-assistant

# Update PR
git push
```

---

## 📚 Example Conversations with Cascade

### Example 1: Building Authentication

**You:**
```
"Implement JWT authentication with:
- Login endpoint
- Signup endpoint  
- Protected routes
- Token refresh
- Password hashing with bcrypt"
```

**Cascade (with Memories + Rules):**
- Creates `backend/app/api/v1/endpoints/auth.py`
- Implements JWT token generation
- Adds bcrypt password hashing
- Creates `frontend/app/(auth)/login/page.tsx`
- Implements protected route middleware
- Adds proper TypeScript types
- Creates tests for all endpoints
- Updates documentation

**Why it works:**
- **Memory** tells Cascade the project structure
- **Rules** ensure it follows FastAPI + Next.js patterns
- **Result:** Production-ready auth system

### Example 2: Adding Database Model

**You:**
```
"Add a Blog Post model with:
- Title, content, author
- Published/draft status
- Tags
- Created/updated timestamps
- API endpoints for CRUD"
```

**Cascade:**
- Creates SQLAlchemy model
- Creates Pydantic schemas
- Generates migration
- Implements CRUD endpoints
- Adds authorization checks
- Creates frontend components
- Generates tests
- Updates API documentation

**Why it works:**
- **Memory** provides database patterns
- **Rules** enforce consistent API design
- **Result:** Complete feature stack

### Example 3: Refactoring Code

**You:**
```
"Refactor the user service to use dependency injection
and extract business logic from route handlers"
```

**Cascade:**
- Analyzes current code structure
- Creates service layer
- Implements dependency injection
- Updates route handlers
- Maintains backwards compatibility
- Updates tests
- Documents changes

**Why it works:**
- **Memory** understands architecture
- **Rules** follow best practices
- **Result:** Cleaner, more maintainable code

---

## 🔧 Customization

### Adapting to Your Stack

**If you use different tech:**

1. **Replace Memories:**
```bash
# Instead of Next.js
cp ~/memories-arsenal/project-types/vue-nuxt-memory.md \
   .windsurf/memories/

# Instead of FastAPI
cp ~/memories-arsenal/project-types/django-memory.md \
   .windsurf/memories/
```

2. **Replace Rules:**
```bash
# Match your framework
cp ~/ai-rules-arsenal/windsurf/by-framework/[your-framework].md \
   .windsurf/rules/
```

3. **Keep Workflows:**
```bash
# Workflows are framework-agnostic
# Keep them all!
```

### Team-Specific Configuration

**Add team conventions:**

```markdown
# .windsurf/memories/team-conventions.md

## Our Team Patterns

### Code Review
- All PRs need 2 approvals
- Must pass all CI checks
- Squash commits on merge

### Deployment
- Staging deploys on PR
- Production deploys on release tag
- Rollback if metrics degrade

### Communication
- Daily standup at 10am
- PR reviews within 4 hours
- Slack for urgent issues
```

---

## 🐛 Troubleshooting

### Cascade not using Memories

**Solution:**
```bash
# 1. Check files are in correct location
ls .windsurf/memories/

# 2. Verify file names end in .md
# 3. Restart Windsurf
# 4. Open project folder (not just files)
```

### Rules not being followed

**Solution:**
```bash
# 1. Check rules file format
# 2. Ensure no conflicting rules
# 3. Be specific in requests
#    Instead of: "Build a feature"
#    Say: "Build a feature following our Next.js patterns"
```

### Workflows not found

**Solution:**
```bash
# 1. Verify location
ls .windsurf/workflows/

# 2. Check file names match command
# /run-tests-and-fix → run-tests-and-fix.md

# 3. Restart Cascade
```

---

## 📊 Success Metrics

**After Arsenal integration:**

- **Development Speed:** 3x faster feature development
- **Code Quality:** 40% fewer PR comments
- **Consistency:** 95% adherence to standards
- **Onboarding:** 2 days vs 2 weeks
- **Bug Rate:** 50% reduction
- **Test Coverage:** 85%+ maintained

---

## 🎯 Next Steps

1. **Explore the codebase** - See how everything connects
2. **Try the workflows** - Use `/run-tests-and-fix`, `/code-review-assistant`
3. **Customize for your needs** - Edit Memories and Rules
4. **Share with team** - Commit `.windsurf/` to git
5. **Keep learning** - Check other examples

---

## 📞 Need Help?

- **Documentation:** See [docs](../../docs/)
- **Issues:** Report problems
- **Discussions:** Ask questions
- **Examples:** Browse other [examples](../)

---

## 🙏 Credits

Built using:
- [Windsurf Memories Arsenal](https://github.com/ChrisTansey007/windsurf-memories-arsenal)
- [AI Rules Arsenal](https://github.com/ChrisTansey007/ai-rules-arsenal)
- [AI Workflows Arsenal](https://github.com/ChrisTansey007/ai-workflows-arsenal)
- [Prompt Arsenal](https://github.com/ChrisTansey007/prompt-arsenal)

---

**Happy building! This is how modern development should feel.** 🚀
