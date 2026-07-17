import typer
from rich import print
from scholaros.transcripts.preprocessor import preprocess
from scholaros.storage.cache import ensure_cache
from scholaros.extraction.technical_terms import extract_terms
from scholaros.transcripts.provider import TranscriptProvider
from scholaros.youtube.cleaner import clean_transcript

from scholaros.generators.concepts import generate_concepts
from scholaros.generators.notes import generate_notes

from scholaros.storage.vault import save_document

app = typer.Typer(
    help="ScholarOS - AI Powered Learning Platform"
)


@app.command()
def version():
    print("[bold green]ScholarOS v0.1.0[/bold green]")


@app.command()
def hello():
    print("[bold cyan]ScholarOS is working![/bold cyan]")


@app.command()
def ingest(
    url: str,
    subject: str,
    lecture: str,
):
    """Ingest a YouTube lecture."""
    ensure_cache()

    print("[yellow]Downloading transcript...[/yellow]")

    from pathlib import Path

    transcript = Path(
       "sample_data/lecture01.txt"
         ).read_text(
          encoding="utf-8"
)

    transcript = clean_transcript(transcript)

    transcript = preprocess(transcript)
    print("\n========== CLEANED TRANSCRIPT ==========\n")
    print(transcript[:3000])
    print("\n========================================\n")

    print("[cyan]Generating Concept Inventory...[/cyan]")

    terms = "\n".join(
    extract_terms(transcript)
)

    concepts = generate_concepts(terms)

    save_document(
        subject,
        lecture,
        "01 - Concept Inventory",
        concepts,
    )

    print("[cyan]Generating Elite Notes...[/cyan]")

    notes = generate_notes(transcript)

    save_document(
        subject,
        lecture,
        "02 - Elite Notes",
        notes,
    )

    print()
    print("[bold green]Knowledge Object Created Successfully![/bold green]")


if __name__ == "__main__":
    app()