#!/bin/bash

# Next.js 15 + Arsenal Content - Arsenal Setup Script
# Sets up comprehensive MDX content system with Next.js 15 patterns

set -e

echo "🔧 Setting up Next.js 15 + Arsenal Content configuration..."

# Check if we're in a project directory
if [ ! -d "src" ] && [ ! -d "app" ]; then
    echo "❌ This doesn't look like a Next.js project directory."
    echo "   Please run this script from your Next.js project root."
    exit 1
fi

# Create .windsurf directory structure
if [ ! -d ".windsurf" ]; then
    echo "📁 Creating .windsurf directory structure..."
    mkdir -p .windsurf/{memories,rules,workflows}
fi

# Check if Arsenal repos are installed
if [ ! -d "$HOME/arsenals" ]; then
    echo "❌ Arsenal repositories not found. Please run:"
    echo "   curl -sSL https://raw.githubusercontent.com/ChrisTansey007/arsenal-integration-hub/main/scripts/install-all.sh | bash"
    exit 1
fi

ARSENAL_PATH="$HOME/arsenals/ai-rules-arsenal/windsurf"

echo ""
echo "📋 Copying Arsenal rules..."

# Copy Next.js 15 App Router rule
if [ -f "$ARSENAL_PATH/by-framework/nextjs-15-app-router.md" ]; then
    echo "  ✅ Next.js 15 App Router patterns"
    cp "$ARSENAL_PATH/by-framework/nextjs-15-app-router.md" .windsurf/rules/
else
    echo "  ⚠️  Next.js 15 App Router rule not found"
fi

# Copy MDX Content Management rule
if [ -f "$ARSENAL_PATH/by-framework/mdx-content-management.md" ]; then
    echo "  ✅ MDX Content Management system"
    cp "$ARSENAL_PATH/by-framework/mdx-content-management.md" .windsurf/rules/
else
    echo "  ⚠️  MDX Content Management rule not found"
fi

# Copy Frontend UX Patterns rule
if [ -f "$ARSENAL_PATH/by-domain/frontend-ux-patterns.md" ]; then
    echo "  ✅ Frontend UX patterns"
    cp "$ARSENAL_PATH/by-domain/frontend-ux-patterns.md" .windsurf/rules/
else
    echo "  ⚠️  Frontend UX Patterns rule not found"
fi

# Copy TypeScript Strict Development rule
if [ -f "$ARSENAL_PATH/by-domain/typescript-strict-development.md" ]; then
    echo "  ✅ TypeScript Strict Development"
    cp "$ARSENAL_PATH/by-domain/typescript-strict-development.md" .windsurf/rules/
else
    echo "  ⚠️  TypeScript Strict Development rule not found"
fi

# Copy Windows PowerShell Git rule (if on Windows)
if [ -f "$ARSENAL_PATH/platform-specific/windows-powershell-git.md" ]; then
    echo "  ✅ Windows PowerShell Git commands"
    cp "$ARSENAL_PATH/platform-specific/windows-powershell-git.md" .windsurf/rules/
fi

# Create content directory structure
echo ""
echo "📁 Creating content directory structure..."
mkdir -p content/arsenal/{workflows,scripts,rules,memories,integration}
echo "  ✅ Content directories created"

# Create lib directory structure
echo ""
echo "📁 Creating lib directory structure..."
if [ -d "src" ]; then
    mkdir -p src/lib/arsenal
    echo "  ✅ src/lib/arsenal/ created"
else
    mkdir -p lib/arsenal
    echo "  ✅ lib/arsenal/ created"
fi

# Count rules
rule_count=$(ls -1 .windsurf/rules/*.md 2>/dev/null | wc -l)

echo ""
echo "✅ Setup complete!"
echo ""
echo "📊 Summary:"
echo "   - Arsenal rules installed: $rule_count"
echo "   - Content directories: 5"
echo "   - Lib directories: created"
echo ""
echo "📝 Next steps:"
echo ""
echo "1. Install dependencies:"
echo "   npm install gray-matter"
echo "   npm install --save-dev @tailwindcss/typography"
echo ""
echo "2. Create TypeScript interfaces:"
echo "   # See example in README.md"
echo "   # Create src/lib/arsenal/types.ts"
echo ""
echo "3. Create content loaders:"
echo "   # See example in README.md"
echo "   # Create src/lib/arsenal/content.ts"
echo ""
echo "4. Configure Tailwind:"
echo "   # Add @tailwindcss/typography plugin"
echo "   # Add prose styles to globals.css"
echo ""
echo "5. Create your first MDX content:"
echo "   # Create content/arsenal/workflows/example.mdx"
echo ""
echo "6. Create pages:"
echo "   # Index: src/app/arsenal/workflows/page.tsx"
echo "   # Detail: src/app/arsenal/workflows/[slug]/page.tsx"
echo ""
echo "7. Test:"
echo "   npm run dev"
echo "   npm run type-check"
echo ""
echo "📖 Full setup guide: examples/nextjs-15-arsenal-content/README.md"
echo ""
echo "🎉 Ready to build your content platform!"
