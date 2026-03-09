#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════
# The Lesson Digester — GitHub Setup
# Creates the repo and pushes the initial commit
#
# Usage:
#   cd lesson-digester
#   bash scripts/setup-github.sh
# ═══════════════════════════════════════════════════════════

set -euo pipefail

AMBER='\033[0;33m'
TEAL='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${AMBER}"
echo "╔══════════════════════════════════════════════╗"
echo "║   The Lesson Digester — GitHub Setup         ║"
echo "╚══════════════════════════════════════════════╝"
echo -e "${NC}"

# ─── PREFLIGHT ───
echo -e "${TEAL}[1/6] Checking prerequisites...${NC}"

if ! command -v git &>/dev/null; then
  echo -e "${RED}Error: git not found${NC}"
  exit 1
fi

if ! command -v gh &>/dev/null; then
  echo -e "${RED}Error: gh (GitHub CLI) not found.${NC}"
  echo "Install it with: brew install gh"
  echo "Then log in with: gh auth login"
  exit 1
fi

if ! gh auth status &>/dev/null; then
  echo -e "${RED}Error: Not authenticated with GitHub CLI.${NC}"
  echo "Run: gh auth login"
  exit 1
fi

echo -e "${GREEN}✓ git and gh CLI ready${NC}"

# ─── INIT ───
echo ""
echo -e "${TEAL}[2/6] Initializing git repository...${NC}"
git init
git branch -M main
echo -e "${GREEN}✓ Repository initialized${NC}"

# ─── STAGE ───
echo ""
echo -e "${TEAL}[3/6] Staging files...${NC}"
git add -A
echo -e "${GREEN}✓ All files staged${NC}"

# ─── COMMIT ───
echo ""
echo -e "${TEAL}[4/6] Creating initial commit...${NC}"
git commit -m "$(cat <<'EOF'
Initial release: The Lesson Digester v1.0.0

Chews up cluttered CPM math lesson decks and spits out clean,
standards-aligned, story-driven presentations.

- 23 slide builders (Drummond Design System)
- MCA-III standards alignment for Grades 7-8
- Standards-based quiz/assessment generator
- AI image prompt generator
- Interactive web dashboard
- Web app scaffolder (4 templates)

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)"
echo -e "${GREEN}✓ Initial commit created${NC}"

# ─── CREATE GITHUB REPO ───
echo ""
echo -e "${TEAL}[5/6] Creating GitHub repository...${NC}"
gh repo create lesson-digester \
  --public \
  --description "Chews up cluttered CPM math lesson decks. Spits out clean, standards-aligned, story-driven presentations." \
  --source . \
  --push
echo -e "${GREEN}✓ Repository created and pushed!${NC}"

# ─── DONE ───
echo ""
echo -e "${TEAL}[6/6] All done!${NC}"
echo ""

REPO_URL=$(gh repo view --json url -q '.url' 2>/dev/null || echo "https://github.com/YOUR_USERNAME/lesson-digester")

echo -e "${GREEN}══════════════════════════════════════════════${NC}"
echo -e "${GREEN}  Your repo is live!${NC}"
echo ""
echo -e "  ${TEAL}Repository:${NC}  $REPO_URL"
echo -e "  ${TEAL}Clone:${NC}       git clone $REPO_URL"
echo ""
echo -e "  ${AMBER}Tip:${NC} To enable GitHub Pages, go to:"
echo -e "       Settings > Pages > Source: main branch"
echo -e "${GREEN}══════════════════════════════════════════════${NC}"
echo ""
