#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════
# The Lesson Digester — Web App Scaffolder
# Creates new web pages/apps from templates
#
# Usage:
#   ./scripts/new-app.sh <app-name> [template]
#
# Templates:
#   dashboard  — Full interactive dashboard (default)
#   viewer     — Slide viewer / comparison page
#   report     — Standards alignment report page
#   demo       — Demo/showcase page
#
# Example:
#   ./scripts/new-app.sh standards-report report
#   ./scripts/new-app.sh slide-viewer viewer
# ═══════════════════════════════════════════════════════════

set -euo pipefail

APP_NAME="${1:?Usage: ./scripts/new-app.sh <app-name> [template]}"
TEMPLATE="${2:-dashboard}"
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WEBAPP_DIR="$PROJECT_ROOT/webapp"
APP_DIR="$WEBAPP_DIR/$APP_NAME"

AMBER='\033[0;33m'
TEAL='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${AMBER}╔══════════════════════════════════════╗${NC}"
echo -e "${AMBER}║   The Lesson Digester — Scaffolder   ║${NC}"
echo -e "${AMBER}╚══════════════════════════════════════╝${NC}"
echo ""

if [ -d "$APP_DIR" ]; then
  echo -e "${RED}Error: $APP_DIR already exists${NC}"
  exit 1
fi

echo -e "${TEAL}Creating:${NC} webapp/$APP_NAME/"
mkdir -p "$APP_DIR"

# ─── TEMPLATE: DASHBOARD ───
generate_dashboard() {
  cat > "$APP_DIR/index.html" << 'HTMLEOF'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Lesson Digester — Dashboard</title>
<link rel="stylesheet" href="../css/digester-theme.css">
<style>
  .dash-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 16px;
    margin: 30px 0;
  }
</style>
</head>
<body>
<div class="hero">
  <h1>The Lesson <span>Digester</span></h1>
  <p class="subtitle">Dashboard</p>
</div>
<div class="container">
  <h2 class="section-title">Dashboard</h2>
  <p class="section-desc">Your content goes here.</p>
  <div class="dash-grid">
    <div class="card card-accent"><h3 style="font-weight:700;margin-bottom:8px;">Panel One</h3><p style="color:var(--text-dim);font-size:0.9em;">Replace with your content.</p></div>
    <div class="card card-accent"><h3 style="font-weight:700;margin-bottom:8px;">Panel Two</h3><p style="color:var(--text-dim);font-size:0.9em;">Replace with your content.</p></div>
    <div class="card card-accent"><h3 style="font-weight:700;margin-bottom:8px;">Panel Three</h3><p style="color:var(--text-dim);font-size:0.9em;">Replace with your content.</p></div>
  </div>
</div>
<div class="footer"><span>The Lesson Digester</span> &mdash; Drummond Design System</div>
<script src="../js/digester-core.js"></script>
</body>
</html>
HTMLEOF
}

# ─── TEMPLATE: VIEWER ───
generate_viewer() {
  cat > "$APP_DIR/index.html" << 'HTMLEOF'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Lesson Digester — Slide Viewer</title>
<link rel="stylesheet" href="../css/digester-theme.css">
<style>
  .viewer-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin: 30px 0; }
  .slide-thumb { background: #0d1220; border: 1px solid var(--border); border-radius: 10px; aspect-ratio: 16/9; display: flex; align-items: center; justify-content: center; color: var(--text-dim); font-size: 0.9em; margin-bottom: 12px; cursor: pointer; transition: all 0.2s; }
  .slide-thumb:hover { border-color: var(--amber); }
  .slide-nav { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 16px; }
  .slide-nav button { width: 36px; height: 36px; border-radius: 8px; border: 1px solid var(--border); background: var(--card); color: var(--text); font-weight: 600; cursor: pointer; }
  .slide-nav button:hover { border-color: var(--amber); color: var(--amber); }
  @media (max-width: 768px) { .viewer-grid { grid-template-columns: 1fr; } }
</style>
</head>
<body>
<div class="hero"><h1>Slide <span>Viewer</span></h1><p class="subtitle">Compare before and after — side by side</p></div>
<div class="container">
  <div class="viewer-grid">
    <div class="card"><h3 style="font-weight:700;color:var(--danger);margin-bottom:16px;">Before</h3><div class="slide-thumb">Drop original slide images here</div><div class="slide-nav"></div></div>
    <div class="card"><h3 style="font-weight:700;color:var(--success);margin-bottom:16px;">After — Digested</h3><div class="slide-thumb">Drop rebuilt slide images here</div><div class="slide-nav"></div></div>
  </div>
</div>
<div class="footer"><span>The Lesson Digester</span> &mdash; Slide Viewer</div>
<script src="../js/digester-core.js"></script>
</body>
</html>
HTMLEOF
}

