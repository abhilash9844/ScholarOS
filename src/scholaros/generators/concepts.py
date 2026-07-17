from scholaros.llm.qwen import generate

PROMPT = """
You are an expert Computer Science curriculum designer.

You are given a list of technical terms that were extracted from a lecture.

Do NOT invent new terms.

Use ONLY the supplied terms.

Your job is to organize them into a Concept Inventory.

Rules:

- NEVER add concepts.
- NEVER remove concepts.
- NEVER rename concepts.
- NEVER use outside knowledge.

If you cannot determine whether a concept was explained or merely mentioned,
place it under "Mentioned Today".

If no relationship can be confidently determined,
leave it under an "Unclassified" section.

Output ONLY Markdown.

Format:

# Concept Inventory

## Explained Today

...

---

## Mentioned Today

...

---

## Relationships Found

...

---

## Unclassified

...

Technical Terms:

{terms}
"""


def generate_concepts(terms: str) -> str:
    print("Building Concept Inventory...")

    concepts = generate(
        PROMPT.format(
            terms=terms
        )
    )

    print("Concept Inventory generated.")

    return concepts