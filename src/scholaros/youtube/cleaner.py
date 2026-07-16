import re


def clean_transcript(text: str) -> str:
    """
    Cleans raw YouTube transcripts before sending them to the LLM.
    """

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove common YouTube promotions
    patterns = [
        r"like,? share and subscribe.*?(?=\.|$)",
        r"don't forget to subscribe.*?(?=\.|$)",
        r"subscribe to the channel.*?(?=\.|$)",
        r"press the bell icon.*?(?=\.|$)",
        r"join our telegram.*?(?=\.|$)",
        r"follow me on instagram.*?(?=\.|$)",
        r"use code .*?(?=\.|$)",
        r"discount.*?(?=\.|$)",
        r"academy plus.*?(?=\.|$)",
        r"unacademy.*?(?=\.|$)",
    ]

    for pattern in patterns:
        text = re.sub(
            pattern,
            "",
            text,
            flags=re.IGNORECASE,
        )

    return text.strip()