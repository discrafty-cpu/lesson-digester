#!/usr/bin/env python3
"""
THE LESSON DIGESTER — Analysis Pipeline
=========================================
The "drop-in" analyzer: give it a PPTX file, and it:
1. Extracts text from the original deck
2. Classifies each slide by type
3. Aligns content to MCA-III standards
4. Identifies required vocabulary
5. Outputs a structured lesson plan (JSON) ready for the engine

Usage:
    python rebuild.py input.pptx [--grade 7] [--output plan.json]

This script handles Phase 1 (Analysis) and Phase 2 (Content Extraction).
The actual PPTX generation (Phase 5) is done by writing a build script
that uses engine.py's slide builders.
"""

import json
import sys
import os
import re
import subprocess

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from standards import (
    align_lesson,
    get_vocabulary_for_lesson,
    format_standards_report,
    generate_vocab_discussion_prompts,
    generate_vocab_sentence_frames,
    get_teaching_insights,
    get_misconceptions_for_topic,
    generate_leveled_problems,
)

# ─── SLIDE TYPE CLASSIFICATION ──────────────────────────────────

SLIDE_TYPES = {
    "INTRO_AGENDA": {
        "keywords": ["need", "do", "next", "notebook", "pencil", "chromebook", "focus skill", "label your"],
        "priority": 10,
    },
    "CHECKIN_FEELINGS": {
        "keywords": ["how you are feeling", "feeling like number", "share with your team", "what number"],
        "priority": 9,
    },
    "BREATHING_MINDFULNESS": {
        "keywords": ["breathe in", "breathe out", "hold for", "box breathing", "mindful"],
        "priority": 9,
    },
    "COMMITMENT": {
        "keywords": ["commitment", "being in the present", "mind full", "mindful"],
        "priority": 8,
    },
    "LEARNING_TARGET": {
        "keywords": ["learning target", "success criteria", "i will", "i'll know if"],
        "priority": 8,
    },
    "TEAM_ROLES": {
        "keywords": ["facilitator", "task manager", "resource manager", "recorder reporter", "tu trabajo", "your job"],
        "priority": 7,
    },
    "STORY_NARRATIVE": {
        "keywords": [],  # Detected by context (story text, character names)
        "priority": 5,
    },
    "STORY_DRAMATIC": {
        "keywords": ["alert", "emergency", "breaking", "urgent"],
        "priority": 6,
    },
    "ACTIVITY_LAUNCH": {
        "keywords": ["teams complete", "do:", "team roles for today"],
        "priority": 7,
    },
    "PROBLEM_SLIDE": {
        "keywords": [],  # Detected by problem number patterns (7-2, 9-15, etc.)
        "priority": 4,
    },
    "CLOSURE": {
        "keywords": ["closure", "exit ticket", "wrap up", "what did you learn"],
        "priority": 8,
    },
    "HOMEWORK": {
        "keywords": ["homework", "tonight", "hw:"],
        "priority": 9,
    },
    "DAY_DIVIDER": {
        "keywords": ["day 2", "day two", "day 3"],
        "priority": 9,
    },
    "FOCUS_SKILL_DETAIL": {
        "keywords": ["focus skill", "review", "bar model", "proportion matrix"],
        "priority": 6,
    },
    "MATH_TOOL": {
        "keywords": ["proportion matrix", "bar model", "rate", "base", "part", "whole"],
        "priority": 5,
    },
    "EQUATION_SOLVE": {
        "keywords": ["solve", "equation", "find x", "simplify"],
        "priority": 4,
    },
}


def classify_slide(text):
    """
    Classify a slide's text content into a slide type.
    Returns (slide_type, confidence_score).
    """
    text_lower = text.lower()
    scores = {}

    for stype, config in SLIDE_TYPES.items():
        score = 0
        for kw in config["keywords"]:
            if kw in text_lower:
                score += config["priority"]
        scores[stype] = score

    # Special patterns
    # Problem slides: look for patterns like "7-2", "9-15", etc.
    if re.search(r'\b\d+[-–]\d+\b', text) and scores.get("PROBLEM_SLIDE", 0) == 0:
        # Check if it's primarily a problem (not just a reference)
        if len(text) < 500 and not any(scores[k] > 10 for k in scores):
            scores["PROBLEM_SLIDE"] = 6

    # Get best match
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return ("UNKNOWN", 0)
    return (best, scores[best])


