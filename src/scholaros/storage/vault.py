from pathlib import Path

# Change this later to your actual Obsidian vault
VAULT_PATH = Path.home() / "Documents" / "ScholarOSVault"


def ensure_vault():
    VAULT_PATH.mkdir(parents=True, exist_ok=True)


def list_subjects():
    ensure_vault()
    return sorted([p.name for p in VAULT_PATH.iterdir() if p.is_dir()])


def create_subject(name: str):
    subject_path = VAULT_PATH / name
    subject_path.mkdir(parents=True, exist_ok=True)
    return subject_path


def save_note(subject: str, title: str, content: str):
    subject_path = create_subject(subject)

    # Make filename filesystem-safe
    safe_title = "".join(
        c for c in title if c not in r'<>:"/\|?*'
    ).strip()

    note_path = subject_path / f"{safe_title}.md"

    note_path.write_text(content, encoding="utf-8")

    return note_path