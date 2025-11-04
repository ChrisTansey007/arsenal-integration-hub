# 🚀 React Vite Setup - Complete Example

**Full workflow demonstration: Set up React/Vite project with automated ESM fixes and modern UI transformation.**

---

## 🎯 Scenario

You're starting a new React project with Vite. You want:
1. ✅ **Automated setup** - No manual config file tweaking
2. ✅ **ESM consistency** - No "module is not defined" errors
3. ✅ **Modern UI** - Professional, accessible design from day one

**Time to complete:** 30-45 minutes  
**Time saved:** 2-3 hours vs manual setup

---

## 📦 Arsenal Items Used

### 1. 🔧 Script: React Vite Setup
**Location:** [ai-scripts-arsenal/scripts/frontend/react-vite-setup](https://github.com/ChrisTansey007/ai-scripts-arsenal/tree/main/scripts/frontend/react-vite-setup)

**What it does:**
- Validates environment (Node.js, npm)
- Installs all dependencies
- Automatically fixes ESM configuration
- Creates backups before changes
- Verifies setup correctness

### 2. ⚙️ Rule: Vite ESM Consistency  
**Location:** [ai-rules-arsenal/windsurf/by-framework/vite-esm-modules.md](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/by-framework/vite-esm-modules.md)

**What it enforces:**
- ES module syntax in all config files
- Prevents CommonJS/ESM mixing
- Provides troubleshooting for common errors

### 3. 💭 Prompt: Modernize React UI
**Location:** [prompt-arsenal/development/ui/modernize-react-ui.md](https://github.com/ChrisTansey007/prompt-arsenal/blob/main/development/ui/modernize-react-ui.md)

**What it provides:**
- 6-phase UI transformation guide
- Modern design patterns (gradients, icons, animations)
- Accessibility best practices
- Before/after code examples

---

## 🎬 Complete Workflow

### Phase 1: Project Creation (5 min)

**Step 1: Create new Vite project**

```bash
# Create project with React template
npm create vite@latest my-modern-app -- --template react

# Navigate to project
cd my-modern-app
```

**Step 2: Download setup script**

```bash
# Create scripts directory
mkdir -p scripts

# Download setup script (choose one)
# PowerShell version
curl -o scripts/setup-react-vite.ps1 https://raw.githubusercontent.com/ChrisTansey007/ai-scripts-arsenal/main/scripts/frontend/react-vite-setup/setup-react-vite.ps1

# Bash version
curl -o scripts/setup-react-vite.sh https://raw.githubusercontent.com/ChrisTansey007/ai-scripts-arsenal/main/scripts/frontend/react-vite-setup/setup-react-vite.sh
chmod +x scripts/setup-react-vite.sh
```

---

### Phase 2: Automated Setup (10 min)

**Step 3: Run setup script**

```bash
# Preview changes first (dry run)
./scripts/setup-react-vite.sh --project-path . --dry-run

# Run full setup
./scripts/setup-react-vite.sh --project-path .
```

**Expected output:**
```
========================================
  React Vite Setup - Starting
========================================

========================================
  Step 1/6: Validate Environment
========================================
✓ Project path exists: /home/user/my-modern-app
✓ Changed to project directory
✓ Node.js version: v20.10.0
✓ npm version: 10.2.3
✓ Found package.json

========================================
  Step 2/6: Install Root Dependencies
========================================
✓ Root dependencies installed successfully

========================================
  Step 3/6: Detect and Fix ESM Configuration
========================================
✓ package.json has "type": "module"
⚠ Found CommonJS syntax in postcss.config.js
✓ Converted postcss.config.js to ESM syntax
⚠ Found CommonJS syntax in tailwind.config.js
✓ Converted tailwind.config.js to ESM syntax
✓ Fixed 2 config file(s)

========================================
  Step 6/6: Verification
========================================
✓ All config files passed syntax verification

========================================
  Setup Complete!
========================================
✓ All done! 🚀
```

**Step 4: Verify setup**

```bash
# Start dev server
npm run dev

# Should start without errors
# Visit http://localhost:5173
```

---

### Phase 3: UI Modernization (25 min)

**Step 5: Install UI dependencies**

```bash
# Install Lucide icons
npm install lucide-react

# Install utility libraries (optional)
npm install clsx tailwind-merge
```

**Step 6: Configure Tailwind**

Update `tailwind.config.js`:

```javascript
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in',
        'slide-up': 'slideUp 0.5s ease-out',
        'scale-in': 'scaleIn 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        scaleIn: {
          '0%': { opacity: '0', transform: 'scale(0.95)' },
          '100%': { opacity: '1', transform: 'scale(1)' },
        },
      },
    },
  },
  plugins: [],
}
```

**Step 7: Add global styles**

Update `src/index.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer utilities {
  /* Gradient backgrounds */
  .bg-gradient-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  }
  
  /* Gradient text */
  .text-gradient {
    @apply bg-clip-text text-transparent;
    background-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  }
  
  /* Modern cards */
  .card-modern {
    @apply rounded-3xl bg-white shadow-lg hover:shadow-xl 
           transition-all duration-300 border border-gray-100;
  }
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

**Step 8: Transform components**

**Before** (`src/App.jsx`):
```jsx
function App() {
  return (
    <div>
      <h1>Welcome</h1>
      <button>Get Started</button>
    </div>
  )
}
```

**After** (`src/App.jsx`):
```jsx
import { Sparkles, ArrowRight } from 'lucide-react'

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 via-white to-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center space-y-8 animate-fade-in">
          {/* Badge */}
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-white rounded-full shadow-lg">
            <Sparkles className="w-4 h-4 text-purple-600" aria-hidden="true" />
            <span className="text-sm font-medium text-gray-900">Modern Design</span>
          </div>
          
          {/* Title */}
          <h1 className="text-6xl md:text-7xl font-bold tracking-tight">
            <span className="text-gradient">Welcome to</span>
            <br />
            <span className="text-gray-900">Your App</span>
          </h1>
          
          {/* Description */}
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Beautiful, modern UI built with React and Tailwind CSS
          </p>
          
          {/* CTA Button */}
          <button 
            className="
              inline-flex items-center gap-2 px-8 py-4
              bg-gradient-primary text-white rounded-xl
              hover:shadow-xl hover:scale-105
              active:scale-95
              transition-all duration-200
              font-medium text-lg
              min-h-[56px]
            "
            aria-label="Get started with the app"
          >
            <span>Get Started</span>
            <ArrowRight className="w-5 h-5" aria-hidden="true" />
          </button>
        </div>
      </div>
    </div>
  )
}

