from pathlib import Path

CACHE = Path(".cache")

TRANSCRIPTS = CACHE / "transcripts"
CONCEPTS = CACHE / "concepts"
NOTES = CACHE / "notes"


def ensure_cache():
    TRANSCRIPTS.mkdir(parents=True, exist_ok=True)
    CONCEPTS.mkdir(parents=True, exist_ok=True)
    NOTES.mkdir(parents=True, exist_ok=True)