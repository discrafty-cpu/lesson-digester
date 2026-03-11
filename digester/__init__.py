"""
The Lesson Digester
====================
Chews up cluttered group-based learning math lesson decks and spits out clean,
standards-aligned, story-driven presentations.

Modules:
    engine.py       — 23 slide builders (Drummond Design System)
    standards.py    — MCA-III alignment, vocab, quiz generation
    rebuild.py      — Analysis pipeline (classify, extract, align)
    data_complete.py — Complete educational databases and helper functions
"""

__version__ = "1.0.0"
__author__ = "Jon Drummond"

# Import complete data modules
from digester.data_complete import (
    TEACHING_INSIGHTS_COMPLETE,
    RISA_DIALOGUES_COMPLETE,
    LEVELED_PROBLEMS_COMPLETE,
    search_topic,
    get_all_topics_by_grade,
    get_teaching_insights_by_grade,
    get_risa_dialogues_by_grade,
    get_leveled_problems_by_grade,
)

__all__ = [
    'TEACHING_INSIGHTS_COMPLETE',
    'RISA_DIALOGUES_COMPLETE',
    'LEVELED_PROBLEMS_COMPLETE',
    'search_topic',
    'get_all_topics_by_grade',
    'get_teaching_insights_by_grade',
    'get_risa_dialogues_by_grade',
    'get_leveled_problems_by_grade',
]