# ─── TEMPLATE: REPORT ───
generate_report() {
  cat > "$APP_DIR/index.html" << 'HTMLEOF'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Lesson Digester — Standards Report</title>
<link rel="stylesheet" href="../css/digester-theme.css">
<style>
  .report-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; flex-wrap: wrap; gap: 12px; }
  .strand-section { margin-bottom: 24px; }
  .strand-title { font-weight: 700; font-size: 1.1em; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid var(--border); }
  .benchmark-row { display: flex; align-items: center; gap: 16px; padding: 12px 16px; background: var(--card); border: 1px solid var(--border); border-radius: 10px; margin-bottom: 8px; transition: all 0.2s; }
  .benchmark-row:hover { border-color: var(--amber); }
  .benchmark-id { font-weight: 700; color: var(--amber); min-width: 80px; }
  .benchmark-desc { flex: 1; font-size: 0.9em; color: var(--text-dim); }
  .status-covered { color: var(--success); font-weight: 600; }
  .status-gap { color: var(--danger); font-weight: 600; }
  .vocab-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 10px; margin: 20px 0; }
  .vocab-card { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 14px; border-left: 3px solid var(--teal); }
  .vocab-card h4 { font-size: 0.9em; margin-bottom: 4px; }
  .vocab-card p { font-size: 0.78em; color: var(--text-dim); }
</style>
</head>
<body>
<div class="hero"><h1>Standards <span>Report</span></h1><p class="subtitle">MCA-III alignment analysis for your lesson</p></div>
<div class="container">
  <div class="report-header">
    <div><h2 class="section-title">Lesson: <span style="color:var(--amber);">[Lesson Name]</span></h2><p class="section-desc">Grade 7 &bull; MCA-III Mathematics</p></div>
    <div><span class="tag tag-teal">6 Benchmarks Aligned</span> <span class="tag tag-pink">2 Gaps Found</span></div>
  </div>
  <div class="strand-section">
    <div class="strand-title">Number &amp; Operation</div>
    <div class="benchmark-row"><div class="benchmark-id">7.1.1.1</div><div class="benchmark-desc">Know properties of rational numbers</div><div class="status-covered">&#x2713; Covered</div></div>
  </div>
  <div class="strand-section">
    <div class="strand-title">Geometry &amp; Measurement</div>
    <div class="benchmark-row"><div class="benchmark-id">7.3.2.1</div><div class="benchmark-desc">Calculate area of circles</div><div class="status-covered">&#x2713; Covered</div></div>
    <div class="benchmark-row"><div class="benchmark-id">7.3.2.3</div><div class="benchmark-desc">Understand pi as ratio of circumference to diameter</div><div class="status-covered">&#x2713; Covered</div></div>
  </div>
  <h2 class="section-title" style="margin-top:40px;">Vocabulary</h2>
  <p class="section-desc">MCA-III required terms for this lesson</p>
  <div class="vocab-grid">
    <div class="vocab-card"><h4>circumference</h4><p>The distance around a circle</p></div>
    <div class="vocab-card"><h4>diameter</h4><p>A line segment through the center</p></div>
    <div class="vocab-card"><h4>radius</h4><p>Half the diameter</p></div>
    <div class="vocab-card"><h4>pi</h4><p>Ratio of circumference to diameter</p></div>
  </div>
