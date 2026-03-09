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
        "report": report,
    }

    return result


# ─── CLI ──────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Analyze a CPM lesson PPTX for rebuild")
    parser.add_argument("pptx", help="Path to the input PPTX file")
    parser.add_argument("--grade", type=int, default=7, help="Grade level (7 or 8)")
    parser.add_argument("--output", "-o", help="Output JSON file path")
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
