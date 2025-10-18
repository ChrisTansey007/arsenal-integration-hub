#!/bin/bash

# Arsenal Integration Hub - Install All Arsenals Script
# This script clones all Arsenal repositories to your local machine

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
ARSENAL_DIR="${HOME}/arsenals"
GITHUB_USER="ChrisTansey007"

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to clone or update repository
clone_or_update() {
    local repo_name=$1
    local repo_path="${ARSENAL_DIR}/${repo_name}"
    
    if [ -d "${repo_path}" ]; then
        print_info "Updating ${repo_name}..."
        cd "${repo_path}"
        git pull origin main
        print_success "${repo_name} updated!"
    else
        print_info "Cloning ${repo_name}..."
        git clone "https://github.com/${GITHUB_USER}/${repo_name}.git" "${repo_path}"
        print_success "${repo_name} cloned!"
    fi
}

# Main script
echo ""
echo "================================================"
echo "  Arsenal Integration Hub - Install Script"
echo "================================================"
echo ""

print_info "Installing all Arsenal repositories to: ${ARSENAL_DIR}"
echo ""

# Create arsenals directory if it doesn't exist
mkdir -p "${ARSENAL_DIR}"

# Clone/update all Arsenal repositories
print_info "Step 1/5: Installing Windsurf Memories Arsenal..."
clone_or_update "windsurf-memories-arsenal"
echo ""

print_info "Step 2/5: Installing Prompt Arsenal..."
clone_or_update "prompt-arsenal"
echo ""

print_info "Step 3/5: Installing AI Rules Arsenal..."
clone_or_update "ai-rules-arsenal"
echo ""

print_info "Step 4/5: Installing AI Workflows Arsenal..."
clone_or_update "ai-workflows-arsenal"
echo ""

print_info "Step 5/5: Installing AI Scripts Arsenal..."
clone_or_update "ai-scripts-arsenal"
echo ""

# Create symbolic links for easy access (optional)
print_info "Creating quick access links..."
mkdir -p "${HOME}/.local/bin"

# Create helper script
cat > "${HOME}/.local/bin/arsenal" << 'EOF'
#!/bin/bash
# Arsenal Helper Script

ARSENAL_DIR="${HOME}/arsenals"

case "$1" in
    list)
        echo "Available Arsenals:"
        ls -1 "${ARSENAL_DIR}"
        ;;
    update)
        echo "Updating all Arsenals..."
        for repo in "${ARSENAL_DIR}"/*; do
            if [ -d "$repo/.git" ]; then
                echo "Updating $(basename $repo)..."
                cd "$repo" && git pull
            fi
        done
        ;;
    open)
        if [ -z "$2" ]; then
            echo "Usage: arsenal open <name>"
            echo "Available: memories, prompts, rules, workflows, scripts"
            exit 1
        fi
        case "$2" in
            memories) cd "${ARSENAL_DIR}/windsurf-memories-arsenal" ;;
            prompts) cd "${ARSENAL_DIR}/prompt-arsenal" ;;
            rules) cd "${ARSENAL_DIR}/ai-rules-arsenal" ;;
            workflows) cd "${ARSENAL_DIR}/ai-workflows-arsenal" ;;
            scripts) cd "${ARSENAL_DIR}/ai-scripts-arsenal" ;;
            *) echo "Unknown arsenal: $2"; exit 1 ;;
        esac
        ;;
    *)
        echo "Arsenal Helper"
        echo ""
        echo "Usage: arsenal <command>"
        echo ""
        echo "Commands:"
        echo "  list    - List all installed Arsenals"
        echo "  update  - Update all Arsenals"
        echo "  open    - Open an Arsenal directory"
        echo ""
        ;;
esac
EOF

chmod +x "${HOME}/.local/bin/arsenal"

# Print summary
echo ""
echo "================================================"
echo "  ✨ Installation Complete!"
echo "================================================"
echo ""
print_success "All Arsenals installed successfully!"
echo ""
echo "📁 Installation directory: ${ARSENAL_DIR}"
echo ""
echo "Available Arsenals:"
echo "  💭 Windsurf Memories Arsenal  - ${ARSENAL_DIR}/windsurf-memories-arsenal"
echo "  📝 Prompt Arsenal             - ${ARSENAL_DIR}/prompt-arsenal"
echo "  ⚙️  AI Rules Arsenal           - ${ARSENAL_DIR}/ai-rules-arsenal"
echo "  🔄 AI Workflows Arsenal       - ${ARSENAL_DIR}/ai-workflows-arsenal"
echo "  🤖 AI Scripts Arsenal         - ${ARSENAL_DIR}/ai-scripts-arsenal"
echo ""
echo "🔧 Helper command installed: arsenal"
echo ""
echo "Quick commands:"
echo "  arsenal list    - List all Arsenals"
echo "  arsenal update  - Update all Arsenals"
echo "  arsenal open memories - Open Memories Arsenal"
echo ""
echo "📚 Next steps:"
echo "  1. Browse available content in ${ARSENAL_DIR}"
echo "  2. Copy files to your project's .windsurf/ directory"
echo "  3. Start using Arsenal with Windsurf!"
echo ""
echo "💡 See examples: ${ARSENAL_DIR}/../arsenal-integration-hub/examples/"
echo ""
print_success "Happy coding! 🚀"
echo ""