</div>
<div class="footer"><span>The Lesson Digester</span> &mdash; Standards Report</div>
<script src="../js/digester-core.js"></script>
</body>
</html>
HTMLEOF
}

# ─── TEMPLATE: DEMO ───
generate_demo() {
  cat > "$APP_DIR/index.html" << 'HTMLEOF'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Lesson Digester — Demo</title>
<link rel="stylesheet" href="../css/digester-theme.css">
<style>
  .demo-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; margin: 30px 0; }
  .demo-card { text-align: center; padding: 30px 20px; }
  .demo-card .icon { font-size: 2.5em; margin-bottom: 12px; }
  .demo-card h3 { font-weight: 700; margin-bottom: 8px; }
  .demo-card p { font-size: 0.88em; color: var(--text-dim); line-height: 1.5; }
  .cta-box { text-align: center; margin: 50px 0; padding: 48px; background: linear-gradient(135deg, var(--navy) 0%, #12183a 100%); border: 1px solid var(--border); border-radius: 20px; }
  .cta-box h2 { font-size: 1.8em; font-weight: 800; margin-bottom: 16px; }
  .cta-box h2 span { color: var(--amber); }
  .cta-box p { color: var(--text-dim); max-width: 500px; margin: 0 auto 24px; }
</style>
</head>
<body>
<div class="hero"><h1>The Lesson <span>Digester</span></h1><p class="subtitle">See what it can do</p></div>
<div class="container">
  <div class="demo-grid">
    <div class="card demo-card"><div class="icon">&#x1F4E5;</div><h3>Drop In</h3><p>Upload any CPM lesson PPTX and watch it transform.</p></div>
    <div class="card demo-card"><div class="icon">&#x1F52C;</div><h3>Analyze</h3><p>Auto-classify 23 slide types, detect topics, flag duplicates.</p></div>
    <div class="card demo-card"><div class="icon">&#x1F3AF;</div><h3>Align</h3><p>Match to MCA-III benchmarks with vocabulary and gap analysis.</p></div>
    <div class="card demo-card"><div class="icon">&#x1F4D6;</div><h3>Story</h3><p>Real-world narrative arcs that make math meaningful.</p></div>
    <div class="card demo-card"><div class="icon">&#x1F3A8;</div><h3>Design</h3><p>Drummond Design System — card layouts, role colors, clean type.</p></div>
    <div class="card demo-card"><div class="icon">&#x2705;</div><h3>QA</h3><p>Visual inspection catches overflow, fixes issues automatically.</p></div>
  </div>
  <div class="cta-box">
    <h2>Ready to <span>Digest</span>?</h2>
    <p>Drop a lesson PPTX into Claude and say "Digest this lesson."</p>
    <button class="btn btn-primary">Try It Now</button>
  </div>
</div>
<div class="footer"><span>The Lesson Digester</span> &mdash; Demo</div>
<script src="../js/digester-core.js"></script>
</body>
</html>
HTMLEOF
}

# ─── DISPATCH ───
case "$TEMPLATE" in
  dashboard) generate_dashboard ;;
  viewer)    generate_viewer ;;
  report)    generate_report ;;
  demo)      generate_demo ;;
  *)
    echo -e "${RED}Unknown template: $TEMPLATE${NC}"
    echo "Available: dashboard, viewer, report, demo"
    exit 1
    ;;
esac

echo ""
echo -e "${GREEN}✓ Created: webapp/$APP_NAME/index.html${NC}"
echo -e "${GREEN}✓ Template: $TEMPLATE${NC}"
echo -e "${TEAL}Open in browser:${NC} webapp/$APP_NAME/index.html"
echo ""