export default App
```

**Step 9: Test accessibility**

```bash
# Install axe-core for accessibility testing
npm install -D @axe-core/react

# Add to src/main.tsx (development only)
if (import.meta.env.DEV) {
  import('@axe-core/react').then((axe) => {
    axe.default(React, ReactDOM, 1000)
  })
}
```

---

### Phase 4: Verification (5 min)

**Step 10: Final checks**

```bash
# 1. Build succeeds
npm run build

# 2. Preview works
npm run preview

# 3. No console errors
# Open browser DevTools and check console

# 4. Lighthouse audit
# Chrome DevTools -> Lighthouse -> Run audit
# Target: Accessibility score > 90
```

**Checklist:**
- [ ] Dev server starts without errors
- [ ] Build completes successfully
- [ ] All pages load correctly
- [ ] No ESM/CommonJS errors in console
- [ ] Buttons have proper hover/active states
- [ ] Focus states visible (tab through page)
- [ ] Touch targets >= 48x48px
- [ ] Responsive on mobile (375px width)
- [ ] Lighthouse accessibility score > 90

---

## 📊 Results

### Time Comparison

**Manual Setup:**
- Create project: 5 min
- Install dependencies: 5 min
- Fix ESM issues (trial & error): 30-60 min
- Configure Tailwind: 10 min
- Add styles: 20 min
- Transform components: 60-90 min
- Fix accessibility: 30 min
**Total: 3-4 hours**

**With Arsenal:**
- Create project: 5 min
- Run automated setup: 10 min
- Install UI dependencies: 2 min
- Add global styles: 5 min
- Transform components: 15 min
- Verify: 5 min
**Total: 42 minutes**

**Time Saved: 2-3 hours** ⚡

### Quality Improvements

**Before (Manual):**
- ❌ ESM errors during development
- ❌ Inconsistent styling
- ❌ Basic, boring UI
- ❌ Poor accessibility
- ❌ No animations

**After (With Arsenal):**
- ✅ No build/runtime errors
- ✅ Consistent modern design
- ✅ Professional, polished UI
- ✅ WCAG 2.1 AA compliant
- ✅ Smooth animations

---

## 🎓 What You Learned

### 1. Automated Setup Benefits
- Scripts eliminate manual config errors
- Dry-run mode previews changes safely
- Automatic backups enable easy rollback
- Validation catches issues early

### 2. ESM Consistency Importance
- `"type": "module"` requires ES syntax everywhere
- `module.exports` causes runtime errors in Vite
- All config files must use `export default`
- Renaming to `.cjs` is alternative solution

### 3. Modern UI Patterns
- Gradients add visual interest
- Icons improve usability
- Animations provide feedback
- Cards create visual hierarchy
- Proper spacing improves readability

### 4. Accessibility Essentials
- Keyboard navigation is critical
- Focus states must be visible
- Touch targets need adequate size
- Color contrast matters
- Screen readers need proper ARIA

---

## 🔗 Next Steps

### Extend the Example

**Add more features:**

```bash
# Add routing
npm install react-router-dom

# Add state management
npm install zustand
# or
npm install @tanstack/react-query

# Add forms
npm install react-hook-form zod

# Add testing
npm install -D vitest @testing-library/react @testing-library/jest-dom
```

### Apply to Existing Projects

**Use the setup script on existing projects:**

```bash
# Navigate to existing project
cd my-existing-project

