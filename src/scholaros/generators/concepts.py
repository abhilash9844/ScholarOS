from scholaros.llm.qwen import generate

PROMPT = """
You are an information extraction system.

Your task is NOT to summarize.
Your task is NOT to teach.
Your task is NOT to complete the syllabus.

Your ONLY job is to extract concepts that explicitly appear in the transcript.

Rules:

- NEVER invent concepts.
- NEVER add concepts from your own knowledge.
- NEVER predict future topics.
- NEVER complete hierarchies using outside knowledge.
- Every concept in the output must be traceable to the transcript.
- Ignore greetings.
- Ignore advertisements.
- Ignore motivational speech.
- Ignore course promotion.

Output ONLY markdown.

# Concept Inventory

## Explained Today

List only concepts that were actually explained.

---

## Mentioned Today

List concepts that were mentioned but not explained.

---

## Relationships Found

Create a hierarchy ONLY when the relationship is explicitly stated by the lecturer.

If no hierarchy exists in the transcript, do not invent one.

If you are unsure whether a concept appeared,
DO NOT include it.

Transcript:

{transcript}
"""


def generate_concepts(transcript: str) -> str:
    print("Generating Concept Inventory...")

    concepts = generate(
        PROMPT.format(
            transcript=transcript
        )
    )

    print("Concept Inventory generated.")

    return concepts