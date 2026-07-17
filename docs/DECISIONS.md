# Architecture Decisions

This document records important engineering decisions made during ScholarOS development.

---

## ADR-001: Modular Knowledge Pipeline

**Status:** Accepted

Instead of one large prompt, ScholarOS is divided into independent stages.

Pipeline:

Transcript
→ Transcript Cleaner
→ Transcript Preprocessor
→ Technical Term Extraction
→ Concept Inventory
→ Elite Notes

Reason:
- Easier debugging
- Better testing
- Better maintainability
- Independent improvements

---

## ADR-002: Deterministic Concept Detection

**Status:** In Progress

Technical term extraction should not rely solely on an LLM.

Reason:
- Prevent hallucinations
- Improve reproducibility
- Increase accuracy

LLMs will organize and explain concepts rather than discover them.

---

## ADR-003: Truthful Documentation

**Status:** Accepted

Documentation must describe the current state of ScholarOS.

Do not document planned features as implemented.

Planned work must be clearly marked as "Planned" or "In Progress."

---

## ADR-004: Development Without External Dependencies

**Status:** Proposed

ScholarOS development should not repeatedly depend on YouTube.

Future solution:

- Transcript caching
- Local transcript input
- Offline development pipeline

Reason:
- Avoid API/rate limits
- Faster iteration
- Better reliability