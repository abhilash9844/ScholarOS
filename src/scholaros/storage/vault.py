from pathlib import Path

VAULT_PATH = Path.home() / "Documents" / "ScholarOSVault"


def ensure_vault():
    VAULT_PATH.mkdir(parents=True, exist_ok=True)


def list_subjects():
    ensure_vault()
    return sorted(
        p.name for p in VAULT_PATH.iterdir()
        if p.is_dir()
    )


def create_subject(name: str):
    path = VAULT_PATH / name
    path.mkdir(parents=True, exist_ok=True)
    return path


def create_lecture(subject: str, lecture: str):
    subject_path = create_subject(subject)

    lecture_path = subject_path / lecture

    lecture_path.mkdir(
        parents=True,
        exist_ok=True,
    )

    return lecture_path


def save_document(
    subject: str,
    lecture: str,
    filename: str,
    content: str,
):
    lecture_path = create_lecture(
        subject,
        lecture,
    )

    safe_name = "".join(
        c for c in filename
        if c not in r'<>:"/\|?*'
    ).strip()

    path = lecture_path / f"{safe_name}.md"

    path.write_text(
        content,
        encoding="utf-8",
    )

    return path