def extract_text_from_pptx(pptx_path):
    """Extract text from PPTX using markitdown."""
    try:
        result = subprocess.run(
            ["python", "-m", "markitdown", pptx_path],
            capture_output=True, text=True, timeout=60
        )
        return result.stdout
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""


def parse_slides_from_markdown(md_text):
    """Parse markitdown output into individual slide texts."""
    slides = []
    current_slide = []
    slide_num = 0

    for line in md_text.split("\n"):
        # markitdown uses "<!-- Slide X -->" or "# Slide X" patterns
        if re.match(r'^<!-- Slide \d+ -->', line) or re.match(r'^# Slide \d+', line):
            if current_slide:
                slides.append({
                    "number": slide_num,
                    "text": "\n".join(current_slide),
                })
            current_slide = []
            slide_num += 1
        else:
            current_slide.append(line)

    # Last slide
    if current_slide:
        slides.append({
            "number": slide_num,
            "text": "\n".join(current_slide),
        })

    return slides


def extract_topic_keywords(full_text):
    """
    Extract math topic keywords from the full lesson text.
    Used for standards alignment.
    """
    text_lower = full_text.lower()

    # Known topic patterns to check
    topic_checks = [
        ("circumference", "circumference"),
        ("diameter", "diameter"),
        ("radius", "radius"),
        ("pi", r'\bpi\b|π|3\.14'),
        ("proportional relationships", r'proportional'),
        ("distance rate time", r'distance.*rate.*time|rate.*time|d\s*=\s*r\s*t'),
        ("scaling", r'scal(e|ing)'),
        ("scale factor", r'scale factor'),
        ("percent", r'percent|%'),
        ("ratio", r'\bratio'),
        ("proportion", r'\bproportion'),
        ("unit rate", r'unit rate'),
        ("slope", r'\bslope'),
        ("equations", r'\bequation'),
        ("inequalities", r'\binequality'),
        ("exponents", r'\bexponent'),
        ("absolute value", r'absolute value'),
        ("similarity", r'\bsimilar'),
        ("transformations", r'transform|translat|reflect'),
        ("mean median range", r'\bmean\b.*median|median.*mean'),
        ("probability", r'\bprobability'),
        ("volume", r'\bvolume'),
        ("surface area", r'surface area'),
        ("cylinder", r'\bcylinder'),
        ("multiplier", r'\bmultiplier'),
        ("interest", r'\binterest\b'),
        ("linear functions", r'linear function'),
        ("pythagorean theorem", r'pythagorean'),
        ("scientific notation", r'scientific notation'),
        ("scatterplot", r'scatterplot|scatter plot'),
        ("systems of equations", r'system.*equation'),
    ]

    found = []
    for topic, pattern in topic_checks:
        if re.search(pattern, text_lower):
            found.append(topic)

    return found


