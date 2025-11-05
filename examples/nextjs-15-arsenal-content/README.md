# Next.js 15 + Arsenal Content Management

**Complete setup for type-safe MDX content system with Next.js 15 App Router**

[![Next.js](https://img.shields.io/badge/Next.js-15-black)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-blue)](https://www.typescriptlang.org/)
[![MDX](https://img.shields.io/badge/MDX-3.0-orange)](https://mdxjs.com/)

---

## 🎯 What This Is

A comprehensive integration example showing how to build a Next.js 15 application with:

✅ **MDX-based content management** with TypeScript metadata schemas  
✅ **Next.js 15 async params** pattern for dynamic routes  
✅ **Type-safe content loading** with strict validation  
✅ **Accessible typography** with proper contrast  
✅ **Mobile-friendly overlays** using React portals  
✅ **Windows PowerShell** Git command compatibility  

**Perfect for:** Documentation sites, blogs, content platforms, Arsenal-style resource collections

---

## ⚡ Quick Start

### **Step 1: Install Arsenal**

```bash
# Install Arsenal repositories
curl -sSL https://raw.githubusercontent.com/ChrisTansey007/arsenal-integration-hub/main/scripts/install-all.sh | bash
```

### **Step 2: Set Up Project**

```bash
# Create Next.js 15 app
npx create-next-app@latest my-content-site --typescript --tailwind --app

cd my-content-site

# Run setup script
bash ~/arsenals/arsenal-integration-hub/examples/nextjs-15-arsenal-content/setup.sh
```

### **Step 3: Verify Installation**

```bash
# Check rules are installed
ls -la .windsurf/rules/

# Should see:
# - nextjs-15-app-router.md
# - mdx-content-management.md
# - frontend-ux-patterns.md
# - typescript-strict-development.md
# - windows-powershell-git.md (if on Windows)

# Start development
npm run dev
```

---

## 📦 What's Included

### **Arsenal Rules (5)**

1. **Next.js 15 App Router Patterns** ⭐ Core
   - Async params in dynamic routes
   - Detail page template pattern
   - generateMetadata with async params

2. **MDX Content Management** ⭐ Core
   - TypeScript metadata schemas
   - Content creation workflow
   - Directory structure standards
   - Frontmatter validation

3. **Frontend UX Patterns**
   - Typography contrast via CSS variables
   - Mobile overlays with portals
   - Centralized prose styling

4. **TypeScript Strict Development**
   - Metadata-first approach
   - No `any` types
   - Compile-time validation

5. **Windows PowerShell Git** (Windows only)
   - Proper commit message quoting
   - Cross-platform compatibility

### **Example Code**

- TypeScript interfaces for content metadata
- MDX content loader functions
- Dynamic route pages with async params
- Mobile menu with portal rendering
- Global CSS with typography overrides

---

## 🏗️ Architecture

### **Directory Structure**

```
my-content-site/
├── content/
│   └── arsenal/          # MDX content
│       ├── workflows/
│       ├── scripts/
│       ├── rules/
│       └── memories/
├── src/
│   ├── app/
│   │   └── arsenal/
│   │       ├── workflows/
│   │       │   ├── page.tsx        # Index page
│   │       │   └── [slug]/
│   │       │       └── page.tsx    # Detail page
│   │       ├── scripts/
│   │       ├── rules/
│   │       └── memories/
│   └── lib/
│       └── arsenal/
│           ├── types.ts            # All interfaces
│           ├── content.ts          # Loaders
│           └── utils.ts            # Helpers
└── .windsurf/
    └── rules/                      # Arsenal rules
```

### **Key Patterns**

**1. Async Params (Next.js 15)**
```typescript
interface PageProps {
  params: Promise<{ slug: string }>
}

export default async function Page({ params }: PageProps) {
  const { slug } = await params  // ✅ Await first
  // ...
}
```

**2. Type-Safe Content Loading**
```typescript
const resource = await loadArsenalResource<WorkflowMetadata>(
  'workflow',
  slug
)
```

**3. Portal-Based Overlays**
```typescript
{mounted && isOpen && createPortal(
  <div className="fixed inset-0 z-[9999]">
    {/* Overlay content */}
  </div>,
  document.body
)}
```

---

## 📝 Step-by-Step Setup

### **1. Create TypeScript Interfaces**

```typescript
// src/lib/arsenal/types.ts
export interface BaseArsenalMetadata {
  slug: string
  title: string
  description: string
  resourceType: ArsenalResourceType
  status: 'available' | 'coming-soon' | 'beta' | 'deprecated'
  dateAdded: string
  dateUpdated: string
  tags: string[]
  githubRepo: string
  githubPath: string
  githubUrl: string
}

export type ArsenalResourceType = 
  | 'workflow'
  | 'script'
  | 'rule'
  | 'memory'

export interface WorkflowMetadata extends BaseArsenalMetadata {
  resourceType: 'workflow'
  platform: 'windsurf' | 'cursor' | 'vscode' | 'general'
  difficulty: 'beginner' | 'intermediate' | 'advanced'
  estimatedTime: string
}
```

### **2. Create Content Loader**

```typescript
// src/lib/arsenal/content.ts
import { readFile } from 'fs/promises'
import { join } from 'path'
import matter from 'gray-matter'

export async function loadArsenalResource<T extends BaseArsenalMetadata>(
  resourceType: string,
  slug: string
): Promise<{ metadata: T; content: string } | null> {
  try {
    const filePath = join(
      process.cwd(),
      'content',
      'arsenal',
      resourceType + 's',
      `${slug}.mdx`
    )
    
    const fileContent = await readFile(filePath, 'utf-8')
    const { data, content } = matter(fileContent)
    
    if (!data.slug || !data.title || !data.resourceType) {
      throw new Error(`Invalid metadata in ${slug}.mdx`)
    }
    
    return {
      metadata: data as T,
      content
    }
  } catch {
    return null
  }
}
```

### **3. Create MDX Content**

```mdx
---
slug: "git-workflow-automation"
title: "Git Workflow Automation"
description: "Automate your Git workflow with scripts and aliases"
resourceType: "workflow"
status: "available"
dateAdded: "2025-11-05"
dateUpdated: "2025-11-05"
tags: ["git", "automation", "workflow"]
platform: "general"
difficulty: "intermediate"
estimatedTime: "30 minutes"
githubRepo: "username/repo"
githubPath: "content/arsenal/workflows/git-workflow-automation.mdx"
githubUrl: "https://github.com/..."
---

# Git Workflow Automation

Automate your Git workflow...

## Steps

1. Create Git aliases
2. Set up hooks
3. Test automation
```

### **4. Create Index Page**

```typescript
// src/app/arsenal/workflows/page.tsx
import { loadAllArsenalResources } from '@/lib/arsenal/content'
import { WorkflowMetadata } from '@/lib/arsenal/types'
import Link from 'next/link'

export default async function Page() {
  const workflows = await loadAllArsenalResources<WorkflowMetadata>('workflow')
  
  return (
    <div className="container mx-auto px-4 py-12">
      <h1 className="text-4xl font-bold mb-8">Workflows</h1>
      
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {workflows.map((workflow) => (
          <Link
            key={workflow.slug}
            href={`/arsenal/workflows/${workflow.slug}`}
            className="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition"
          >
            <h2 className="text-xl font-semibold mb-2">{workflow.title}</h2>
            <p className="text-gray-600 mb-4">{workflow.description}</p>
            
            <div className="flex flex-wrap gap-2">
              {workflow.tags.map((tag) => (
                <span key={tag} className="text-xs px-2 py-1 bg-blue-100 text-blue-800 rounded">
                  {tag}
                </span>
              ))}
            </div>
          </Link>
        ))}
      </div>
    </div>
  )
}
```

### **5. Create Detail Page**

```typescript
// src/app/arsenal/workflows/[slug]/page.tsx
import { loadArsenalResource } from '@/lib/arsenal/content'
import { WorkflowMetadata } from '@/lib/arsenal/types'
import { notFound } from 'next/navigation'
import { Metadata } from 'next'

interface PageProps {
  params: Promise<{ slug: string }>
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params
  const resource = await loadArsenalResource<WorkflowMetadata>('workflow', slug)
  
  if (!resource) {
    return { title: 'Not Found' }
  }
  
  return {
    title: resource.metadata.title,
    description: resource.metadata.description,
  }
}

export default async function Page({ params }: PageProps) {
  const { slug } = await params
  const resource = await loadArsenalResource<WorkflowMetadata>('workflow', slug)
  
  if (!resource) {
    notFound()
  }
  
  return (
    <div className="min-h-screen">
      {/* Hero section */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-16">
        <div className="container mx-auto px-4">
          <h1 className="text-4xl font-bold mb-4">{resource.metadata.title}</h1>
          <p className="text-xl opacity-90">{resource.metadata.description}</p>
          
          {/* Badges */}
          <div className="flex flex-wrap gap-2 mt-6">
            <span className="px-3 py-1 bg-white/20 rounded-full text-sm">
              {resource.metadata.platform}
            </span>
            <span className="px-3 py-1 bg-white/20 rounded-full text-sm">
              {resource.metadata.difficulty}
            </span>
            <span className="px-3 py-1 bg-white/20 rounded-full text-sm">
              {resource.metadata.estimatedTime}
            </span>
          </div>
        </div>
      </div>
      
      {/* Content section */}
      <div className="container mx-auto px-4 py-12">
        <article className="prose prose-slate prose-lg max-w-none">
          {/* Render MDX content here */}
          <div dangerouslySetInnerHTML={{ __html: resource.content }} />
        </article>
      </div>
    </div>
  )
}
```

### **6. Configure globals.css**

```css
/* src/app/globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .prose {
    --tw-prose-body: theme('colors.slate.700');
    --tw-prose-headings: theme('colors.slate.900');
    --tw-prose-links: theme('colors.blue.600');
    --tw-prose-code: theme('colors.slate.900');
    --tw-prose-pre-bg: theme('colors.slate.900');
    --tw-prose-pre-code: theme('colors.slate.100');
  }
  
  .prose pre {
    @apply bg-slate-900 text-slate-100;
  }
  
  .prose code {
    @apply bg-transparent text-current font-semibold;
  }
}
```

---

## 🎓 Common Workflows

### **Adding New Content Type**

```bash
# 1. Define interface in types.ts
# 2. Create content directory
mkdir -p content/arsenal/new-types

# 3. Create MDX file
touch content/arsenal/new-types/example.mdx

# 4. Create index page
mkdir -p src/app/arsenal/new-types
touch src/app/arsenal/new-types/page.tsx

# 5. Create detail page
mkdir -p src/app/arsenal/new-types/[slug]
touch src/app/arsenal/new-types/[slug]/page.tsx

# 6. Test
npm run dev
```

### **Deploying to Production**

```bash
# Verify type-check passes
npm run type-check

# Build
npm run build

# Test production build locally
npm start

# Deploy (example: Vercel)
vercel deploy --prod
```

---

## 🔗 Related Arsenal Items

### **⚙️ Rules**

- [Next.js 15 App Router](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/by-framework/nextjs-15-app-router.md) ⭐ Core - Async params and page templates
- [MDX Content Management](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/by-framework/mdx-content-management.md) ⭐ Core - Type-safe content system
- [Frontend UX Patterns](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/by-domain/frontend-ux-patterns.md) - Typography and mobile UX
- [TypeScript Strict Development](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/by-domain/typescript-strict-development.md) - Metadata-first approach
- [Windows PowerShell Git](https://github.com/ChrisTansey007/ai-rules-arsenal/blob/main/windsurf/platform-specific/windows-powershell-git.md) - Git commands on Windows

### **📝 Prompts**

- [Structured Document Architect](https://github.com/ChrisTansey007/prompt-arsenal/blob/main/development/documentation/structured-document-architect.md) - Create MDX content
- [Modernize React UI](https://github.com/ChrisTansey007/prompt-arsenal/blob/main/development/ui/modernize-react-ui.md) - UI improvements
- [Self-Score Output](https://github.com/ChrisTansey007/prompt-arsenal/blob/main/quality-assurance/self-score-output.md) - Validate quality

### **🔄 Workflows**

- [Run Tests and Fix](https://github.com/ChrisTansey007/ai-workflows-arsenal) - Automated testing
- [Code Review Assistant](https://github.com/ChrisTansey007/ai-workflows-arsenal) - Review changes

### **💭 Memories**

- [Next.js Patterns Library](https://github.com/ChrisTansey007/windsurf-memories-arsenal) - Common patterns
- [Frontend Best Practices](https://github.com/ChrisTansey007/windsurf-memories-arsenal) - Development standards

### **🔗 Integration Examples**

- [Full-Stack Next.js App](../fullstack-nextjs-app/) - Complete application
- [React Vite Setup](../react-vite-setup/) - Alternative framework
- [Enterprise Quality](../enterprise-quality/) - Production standards

### **🛠️ New Tools**

- [Arsenal CLI](https://github.com/ChrisTansey007/arsenal-cli) - Generate MDX templates and types
- [Arsenal MCP Server](https://github.com/ChrisTansey007/arsenal-mcp-server) - Access patterns via MCP

### **📚 External Resources**

- [Next.js 15 Documentation](https://nextjs.org/docs)
- [MDX Documentation](https://mdxjs.com/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind Typography](https://tailwindcss.com/docs/typography-plugin)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

## 💡 Pro Tips

### **1. Use Code Snippets**

Create VS Code snippets for common patterns:

```json
{
  "Arsenal MDX Frontmatter": {
    "prefix": "arsenal-mdx",
    "body": [
      "---",
      "slug: \"${1:slug}\"",
      "title: \"${2:Title}\"",
      "description: \"${3:Description}\"",
      "resourceType: \"${4|workflow,script,rule,memory|}\"",
      "---"
    ]
  }
}
```

### **2. Automated Validation**

Add to `package.json`:

```json
{
  "scripts": {
    "validate-mdx": "node scripts/validate-mdx.js",
    "precommit": "npm run validate-mdx && npm run type-check"
  }
}
```

### **3. Generate Static Paths**

```typescript
// Optimize for static generation
export async function generateStaticParams() {
  const workflows = await loadAllArsenalResources('workflow')
  return workflows.map((w) => ({ slug: w.slug }))
}
```

### **4. Use Git Hooks**

```bash
# .husky/pre-commit
npm run type-check
npm run validate-mdx
```

---

## 🐛 Troubleshooting

### **Type Errors on `params`**

```
Error: Type 'Promise<{ slug: string }>' is not assignable to type '{ slug: string }'
```

**Solution:** Make sure you're awaiting params:

```typescript
// ❌ WRONG
const { slug } = params

// ✅ CORRECT
const { slug } = await params
```

### **MDX Content Not Loading**

**Check:**
1. File exists in correct directory (`content/arsenal/{type}s/`)
2. Frontmatter is valid YAML
3. All required fields present
4. Slug matches filename

### **Contrast Issues**

**Solution:** Check `globals.css` has prose overrides:

```css
.prose pre {
  @apply bg-slate-900 text-slate-100;
}
```

### **Mobile Menu Not Showing**

**Check:**
1. Portal renders to `document.body`
2. Z-index is high enough (`z-[9999]`)
3. `pointer-events-auto` on content
4. Mounted state check present

---

## 📊 Success Criteria

Your setup is complete when:

✅ `npm run type-check` passes with no errors  
✅ All MDX files have valid frontmatter  
✅ Index pages load all resources  
✅ Detail pages render correctly  
✅ Mobile menu works on all devices  
✅ Contrast meets WCAG AA standards  
✅ Git commands work on Windows PowerShell  
✅ Build succeeds without warnings  

---

## 📄 License

MIT License - Part of the Arsenal Ecosystem

---

**Status:** Production-ready ✅  
**Difficulty:** Intermediate  
**Time to Setup:** 30-60 minutes  
**Maintained by:** Arsenal Ecosystem
