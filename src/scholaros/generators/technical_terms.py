from scholaros.llm.qwen import generate

PROMPT = """
You are an information extraction engine.

Your ONLY task is to extract Computer Science technical terms that EXPLICITLY appear in the transcript.

STRICT RULES:

- Extract ONLY technical Computer Science concepts.
- Do NOT summarize.
- Do NOT explain.
- Do NOT organize.
- Do NOT infer.
- Do NOT complete the syllabus.
- Do NOT add concepts from your own knowledge.

IGNORE:

- greetings
- advertisements
- motivation
- attendance
- instructor introductions
- exam strategy
- YouTube requests
- subscription requests

A technical term means something that could reasonably appear as a topic in:
- GATE CSE syllabus
- Computer Science textbook
- Computer Architecture textbook

GOOD examples:

Harvard Architecture
Von Neumann Architecture
Stored Program
Cache Memory
Instruction
Data Bus
Address Bus
Control Bus
Fixed Point
Floating Point
ASCII
EBCDIC
Two's Complement

BAD examples:

subscribe
attendance
class
today
teacher
experience
discount
scholarship
channel

Return ONLY one technical term per line.

If uncertain,
DO NOT include the term.

Transcript:

{transcript}
"""


def extract_terms(transcript: str) -> str:
    print("Extracting technical terms...")

    terms = generate(
        PROMPT.format(
            transcript=transcript
        )
    )
    print(terms)

    print("Technical terms extracted.")

    return terms