def analyze_lesson(pptx_path, grade=7):
    """
    Full analysis pipeline for a lesson PPTX.

    Returns a structured dict with:
    - slide_map: classified slides
    - topics: detected math topics
    - standards: aligned MCA-III standards
    - vocabulary: required vocabulary
    - vocab_prompts: role-specific vocabulary discussion prompts
    - report: formatted standards alignment report
    """
    print(f"Analyzing: {pptx_path}")

    # Extract text
    md_text = extract_text_from_pptx(pptx_path)
    if not md_text:
        print("  Warning: No text extracted. Trying direct read...")
        md_text = ""

    # Parse slides
    slides = parse_slides_from_markdown(md_text)
    print(f"  Found {len(slides)} slides")

    # Classify each slide
    slide_map = []
    for s in slides:
        stype, confidence = classify_slide(s["text"])
        slide_map.append({
            "number": s["number"],
            "type": stype,
            "confidence": confidence,
            "text_preview": s["text"][:200].replace("\n", " "),
        })
        print(f"  Slide {s['number']:2d}: {stype:25s} (conf: {confidence})")

    # Extract topics from full text
    full_text = md_text or ""
    topics = extract_topic_keywords(full_text)
    print(f"  Topics detected: {', '.join(topics)}")

    # Standards alignment
    alignment = align_lesson(topics, grade=grade)
    report = format_standards_report(topics, os.path.basename(pptx_path), grade=grade)

    # Vocabulary
    vocabulary = alignment["vocabulary"]
    vocab_prompts = generate_vocab_discussion_prompts(vocabulary)
    sentence_frames = generate_vocab_sentence_frames(vocabulary)

    # Teaching insights (misconceptions, differentiation, essential understandings)
    teaching_insights = get_teaching_insights(topics)

    # Leveled problems at 4 proficiency tiers
    leveled_problems = generate_leveled_problems(topics, grade)

    result = {
        "source_file": pptx_path,
        "grade": grade,
        "slide_count": len(slides),
        "slide_map": slide_map,
        "topics": topics,
        "standards": {
            "benchmarks": [b["id"] for b in alignment["benchmarks"]],
            "benchmark_details": alignment["benchmarks"],
            "strands_covered": alignment["strands_covered"],
            "gaps": alignment["gaps"],
        },
        "vocabulary": vocabulary,
        "vocab_prompts": [(r, p) for r, p in vocab_prompts],
        "sentence_frames": sentence_frames,
        "teaching_insights": teaching_insights,
        "leveled_problems": leveled_problems,
        "report": report,
    }

    return result


