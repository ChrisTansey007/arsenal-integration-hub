#!/bin/bash

# Database Migrations - Arsenal Setup Script
# Sets up custom SQL migration rule for your project

set -e

echo "🔧 Setting up Database Migrations Arsenal configuration..."

# Check if we're in a project directory
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

# Copy the database migrations rule
echo "📋 Copying Database Migrations rule..."
cp "$(dirname "$0")/database-migrations-rule.md" .windsurf/rules/

# Copy optional workflow if available
if [ -f "$HOME/arsenals/ai-workflows-arsenal/windsurf/development/database-migration-check.md" ]; then
    echo "🔄 Copying Database Migration Check workflow..."
    cp "$HOME/arsenals/ai-workflows-arsenal/windsurf/development/database-migration-check.md" .windsurf/workflows/
else
    echo "⚠️  Optional workflow not found. You can add it later."
fi

# Success message
echo "✅ Database Migrations Arsenal setup complete!"
echo ""
echo "📁 Files created:"
echo "   - .windsurf/rules/database-migrations-rule.md"
echo "   - .windsurf/workflows/database-migration-check.md (if available)"
echo ""
echo "🚀 Next steps:"
echo "   1. Open Windsurf in your project: windsurf ."
echo "   2. The Database Migrations rule will be active automatically"
echo "   3. Customize the rule for your specific database setup"
echo "   4. Start creating migrations with confidence!"
echo ""
echo "💡 Pro tip: Review the rule file to understand all the safeguards in place."
