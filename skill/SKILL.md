# The Lesson Digester

## Purpose
The Lesson Digester chews up cluttered, inconsistent group-based learning math lesson presentations and spits out clean, modern, visually stunning slide decks following the "Drummond Design System" — a card-based, story-driven aesthetic with professional typography, relevant AI-generated images, and consistent color theming.

## Core Philosophy: Roles Embedded, Not Bolted On

The collaborative team roles (Facilitator, Resource Manager, Task Manager, Recorder Reporter) are NOT separate "role definition" slides that eat up deck space. They are **woven into every discussion and problem slide** as natural conversation prompts. Each role has a color identity and specific sentence starters that appear contextually:

| Role | Color | Function | Signature Prompts |
|------|-------|----------|-------------------|
| **Facilitator** | Teal `0D9488` | Coordination & Inclusion | "Who wants to read?" / "Who has an idea?" / "What do we need to do to get started?" |
| **Resource Manager** | Amber `D4870F` | Logistics & Clarification | "What are we supposed to figure out?" / "What do we need to understand the problem?" |
| **Recorder Reporter** | Blue `3B82F6` | Documentation & Advocacy | "What are we going to say to the class?" / "What do we know about the problem?" |
| **Task Manager** | Red/Pink `E8436D` | Execution & Pace | "What should we try first?" / "Do we all agree?" / "Are we ready to move on?" |