def generate_build_script(analysis):
    """
    Generate a Python build script from the analysis result.

    The generated script uses engine.py's build_* functions, which all follow
    the pattern: build_something(prs, data_dict)

    Args:
        analysis: dict from analyze_lesson() with topics, standards, vocabulary, etc.

    Returns:
        str: Python code that can be saved and run to build the lesson PPTX
    """
    # Extract data from analysis
    topics = analysis.get("topics", [])
    vocabulary = analysis.get("vocabulary", [])
    standards = analysis.get("standards", {})
    benchmarks = standards.get("benchmarks", [])
    benchmark_details = standards.get("benchmark_details", [])
    teaching_insights = analysis.get("teaching_insights", {})
    leveled_problems = analysis.get("leveled_problems", {})
    source_file = analysis.get("source_file", "lesson.pptx")
    grade = analysis.get("grade", 7)

    # Build the learning target from the first benchmark
    learning_target = "Understand and apply mathematical concepts"
    success_criteria = "I can solve problems using these concepts"
    if benchmark_details:
        b = benchmark_details[0]
        learning_target = f"I will {b.get('description', 'apply math concepts')[:80]}"
        success_criteria = f"I can solve problems involving {', '.join(topics[:2])}"

    # Build a clean lesson name from the source file
    lesson_name = os.path.splitext(os.path.basename(source_file))[0]
    lesson_name_clean = lesson_name.replace("_", " ").replace("-", " ")

    lines = []
    lines.append('#!/usr/bin/env python3')
    lines.append(f'"""')
    lines.append(f'AUTO-GENERATED BUILD SCRIPT — {lesson_name_clean}')
    lines.append(f'{"=" * 50}')
    lines.append(f'Generated by The Lesson Digester rebuild pipeline.')
    lines.append(f'Topics: {", ".join(topics)}')
    lines.append(f'Standards: {", ".join(benchmarks[:4])}')
    lines.append(f'Grade: {grade}')
    lines.append(f'')
    lines.append(f'Usage:  python {lesson_name}_build.py')
    lines.append(f'"""')
    lines.append('')
    lines.append('from pptx import Presentation')
    lines.append('import sys, os')
    lines.append('sys.path.insert(0, os.path.dirname(__file__))')
    lines.append('')
    lines.append('from engine import (')
    lines.append('    build_intro_agenda, build_checkin, build_breathing,')
    lines.append('    build_learning_target, build_team_roles, build_vocabulary_cards,')
    lines.append('    build_activity_launch, build_problem, build_group_discussion,')
    lines.append('    build_closure, build_homework, build_exit_ticket,')
    lines.append('    build_misconceptions_slide, build_differentiation_slide,')
    lines.append('    build_leveled_problems, build_leveled_answer_key,')
    lines.append(')')
    lines.append('')
    lines.append('')
    lines.append('def build():')
    lines.append(f'    """Build: {lesson_name_clean}"""')
    lines.append('    prs = Presentation()')
    lines.append('')

    # ── 1. INTRO / AGENDA ──
    needs_list = ["Notebook", "Pencil"]
    if any(t in str(topics) for t in ["graph", "scatter", "linear"]):
        needs_list.append("Graph paper")
    needs_list.append("Chromebook")

    lines.append('    # ── 1. INTRO / AGENDA ──')
    lines.append('    build_intro_agenda(prs, {')
    lines.append(f'        "needs": {repr(needs_list)},')
    lines.append(f'        "standards_tag": "{" | ".join(benchmarks[:3])}",')
    lines.append('    })')
    lines.append('')

    # ── 2. CHECK-IN ──
    lines.append('    # ── 2. CHECK-IN ──')
    lines.append('    build_checkin(prs, {})')
    lines.append('')

    # ── 3. BREATHING ──
    lines.append('    # ── 3. BREATHING / MINDFULNESS ──')
    lines.append('    build_breathing(prs, {})')
    lines.append('')

    # ── 4. LEARNING TARGET ──
    lines.append('    # ── 4. LEARNING TARGET ──')
    lines.append('    build_learning_target(prs, {')
    lines.append(f'        "target": {repr(learning_target)},')
    lines.append(f'        "success": {repr(success_criteria)},')
    lines.append(f'        "standards": {repr(benchmarks[:3])},')
    lines.append('    })')
    lines.append('')

    # ── 5. TEAM ROLES ──
    lines.append('    # ── 5. TEAM ROLES ──')
    lines.append('    build_team_roles(prs, {})')
    lines.append('')

    # ── 6. VOCABULARY CARDS ──
    if vocabulary:
        lines.append(f'    # ── 6. VOCABULARY CARDS ({len(vocabulary)} terms) ──')
        lines.append('    build_vocabulary_cards(prs, {')
        lines.append(f'        "terms": {repr(vocabulary[:8])},')
        lines.append('    })')
        lines.append('')

    # ── 7. ACTIVITY LAUNCH ──
    # Find the unit/problem reference from the original slides
    problem_slides = [s for s in analysis.get("slide_map", [])
                     if s["type"] == "PROBLEM_SLIDE"]
    problem_refs = []
    for ps in problem_slides:
        import re as _re
        refs = _re.findall(r'\b\d+[-–]\d+\b', ps.get("text_preview", ""))
        problem_refs.extend(refs)

    ref_str = ", ".join(problem_refs[:4]) if problem_refs else "See lesson problems"
    lines.append('    # ── 7. ACTIVITY LAUNCH ──')
    lines.append('    build_activity_launch(prs, {')
    lines.append(f'        "ref": {repr(ref_str)},')
    lines.append('        "roles": [["Facilitator", "Recorder Reporter"], ["Resource Manager", "Task Manager"]],')
    lines.append(f'        "needs": {repr(needs_list)},')
    lines.append('    })')
    lines.append('')

    # ── 8. PROBLEM SLIDES (from original) ──
    if problem_slides:
        lines.append(f'    # ── 8. PROBLEM SLIDES ({len(problem_slides)} from original lesson) ──')
        lines.append('    # TODO: Copy problem text from original deck into these data dicts')
        for i, ps in enumerate(problem_slides):
            preview = ps.get("text_preview", "")[:120].replace('"', '\\"').replace('\n', ' ')
            lines.append(f'    build_problem(prs, {{')
            lines.append(f'        "number": "{problem_refs[i] if i < len(problem_refs) else f"P{i+1}"}",')
            lines.append(f'        "text": "{preview}...",')
            lines.append(f'        "role_prompts": [')
            lines.append(f'            ("Facilitator", "Read the problem aloud. What do we know?"),')
            lines.append(f'            ("Resource Mgr", "What tools or formulas might help?"),')
            lines.append(f'            ("Task Mgr", "Let\'s set up our approach first."),')
            lines.append(f'            ("Recorder", "Write down our strategy and answer."),')
            lines.append(f'        ],')
            lines.append(f'    }})')
            lines.append('')

    # ── 9. MISCONCEPTIONS (from StemTC teaching insights) ──
    misconceptions = teaching_insights.get("misconceptions", [])
    if misconceptions:
        # Take top 3 for the slide
        top_misc = misconceptions[:3]
        lines.append(f'    # ── 9. MISCONCEPTIONS — {len(misconceptions)} found from StemTC ──')
        lines.append('    build_misconceptions_slide(prs, {')
        lines.append(f'        "topic": {repr(", ".join(topics[:2]))},')
        lines.append(f'        "standards": {repr(benchmarks[:2])},')
        lines.append('        "misconceptions": [')
        for m in top_misc:
            lines.append('            {')
            lines.append(f'                "error": {repr(m["error"])},')
            lines.append(f'                "why": {repr(m["why"])},')
            lines.append(f'                "address": {repr(m["address"])},')
            lines.append('            },')
        lines.append('        ],')
        lines.append('    })')
        lines.append('')

    # ── 10. LEVELED PROBLEMS (4 proficiency tiers) ──
    levels = leveled_problems.get("levels", [])
    if levels:
        lines.append(f'    # ── 10. LEVELED PROBLEMS — {leveled_problems.get("topic", "topic")} ──')
        lines.append('    build_leveled_problems(prs, {')
        lines.append(f'        "topic": {repr(leveled_problems.get("topic", ""))},')
        lines.append(f'        "standards": {repr(benchmarks[:2])},')
        lines.append('        "levels": [')
        for lvl in levels:
            lines.append('            {')
            lines.append(f'                "label": {repr(lvl["label"])},')
            lines.append(f'                "color": {repr(lvl.get("color", "#4CAF50"))},')
            lines.append(f'                "problems": {repr(lvl["problems"])},')
            if "standards" in lvl:
                lines.append(f'                "standards": {repr(lvl["standards"])},')
            lines.append('            },')
        lines.append('        ],')
        lines.append('    })')
        lines.append('')

        lines.append('    # ── 10b. LEVELED ANSWER KEY ──')
        lines.append('    build_leveled_answer_key(prs, {')
        lines.append(f'        "topic": {repr(leveled_problems.get("topic", ""))},')
        lines.append('        "levels": [')
        for lvl in levels:
            lines.append('            {')
            lines.append(f'                "label": {repr(lvl["label"])},')
            lines.append(f'                "problems": {repr(lvl["problems"])},')
            lines.append('            },')
        lines.append('        ],')
        lines.append('    })')
        lines.append('')

    # ── 11. DIFFERENTIATION (from StemTC) ──
    differentiation = teaching_insights.get("differentiation", {})
    if differentiation:
        essential = teaching_insights.get("essential_understandings", [])
        lines.append('    # ── 11. DIFFERENTIATION STRATEGIES (from StemTC) ──')
        lines.append('    build_differentiation_slide(prs, {')
        lines.append(f'        "topic": {repr(", ".join(topics[:2]))},')
        lines.append(f'        "standards": {repr(benchmarks[:2])},')
        lines.append('        "strategies": {')
        for key in ["emergent", "ell", "extending"]:
            if key in differentiation:
                lines.append(f'            {repr(key)}: {repr(differentiation[key])},')
        lines.append('        },')
        if essential:
            lines.append(f'        "essential_understandings": {repr(essential[:3])},')
        lines.append('    })')
        lines.append('')

    # ── 12. CLOSURE ──
    lines.append('    # ── 12. CLOSURE ──')
    lines.append('    build_closure(prs, {')
    lines.append(f'        "prompt": "Discuss: What are the key ideas about {", ".join(topics[:2])}?",')
    lines.append('    })')
    lines.append('')

    # ── 13. HOMEWORK ──
    lines.append('    # ── 13. HOMEWORK ──')
    if problem_refs:
        hw_ref = problem_refs[-1] if problem_refs else ""
        lines.append(f'    build_homework(prs, {{"ref": "Problems after {hw_ref}"}})')
    else:
        lines.append('    build_homework(prs, {"ref": "See textbook"})')
    lines.append('')

    # ── Save ──
    out_name = f"rebuilt_{lesson_name}.pptx"
    lines.append(f'    # ── SAVE ──')
    lines.append(f'    out = {repr(out_name)}')
    lines.append('    prs.save(out)')
    lines.append(f'    print(f"Created {{out}} ({{len(prs.slides)}} slides)")')
    lines.append('    return out')
    lines.append('')
    lines.append('')
    lines.append('if __name__ == "__main__":')
    lines.append('    build()')

    return "\n".join(lines)


