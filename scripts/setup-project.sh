#!/bin/bash

# Arsenal Integration Hub - Project Setup Script
# Sets up a new project with Arsenal integration

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

print_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
print_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }

# Check if project name provided
if [ -z "$1" ]; then
    echo "Usage: $0 <project-name> [project-type]"
    echo ""
    echo "Project types:"
    echo "  fullstack  - Next.js + FastAPI (default)"
    echo "  frontend   - Next.js only"
    echo "  backend    - FastAPI only"
    echo "  mobile     - React Native"
    echo "  minimal    - Basic setup"
    echo ""
    exit 1
fi

PROJECT_NAME=$1
PROJECT_TYPE=${2:-fullstack}
ARSENAL_DIR="${HOME}/arsenals"

echo ""
echo "================================================"
echo "  Arsenal Project Setup"
echo "================================================"
echo ""
print_info "Project: ${PROJECT_NAME}"
print_info "Type: ${PROJECT_TYPE}"
echo ""

# Check if Arsenals are installed
if [ ! -d "${ARSENAL_DIR}" ]; then
    print_warning "Arsenals not found. Running install script..."
    curl -sSL https://raw.githubusercontent.com/ChrisTansey007/arsenal-integration-hub/main/scripts/install-all.sh | bash
fi

# Create project directory
print_info "Creating project directory..."
mkdir -p "${PROJECT_NAME}"
cd "${PROJECT_NAME}"

# Create Arsenal structure
print_info "Creating Arsenal structure..."
mkdir -p .windsurf/{memories,rules,workflows}

# Copy files based on project type
case "$PROJECT_TYPE" in
    fullstack)
        print_info "Setting up full-stack project..."
        
        # Memories
        cp "${ARSENAL_DIR}/windsurf-memories-arsenal/project-types/nextjs-app-router-memory.md" \
           .windsurf/memories/
        cp "${ARSENAL_DIR}/windsurf-memories-arsenal/project-types/fastapi-memory.md" \
           .windsurf/memories/
        cp "${ARSENAL_DIR}/windsurf-memories-arsenal/team-workflows/code-review-standards-memory.md" \
           .windsurf/memories/
        
        # Rules
        cp "${ARSENAL_DIR}/ai-rules-arsenal/windsurf/by-framework/nextjs-app-router.md" \
           .windsurf/rules/ 2>/dev/null || print_warning "Rules not found, skipping..."
        
        # Workflows
        cp "${ARSENAL_DIR}/ai-workflows-arsenal/windsurf/development"/*.md \
           .windsurf/workflows/ 2>/dev/null || print_warning "Workflows not found, skipping..."
        
        print_success "Full-stack setup complete!"
        ;;
        
    frontend)
        print_info "Setting up frontend project..."
        
        cp "${ARSENAL_DIR}/windsurf-memories-arsenal/project-types/nextjs-app-router-memory.md" \
           .windsurf/memories/
        cp "${ARSENAL_DIR}/ai-workflows-arsenal/windsurf/development"/*.md \
           .windsurf/workflows/ 2>/dev/null || true
        
        print_success "Frontend setup complete!"
        ;;
        
    backend)
        print_info "Setting up backend project..."
        
        cp "${ARSENAL_DIR}/windsurf-memories-arsenal/project-types/fastapi-memory.md" \
           .windsurf/memories/
        cp "${ARSENAL_DIR}/ai-workflows-arsenal/windsurf/development"/*.md \
           .windsurf/workflows/ 2>/dev/null || true
        
        print_success "Backend setup complete!"
        ;;
        
    mobile)
        print_info "Setting up mobile project..."
        
        cp "${ARSENAL_DIR}/windsurf-memories-arsenal/project-types/react-native-memory.md" \
           .windsurf/memories/ 2>/dev/null || print_warning "React Native memory not found"
        cp "${ARSENAL_DIR}/ai-workflows-arsenal/windsurf/development"/*.md \
           .windsurf/workflows/ 2>/dev/null || true
        
        print_success "Mobile setup complete!"
        ;;
        
    minimal)
        print_info "Setting up minimal project..."
        print_success "Minimal setup complete! Add memories and rules as needed."
        ;;
        
    *)
        print_warning "Unknown project type: ${PROJECT_TYPE}"
        print_info "Creating minimal setup..."
        ;;
esac

# Create README
cat > README.md << EOF
# ${PROJECT_NAME}

## Arsenal Integration

This project uses the Arsenal ecosystem for AI-powered development.

### Arsenal Files

\`\`\`
.windsurf/
├── memories/   - Project context for Cascade
├── rules/      - Development guidelines
└── workflows/  - Automated tasks
\`\`\`

### Getting Started

1. **Open in Windsurf:**
   \`\`\`bash
   windsurf .
   \`\`\`

2. **Arsenal files auto-load!**

3. **Start building:**
   - Ask Cascade to build features
   - Use workflows like \`/run-tests-and-fix\`
   - Leverage memories for context

### Available Workflows

$(ls .windsurf/workflows/ 2>/dev/null | sed 's/\.md$//' | sed 's/^/- \//' || echo "- No workflows yet")

### Customization

Edit files in \`.windsurf/\` to match your project needs.

### Resources

- [Arsenal Integration Hub](https://github.com/ChrisTansey007/arsenal-integration-hub)
- [Memories Arsenal](https://github.com/ChrisTansey007/windsurf-memories-arsenal)
- [Workflows Arsenal](https://github.com/ChrisTansey007/ai-workflows-arsenal)

---

**Built with ❤️ using Arsenal**
EOF

# Initialize git
print_info "Initializing git repository..."
git init
git add .
git commit -m "Initial commit with Arsenal integration"

# Print summary
echo ""
echo "================================================"
echo "  ✨ Project Setup Complete!"
echo "================================================"
echo ""
print_success "Project created: ${PROJECT_NAME}"
echo ""
echo "📁 Location: $(pwd)"
echo ""
echo "Arsenal files installed:"
echo "  💭 Memories: $(ls -1 .windsurf/memories/ | wc -l) files"
echo "  ⚙️  Rules: $(ls -1 .windsurf/rules/ 2>/dev/null | wc -l) files"
echo "  🔄 Workflows: $(ls -1 .windsurf/workflows/ 2>/dev/null | wc -l) files"
echo ""
echo "Next steps:"
echo "  1. cd ${PROJECT_NAME}"
echo "  2. Open in Windsurf: windsurf ."
echo "  3. Start building with Cascade!"
echo ""
print_success "Happy coding! 🚀"
echo ""