**How roles appear in slides:**
- On PROBLEM slides: small role-colored prompt cards along the side or bottom — the Facilitator reads, the Resource Manager gathers materials, the Task Manager watches time, the Recorder writes
- On DISCUSSION slides: each role gets a specific question relevant to THAT problem, not generic boilerplate
- On ACTIVITY slides: role assignments tied to specific physical tasks (Timer, Marker, Measurer, etc.)
- NEVER as a full standalone "here are your roles" slide (unless it's the very first day of a new unit with new seats)

**The goal**: Every student knows exactly what their job is at every moment, embedded right in the math, without clutter.

## Quick Start (Drop-In Workflow)

When the user drops a lesson PPTX file, follow these steps:

1. **Analyze**: Run `python lesson-redesign/rebuild.py input.pptx --grade 7` to auto-classify slides and align to MCA-III standards
2. **Extract content**: Run `python -m markitdown input.pptx` for full text extraction
3. **Review alignment**: Check the MCA-III standards report — note vocabulary, covered benchmarks, and strand gaps
4. **Classify slides**: Map each slide to a Slide Type (see below)
5. **Extract & chunk**: Pull essential text, problems, instructions; tag each with role prompts
6. **Add vocabulary**: Create a VOCABULARY_CARDS slide using terms from the standards alignment
7. **Embed vocab in discussions**: Use `generate_vocab_discussion_prompts()` from standards.py to create role-specific prompts that require students to USE vocabulary terms
8. **Generate images**: Create AI images for the lesson topic
9. **Build the deck**: Use the python-pptx engine (`engine.py`) with slide builders
10. **Tag slides**: Add MCA-III standards footer to problem/discussion slides using `add_standards_footer()`
11. **QA**: Convert to images and inspect every slide

### Key Files
- `engine.py` — Slide builders (python-pptx)
- `standards.py` — MCA-III alignment database (Grade 7-8 benchmarks, vocabulary, gap analysis)
- `rebuild.py` — Analysis orchestrator (classify slides, extract topics, align standards)

### Standards Integration
Every rebuilt deck should:
- Include a **Vocabulary Cards** slide near the start (after Learning Target) with MCA-III terms
- Have **vocabulary-rich sentence frames** on discussion slides
- Show **MCA-III benchmark tags** in footers on problem slides
- Flag **strand gaps** in the teacher notes and suggest additions

---

## The Drummond Design System

### Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| **Primary** | Dark Navy | `1E2761` | Slide backgrounds (dark slides), headers |
| **Secondary** | Charcoal | `2D3748` | Body text, card borders |
| **Accent 1** | Amber/Orange | `D4870F` | Arrows, accent bars, icons, highlights |
| **Accent 2** | Teal | `0D9488` | Subtitles, links, category labels |
| **Accent 3** | Blue | `3B82F6` | Card borders, interactive elements |
| **Surface** | White | `FFFFFF` | Card backgrounds |
| **Background** | Light Gray | `F7F8FA` | Slide backgrounds (light slides) |
| **Success** | Green | `4CAF50` | Bar charts, positive indicators |
| **Danger** | Red | `EF4444` | Alerts, emergency slides |
| **Muted** | Slate | `64748B` | Captions, secondary text |

### Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Slide Title | Arial Black / Impact | 36-44pt | Bold | `1E2761` |
| Section Header | Calibri | 24-28pt | Bold | `1E2761` |
| Subtitle / Category | Calibri | 14-16pt | Normal | `0D9488` (teal) |
| Body Text | Calibri | 14-16pt | Normal | `2D3748` |
| Key Terms (inline) | Calibri | 14-16pt | Bold | `2D3748` |
| Caption | Calibri | 10-12pt | Normal | `64748B` |
| Large Stat | Arial Black | 60-72pt | Bold | `1E2761` |

### Layout Principles

1. **Card-based**: Content lives in white cards with subtle shadows on light gray backgrounds
2. **Accent bars**: Vertical orange or teal bars (0.06-0.08" wide) on the left edge of headers
3. **Breathing room**: 0.5" minimum margins, 0.3-0.5" between content blocks
4. **Two-column**: Problems use text-left, image-right layout
5. **Dark/light sandwich**: Dark backgrounds for dramatic/narrative slides, light for content
6. **No clutter**: One concept per visual area, no overlapping elements
7. **Consistent icons**: Use react-icons (Font Awesome set) for all iconography

### Key Visual Motifs

- **Orange arrows** connecting sequential elements (NEED → DO → NEXT)
- **Vertical accent bars** (teal or orange, 0.06" wide) to the left of section titles
- **Rounded icon badges** (colored circles with white icons) for categories
- **Progress/bar charts** with orange/blue/green fills for proportion visualization
- **White cards with shadows** for content grouping
- **AI-generated illustrations** relevant to the specific math context

---

## Slide Types & Templates

### 1. INTRO_AGENDA (Always Slide 1)
**Purpose**: Daily opener — NEED/DO/NEXT + Focus Skill warm-up

**Layout**:
- Top strip: Three white cards in a row (NEED | DO | NEXT) connected by orange arrows
  - NEED card: notebook icon + supply list
  - DO card: wrench icon + "Label Your Notebook: [Unit] [Lesson] [Title]"
  - NEXT card: checkmark icon + focus skill instructions
- Bottom area: Focus Skill problem(s) in a bordered card
- HW reference in corner

**Recognizing this slide**: Contains "NEED", "DO", "NEXT", notebook/pencil/chromebook, lesson number, focus skill

---

### 2. FOCUS_SKILL_DETAIL (Slide 2-3 of the redesigned version)
**Purpose**: Expanded view of the focus skill with worked examples and visual tools

**Layout**:
- Left panel: Review/explanation card with bar model or visual tool
- Right panel: Problem cards with vertical accent bar, subtitle, image, and problem text
- Bottom: Proportion matrix or bar model tool link

**Recognizing this slide**: Contains the same problems as the intro but with more detail, bar models, percentage visualizations

---

### 3. MATH_TOOL (Proportion Matrix, Bar Model, etc.)
**Purpose**: Interactive-looking math tool slide

**Layout**:
- Dark header bar with tool title and mascot/character
- Clean table layout with labeled fields (PART/WHOLE, RATE/BASE)
- Formulaic expression and decimal coefficient sections
- Footer with instruction text

**Recognizing this slide**: Contains proportion/ratio tables, math tool references

---

### 4. CHECKIN_FEELINGS
**Purpose**: Social-emotional check-in

**Layout**:
- Dark background with warm gradient
- "Share with your TEAM" header
- Prompt: "What number/picture best shows how you are feeling? Why?"
- Sentence frame: "I am feeling like number _____ because _____"
- Team role sharing order table

**Recognizing this slide**: "how you are feeling", sharing order table

---

### 5. BREATHING_MINDFULNESS
**Purpose**: Box breathing / mindfulness exercise

**Layout**:
- Full-bleed nature/calm image background (forest, ocean, sky)
- Centered breathing instruction overlay
- Minimal text, maximum visual calm

**Recognizing this slide**: "breathing", "breathe in", "hold", mindfulness imagery

---

### 6. COMMITMENT
**Purpose**: Presence/focus commitment

**Layout**:
- Split: "Mind full" vs "Mindful" visual comparison
- Commitment prompt centered
- Calm, minimal design

**Recognizing this slide**: "commitment", "being in the present"

---

### 7. LEARNING_TARGET
**Purpose**: Learning objectives and success criteria

**Layout**:
- Left 60%: "Learning Target:" header with target icon
  - Success criteria as bold "I will..." statements
  - Discussion prompt with talk icon
  - Sentence frame in italics
- Right 40%: Success Criteria card with blue border
  - "I'll know if I've got it when:" header
  - Bullet list of measurable outcomes
- Bottom right: Team sharing order table
- Relevant images scattered (speedometer, car, etc.)

**Recognizing this slide**: "Learning Target", "Success Criteria", "I will...", "I'll know if I've got it when"

---

### 8. TEAM_ROLES
**Purpose**: Define team job responsibilities

**Layout**:
- Dark charcoal background
- 2x2 grid of role cards, each with:
  - Colored circular icon (unique per role)
  - Role name (English + Spanish)
  - "Your Job / Tu Trabajo" subtitle
  - Bullet list of responsibilities (bilingual)
- Colors: Pink/maroon (Recorder), Brown (Resource), Green (Facilitator), Blue (Task Manager)

**Recognizing this slide**: "Facilitator", "Task Manager", "Resource Manager", "Recorder Reporter", job descriptions

---

### 9. TEAM_ROLES_ACTIVITY (Specific activity roles)
**Purpose**: Assign specific roles for the hands-on activity

**Layout**:
- Similar to TEAM_ROLES but with activity-specific jobs
- Example: Timer, Marker, Toy Starter, Measurer
- Include specific activity instructions

**Recognizing this slide**: Activity-specific role names (Timer, Marker, Measurer, etc.)

---

### 10. STORY_NARRATIVE
**Purpose**: Set up the lesson's story/context (the "hook")

**Layout**:
- Clean white background
- Large colored title (teal/mint) for the story name
- Story text in readable paragraphs
- AI-generated illustration of the scene (bottom-right or right-side)
- Discussion prompt box

**Recognizing this slide**: Story text, character names, narrative setup

---

### 11. STORY_DRAMATIC (Emergency/Alert/Key moment)
**Purpose**: Dramatic story beat — something happens!

**Layout**:
- DARK background (navy/charcoal)
- Split layout:
  - Left: Bold dramatic text (e.g., "Emergency Broadcast", "ALERT")
  - Right: Green accent panel with story continuation + details
- Service update / data bullet points
- AI-generated dramatic image (phone alert, emergency, etc.)

**Recognizing this slide**: Dramatic language, alerts, key story turning points

---

### 12. STORY_MISSION (Team discussion/work prompt)
**Purpose**: Bridge story to math — students discuss what to do

**Layout**:
- Left panel: Dark background with story quote and task callout
- Right panel: Role-specific prompts (Facilitator asks..., Resource Manager asks...)
- Recording table for student responses (icon + "_____ said..." format)

**Recognizing this slide**: Role-specific discussion prompts, "said" recording format

---

### 13. ACTIVITY_LAUNCH (DO slide)
**Purpose**: Launch the team activity — what to complete

**Layout**:
- Top: DO card with task list
- "Teams Complete: [Unit - Lesson: Problem numbers]"
- Team role assignment table (Computers, Calculators, Read 1st Q, Responds 1st)
- Need section with supply icons

**Recognizing this slide**: "DO:", "Teams Complete:", group-based learning problem numbers, role assignments

---

### 14. PROBLEM_SLIDE
**Purpose**: Individual problem display for class discussion

**Layout**:
- Problem number as large header
- Problem content (may include images, diagrams, graphs)
- Clean white background with ample space for discussion

**Recognizing this slide**: Individual problem numbers (7-2, 7-3, etc.), math content

---

### 15. CLOSURE
**Purpose**: End-of-lesson discussion/wrap-up

**Layout**:
- "CLOSURE" header
- Discussion prompt
- Response icons/visuals
- Clean, simple layout

**Recognizing this slide**: "CLOSURE", discussion prompts, end-of-lesson content

---

### 16. HOMEWORK
**Purpose**: Tonight's homework assignment

**Layout**:
- Bold "HOMEWORK TONIGHT" banner (amber/orange background)
- Lesson number and problem range prominently displayed
- Clean, unmistakable design

**Recognizing this slide**: "HOMEWORK", problem ranges (e.g., "7-10 to 7-14")

---

### 17. DAY_DIVIDER
**Purpose**: Marks the start of Day 2 (for multi-day lessons)

**Layout**:
- Full dark background
- Large "Day 2" centered
- Calendar icon or visual
- Lesson reference

**Recognizing this slide**: "Day 2", calendar imagery, second-day intro

---

### 18. EQUATION_SOLVE
**Purpose**: Quick equation warm-up or review

**Layout**:
- Clean centered equation display
- Large readable math text
- Instruction line

**Recognizing this slide**: Equations to solve, review problems

---

## Step-by-Step Process

### Phase 1: Analysis
```bash
python -m markitdown input.pptx
```
Read the output and create a slide map:
```
Slide 1 → INTRO_AGENDA
Slide 2 → CHECKIN_FEELINGS
Slide 3 → BREATHING_MINDFULNESS
...etc
```

### Phase 2: Content Extraction
For each slide, extract:
- **Title**: Main header text
- **Body**: Key instructional content
- **Problems**: Math problems with exact numbers/values
- **Prompts**: Discussion questions and sentence frames
- **Data**: Tables, role assignments, problem numbers
- **Notes**: Speaker notes (often contain teacher instructions)

**CRITICAL**: Preserve all math content EXACTLY. Do not paraphrase or simplify problems.

### Phase 3: Story Development
The 7.1.1 model wraps the math in a real-world narrative (George's train rescue). For each lesson:
1. Identify the core math concept (distance/rate/time, scaling, circumference, etc.)
2. Create a compelling, age-appropriate story context that naturally requires the math
3. Name the characters (diverse names)
4. Break the story into 3-4 beats that map to different slides
5. Generate AI images for key story moments

**Story guidelines**:
- Relatable to 7th/8th graders
- Real-world application of the math
- Creates urgency/engagement ("rescue mission", "solving a mystery", etc.)
- Characters face problems that require the specific math skill

### Phase 4: Image Generation
For each slide that needs an image, generate a prompt:
- Style: "Clean, modern digital illustration, flat design with subtle gradients, professional educational style"
- Include specific scene details relevant to the math context
- Request: "No text in the image"
- Resolution: High quality, 16:9 aspect ratio for slide backgrounds, 4:3 for embedded images

### Phase 5: Build with python-pptx Engine
Use `engine.py` as the base and customize for the specific lesson content.

```bash
# Import the engine
from lesson-redesign.engine import *
from lesson-redesign.standards import align_lesson, generate_vocab_discussion_prompts

# Create presentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(5.625)

# Build slides using the builder functions
build_intro_agenda(prs, {...})
build_learning_target(prs, {...})
build_vocabulary_cards(prs, {"terms": [{"term": "circumference", "definition": "..."}]})
build_problem(prs, {"number": "9-1", "text": "...", "role_prompts": [...]})

# Tag slides with standards
add_standards_footer(prs.slides[-1], ["7.3.1.1", "7.2.1.1"])

# Save
prs.save("output.pptx")
```

### Phase 6: QA
```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
rm -f slide-*.jpg
pdftoppm -jpeg -r 150 output.pdf slide
ls -1 "$PWD"/slide-*.jpg
```
Then visually inspect EVERY slide. Use a subagent for fresh eyes.

---

## Common Slide Sequences

### Standard Lesson Flow (1 Day)
1. INTRO_AGENDA
2. CHECKIN_FEELINGS
3. BREATHING_MINDFULNESS
4. COMMITMENT
5. LEARNING_TARGET
6. TEAM_ROLES (if new unit/new seats)
7. STORY_NARRATIVE (hook)
8. STORY_DRAMATIC (complication)
9. STORY_MISSION (team discussion)
10. ACTIVITY_LAUNCH
11. PROBLEM_SLIDE (×N for each problem)
12. CLOSURE
13. HOMEWORK

### Standard Lesson Flow (2 Days)
Day 1: Slides 1-13 as above
14. DAY_DIVIDER
Day 2:
15. INTRO_AGENDA (Day 2 version)
16. LEARNING_TARGET (review)
17. ACTIVITY_LAUNCH (Day 2 problems)
18. PROBLEM_SLIDE (×N)
19. CLOSURE
20. HOMEWORK

---

## Important Notes

- **Bilingual content**: Many slides include Spanish translations. PRESERVE these.
- **Problem references**: Keep exact problem numbers (7-2, 7-3, etc.) — these map to the textbook
- **Team roles**: The 4-role structure (Facilitator, Task Manager, Resource Manager, Recorder/Reporter) is standard — always include
- **Sentence frames**: These are critical scaffolds for English learners — always include them
- **Focus skills**: These are warm-up review problems, not the main lesson — keep them distinct
- **Speaker notes**: Preserve any teacher notes from the original