# Run script with skip-install if deps already installed
./scripts/setup-react-vite.sh --project-path . --skip-install
```

### Create Custom Variants

**Modify for your needs:**

1. Copy setup script
2. Add project-specific checks
3. Include additional dependencies
4. Customize ESM fixes
5. Add company branding

---

## 🚨 Troubleshooting

### Issue: "module is not defined"

**Cause:** Config file still using CommonJS syntax

**Solution:**
```bash
# Check package.json has "type": "module"
cat package.json | grep '"type"'

# Re-run setup script
./scripts/setup-react-vite.sh --project-path .

# Or manually convert
sed -i 's/module\.exports =/export default/g' vite.config.js
```

### Issue: Gradients not showing

**Cause:** Tailwind not configured properly

**Solution:**
```bash
# Verify Tailwind config uses ESM
cat tailwind.config.js

# Should start with: export default {

# Rebuild
npm run dev
```

### Issue: Icons not displaying

**Cause:** lucide-react not installed

**Solution:**
```bash
# Install icons
npm install lucide-react

# Import in component
import { Icon Name } from 'lucide-react'
```

### Issue: Build fails after changes

**Cause:** Syntax error in updated files

**Solution:**
```bash
# Restore from backup
cp .setup-backups-*/filename.js.bak filename.js

# Or check syntax
node --check filename.js

# Fix errors and retry
```

---

## 🔗 Related Arsenal Items

### **⚙️ Rules**
- [Vite ESM Modules](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/by-framework/vite-esm-modules.md) ⭐ Core - ESM configuration standards
- [Next.js App Router](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/by-framework/nextjs-app-router.md) - React patterns and conventions
- [Prompt Quality Standards](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/prompt-design/prompt-quality-standards.md) - Quality framework

### **📝 Prompts**
- [Modernize React UI](https://github.com/ChrisTansey007/prompt-arsenal/blob/main/development/ui/modernize-react-ui.md) ⭐ Core - UI transformation guide
- [Structured Document Architect](https://github.com/ChrisTansey007/prompt-arsenal/blob/main/development/documentation/structured-document-architect.md) - Documentation creation
- [Self-Score Output](https://github.com/ChrisTansey007/prompt-arsenal/blob/main/quality-assurance/self-score-output.md) - Quality validation

### **🔄 Workflows**
- [Run Tests and Fix](https://github.com/ChrisTansey007/ai-workflows-arsenal/blob/main/windsurf/development/run-tests-and-fix.md) - Automated testing
- [Code Review Assistant](https://github.com/ChrisTansey007/ai-workflows-arsenal/blob/main/windsurf/development/code-review-assistant.md) - Pre-commit review

### **🤖 Scripts**
- [React Vite Setup Script](https://github.com/ChrisTansey007/ai-scripts-arsenal/tree/main/scripts/frontend/react-vite-setup) ⭐ Core - Automated setup

### **💭 Memories**
- [React Patterns Library](https://github.com/ChrisTansey007/windsurf-memories-arsenal) - Component patterns
- [Frontend Best Practices](https://github.com/ChrisTansey007/windsurf-memories-arsenal) - Development standards

### **🔗 Integration Examples**
- [Full-Stack Next.js App](../fullstack-nextjs-app/) - Complete application setup
- [Solo Developer](../solo-developer/) - Minimal configuration
- [Repository Organization](../repo-organization/) - File structure

### **🛠️ New Tools**
- [Arsenal CLI](https://github.com/ChrisTansey007/arsenal-cli) - Manage React projects via CLI
- [Arsenal MCP Server](https://github.com/ChrisTansey007/arsenal-mcp-server) - Access React patterns via MCP

### **📚 External Resources**
- [Vite Documentation](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Lucide Icons](https://lucide.dev/)
- [React Documentation](https://react.dev/)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

## ✅ Success Criteria

**Your setup is successful if:**

- [ ] Dev server starts with: `npm run dev`
- [ ] Build completes with: `npm run build`
- [ ] No console errors in browser
- [ ] All config files use ES module syntax
- [ ] UI looks modern with gradients/icons
- [ ] Buttons have hover/active states
- [ ] Tab navigation works throughout
- [ ] Focus states are visible
- [ ] Touch targets >= 48x48px
- [ ] Responsive on mobile (375px)
- [ ] Lighthouse accessibility > 90
- [ ] Tests pass (if added)

---

**Result: Professional React/Vite project ready for development in under 45 minutes!** 🎉

---

## 💡 Pro Tips

1. **Always run dry-run first** - Preview changes before applying
2. **Commit before running scripts** - Easy rollback if needed
3. **Use the rule in Windsurf** - Add to `.windsurf/rules/` for AI guidance
4. **Save the prompt** - Reference during UI work
5. **Test accessibility early** - Easier to fix during development
6. **Keep backups** - Don't delete until verified working
7. **Document customizations** - Help future developers

---

**Questions or issues? Open an issue in the respective Arsenal repository!**
