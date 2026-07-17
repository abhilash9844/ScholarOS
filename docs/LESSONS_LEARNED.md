# Lessons Learned

---

# 2026-07-16

## Problem

The first version of ScholarOS generated mediocre notes that were closer to summaries than study material.

---

## Investigation

Several experiments were performed.

### Observation 1

English transcripts produced significantly better notes than Hindi auto-generated transcripts.

### Observation 2

The bottleneck was not the LLM itself.

The biggest limitation was transcript quality.

### Observation 3

Very large transcripts (40k+ characters) caused the model to ignore later instructions in the prompt.

---

## Root Causes

1. Low-quality transcripts
2. Very long context
3. Trying to make one prompt perform many independent tasks

---

## Evidence

- English transcript → Better notes
- Hindi auto transcript → Poor notes
- Elite prompt improved quality considerably
- Cleaner transcript improved consistency

---

## Engineering Decisions

### Decision 1

Transcript cleaning should happen before note generation.

Pipeline:

YouTube

↓

Transcript Provider

↓

Transcript Cleaner

↓

LLM

↓

Elite Notes

---

### Decision 2

If a task can be solved deterministically with code, do NOT use the LLM.

Examples:

- Transcript cleaning
- Wiki links
- Metadata
- File naming
- Obsidian formatting

Use the LLM only for reasoning and explanation.

---

### Decision 3

One giant prompt does not scale.

ScholarOS should evolve into multiple generators.

Examples:

- Notes Generator
- Revision Generator
- Flashcard Generator
- Knowledge Check Generator
- Quiz Generator

---

### Decision 4

ScholarOS should optimize for learning, not note generation.

The learner should spend more time thinking than reading.

---

## New Philosophy

ScholarOS is NOT an AI summarizer.

ScholarOS is an evidence-based Learning Operating System.

---

## Future Improvements

High Priority

- Rapid Revision Kit
- Knowledge Check Generator
- Elite Flashcards
- Textbook Retrieval (RAG)

Medium Priority

- Whisper fallback
- OCR
- PYQ Retrieval

Long Term

- Knowledge Graph
- Adaptive Revision
- Mastery Score

## Lesson

The objective is not to summarize lectures.

The objective is to preserve knowledge.

A lecture may briefly introduce concepts that are explained later.

Those concepts must still be captured so the learner has a complete map of the subject.

ScholarOS should distinguish between:

- Covered Concepts
- Mentioned Concepts

rather than discarding concepts that receive little explanation.
# Lesson

Prompt engineering alone is insufficient for reliable concept extraction.

Use deterministic extraction for identifying concepts.

Use LLMs for organization, explanation, and reasoning.

Separate extraction from generation.

Repeated transcript downloads during development cause YouTube rate limiting.

Development should use cached transcripts instead of repeatedly requesting YouTube.