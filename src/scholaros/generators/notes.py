from scholaros.llm.qwen import generate

PROMPT = """
You are an expert Computer Science professor creating study notes for a GATE CSE student.

Your task is NOT to summarize.

Your task is to reconstruct the lecture into complete, structured study notes.

Rules:
- Ignore greetings.
- Ignore jokes.
- Ignore advertisements.
- Ignore repetition.
- Organize ideas logically.
- Fill obvious gaps if the speaker skips steps.
- Preserve technical correctness.

Output ONLY Markdown.

Use this structure:

# Title

## Learning Objectives

## Core Concepts

## Definitions

## Detailed Explanation

## Examples

## Common Mistakes

## GATE Perspective

## Revision Checklist

Transcript:

{transcript}
"""


def generate_notes(transcript: str) -> str:
    print("Sending transcript to Qwen...")
    notes = generate(PROMPT.format(transcript=transcript))
    print("Notes generated.")
    return notes