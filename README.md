# The Lesson Digester

**Chews up cluttered group-based learning math lesson decks. Spits out clean, standards-aligned, story-driven presentations.**

Built on the **Drummond Design System** — card-based layouts, navy/amber/teal palette, embedded collaborative roles, and MCA-III standards alignment baked into every slide.

---

## What It Does

Drop in a 50+ slide group-based learning lesson PowerPoint. Get back a focused 20-25 slide deck that:

- Follows a **real-world story arc** (not just "here's math")
- Embeds **collaborative group-based learning roles** (Facilitator, Resource Manager, Task Manager, Recorder Reporter) as natural conversation prompts — not standalone slides
- Tags every slide with **MCA-III benchmarks** (Minnesota state standards)
- Weaves in **vocabulary** with sentence frames and discussion prompts
- Generates **standards-based assessment items** for exit tickets
- Passes **visual QA** — every slide checked for overflow, alignment, readability

## Project Structure

```
lesson-digester/
├── digester/               # Core Python engine
│   ├── engine.py           # 23 slide builders (Drummond Design System)
│   ├── standards.py        # MCA-III alignment, vocab, quiz generator
│   └── rebuild.py          # Analysis pipeline (classify → align → plan)
├── webapp/                 # Interactive web interface
│   ├── index.html          # Main dashboard & pipeline visualization
│   ├── css/                # Shared Drummond Design System theme
│   ├── js/                 # Shared JavaScript utilities
│   ├── slide-viewer/       # Before/after slide comparison
│   ├── standards-report/   # MCA-III alignment report page
│   └── demo/               # Showcase page
├── skill/                  # Claude skill files
│   └── SKILL.md            # Drop-in skill documentation
├── scripts/                # Automation
│   ├── setup-github.sh     # One-command GitHub repo creation
│   └── new-app.sh          # Scaffold new web apps from templates
├── requirements.txt
└── README.md
```

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Analyze a lesson
```python
from digester.rebuild import analyze_lesson

result = analyze_lesson("path/to/lesson.pptx", grade=7)
print(result)  # Classified slides, topics, standards alignment
```

### 3. Build slides
```python
from pptx import Presentation
from digester.engine import build_intro_agenda, build_story_narrative, build_problem_slide

prs = Presentation()
build_intro_agenda(prs, {"title": "The Pizza Problem", "day": "Day 1 of 2"})
build_story_narrative(prs, {"title": "Marco's Pizzeria", "story": "..."})
prs.save("rebuilt-lesson.pptx")
```

### 4. Standards alignment
```python
from digester.standards import align_lesson, generate_quiz_items

alignment = align_lesson(["area", "circle", "pi"], grade=7)
quiz = generate_quiz_items(["area", "circle"], num_items=5, grade=7)
```

## Web App Scaffolder

Create new web pages from templates:

```bash
bash scripts/new-app.sh my-new-page dashboard   # Full dashboard
bash scripts/new-app.sh comparison viewer        # Before/after viewer
bash scripts/new-app.sh report report            # Standards report
bash scripts/new-app.sh showcase demo            # Demo/showcase
```

## 23 Slide Types

| Type | Builder | Description |
|------|---------|-------------|
| Intro/Agenda | `build_intro_agenda()` | Day overview with learning targets |
| Check-in | `build_checkin_feelings()` | Emoji-scale feelings check |
| Breathing | `build_breathing()` | Mindfulness exercise |
| Learning Target | `build_learning_target()` | "I can..." statement with standards |
| Team Roles | `build_team_roles()` | Color-coded role assignments |
| Story Narrative | `build_story_narrative()` | Story arc setup |
| Story Dramatic | `build_story_dramatic()` | Dramatic twist/reveal |
| Story Mission | `build_story_mission()` | Team challenge |
| Group Discussion | `build_group_discussion()` | Role-prompted discussion |
| Activity Launch | `build_activity_launch()` | Hands-on setup |
| Problem Slide | `build_problem_slide()` | Math problem with role prompts |
| Vocabulary Cards | `build_vocabulary_cards()` | MCA-III terms grid |
| Standards Tag | `build_standards_tag()` | Benchmark display |
| Exit Ticket | `build_exit_ticket()` | 3-question formative check |
| Warm-Up Review | `build_warmup_review()` | Day 2 opener |
| Would You Rather | `build_would_you_rather()` | A vs B comparison |
| Notice/Wonder | `build_notice_wonder()` | Observation routine |
| Learning Log | `build_learning_log()` | Reflection + metacognition |
| Timer | `build_timer()` | Timed activity with roles |
| Day Divider | `build_day_divider()` | Multi-day separator |
| Closure | `build_closure()` | Key takeaways |
| Homework | `build_homework()` | Practice + resources |
| Quiz Generator | `generate_quiz_items()` | Auto-generated assessment items |

## Design System

**Palette:** Navy `#1E2761` / Amber `#D4870F` / Teal `#0D9488` / Blue `#3B82F6` / Pink `#E8436D`

**Role Colors:** Facilitator=Teal / Resource Manager=Amber / Task Manager=Pink / Recorder Reporter=Blue

**Layout:** Card-based with vertical accent bars, dark/light contrast panels, orange directional arrows

## License

MIT

## Author

Jon Drummond — Built with Claude