# ─── CLI ──────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze a CPM lesson PPTX for rebuild")
    parser.add_argument("pptx", help="Path to the input PPTX file")
    parser.add_argument("--grade", type=int, default=7, help="Grade level (7 or 8)")
    parser.add_argument("--output", "-o", help="Output JSON file path")
    parser.add_argument("--build", action="store_true", help="Generate a Python build script")
    args = parser.parse_args()

    result = analyze_lesson(args.pptx, grade=args.grade)

    # Print report
    print("\n" + result["report"])
    print(f"\nVocabulary ({len(result['vocabulary'])} terms):")
    print(f"  {', '.join(result['vocabulary'])}")

    if result["standards"]["gaps"]:
        print(f"\n⚠  Strand gaps: {', '.join(result['standards']['gaps'])}")

    # Save JSON if requested
    if args.output:
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2, default=str)
        print(f"\nSaved analysis to {args.output}")

    # Generate build script if requested
    if args.build:
        base_name = os.path.splitext(os.path.basename(args.pptx))[0]
        build_script_path = os.path.join(
            os.path.dirname(args.pptx),
            f"build_{base_name}.py"
        )

        script_code = generate_build_script(result)

        with open(build_script_path, "w") as f:
            f.write(script_code)

        print(f"\n✓ Build script generated: {build_script_path}")

        # Print summary
        print("\nSlides that will be generated:")
        slide_summary = [
            "  1. INTRO_AGENDA (with topics and standards)",
            "  2. CHECKIN_FEELINGS",
            "  3. BREATHING_MINDFULNESS",
            "  4. LEARNING_TARGET (using standards)",
            "  5. TEAM_ROLES",
            "  6. VOCABULARY_CARDS (using detected vocabulary)",
        ]

        story_slides = [s for s in result.get("slide_map", [])
                       if s["type"] in ("STORY_NARRATIVE", "STORY_DRAMATIC")]
        if story_slides:
            slide_summary.append(f"  7. Story/Narrative slides ({len(story_slides)} slides from original)")

        problem_slides = [s for s in result.get("slide_map", [])
                         if s["type"] == "PROBLEM_SLIDE"]
        slide_idx = 8 if story_slides else 7
        if problem_slides:
            slide_summary.append(f"  {slide_idx}. Problem slides ({len(problem_slides)} slides from original)")
            slide_idx += 1

        misconceptions = result.get("teaching_insights", {}).get("misconceptions", [])
        if misconceptions:
            slide_summary.append(f"  {slide_idx}. MISCONCEPTIONS ({len(misconceptions)} misconceptions)")
            slide_idx += 1

        leveled_problems = result.get("leveled_problems", {})
        if leveled_problems:
            slide_summary.append(f"  {slide_idx}. LEVELED_PROBLEMS (4 proficiency tiers)")
            slide_idx += 1
            slide_summary.append(f"  {slide_idx}. LEVELED_ANSWER_KEY")
            slide_idx += 1

        differentiation = result.get("teaching_insights", {}).get("differentiation", [])
        if differentiation:
            slide_summary.append(f"  {slide_idx}. DIFFERENTIATION ({len(differentiation)} strategies)")
            slide_idx += 1

        slide_summary.append(f"  {slide_idx}. CLOSURE / EXIT_TICKET")
        slide_idx += 1
        slide_summary.append(f"  {slide_idx}. HOMEWORK")

        for line in slide_summary:
            print(line)
