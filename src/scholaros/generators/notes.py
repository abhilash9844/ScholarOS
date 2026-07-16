from scholaros.llm.qwen import generate

PROMPT = """
You are a senior Computer Science professor, textbook author, and GATE CSE mentor.

Your goal is to create ELITE study notes for a student targeting a top GATE rank.

This is NOT a summary.

Convert the lecture into textbook-quality notes.

Rules:

- Ignore greetings.
- Ignore advertisements.
- Ignore motivational talk.
- Ignore repetition.
- Ignore YouTube related content.
- Ignore course promotions.
- Preserve every technical concept.
- Reorganize the lecture logically.
- Fill small missing explanations using standard Computer Science knowledge.
- Never invent facts.
- Use formal textbook language.
- Explain concepts from first principles.
- Whenever appropriate, compare concepts in tables.
- Add intuitive explanations.
- Mention common misconceptions.
- Mention why the concept is important.
- Mention where it connects with other GATE subjects.
- Write in Markdown only.

Output Structure:

# Title

## Learning Goals

State what the student should know after studying this note.

---

## Big Picture

Explain where this topic fits inside Computer Organization and Architecture.

---

## Core Concepts

Explain every important concept thoroughly.

For every concept include:

- Definition
- Intuition
- Working
- Advantages
- Disadvantages
- Real-world example (if applicable)

---

## Comparison Tables

Create tables whenever concepts are compared.

---

## Common Misconceptions

Mention mistakes students usually make.

---

## GATE Perspective

Include:

- Frequently asked ideas
- Important observations
- Memory tricks
- Related topics

---

## Cross Subject Connections

Mention related concepts using Obsidian wiki links.

Example:

- [[Cache Memory]]
- [[Operating Systems]]
- [[Memory Hierarchy]]
- [[CPU]]
- [[Pipeline]]

---

## Revision Box

Write a 10-line ultra-short revision.

---

## Flashcard Seeds

Generate 5-10 question-answer pairs.

Example:

Q: ...

A: ...

---

Transcript:

{transcript}
"""


def generate_notes(transcript: str) -> str:
    print("Sending transcript to Qwen...")

    notes = generate(
        PROMPT.format(
            transcript=transcript
        )
    )

    print("Notes generated.")

    return notes