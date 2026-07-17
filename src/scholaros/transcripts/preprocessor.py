import re

NOISE_PATTERNS = [
    r"\bsubscribe\b",
    r"\blike and share\b",
    r"\bpress the bell\b",
    r"\btelegram\b",
    r"\bdiscount\b",
    r"\bscholarship\b",
    r"\bacademy plus\b",
]


def preprocess(text: str) -> str:
    cleaned = text

    for pattern in NOISE_PATTERNS:
        cleaned = re.sub(
            pattern,
            "",
            cleaned,
            flags=re.IGNORECASE,
        )

    cleaned = re.sub(
        r"\s+",
        " ",
        cleaned,
    )

    return cleaned.strip()