from pathlib import Path

VOCAB = (
    Path(__file__).parent.parent.parent.parent
    / "data"
    / "vocab"
    / "coa.txt"
)


def extract_terms(transcript: str) -> list[str]:
    text = transcript.lower()

    vocab = [
        line.strip()
        for line in VOCAB.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    found = []

    for term in vocab:
        if term.lower() in text:
            found.append(term)

    print("\n========== VOCAB ==========")
    print(VOCAB)
    print("\n========== FOUND TERMS ==========")
    print(found)
    print("=================================\n")

    return found