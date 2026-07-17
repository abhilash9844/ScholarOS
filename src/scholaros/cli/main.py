import typer
from rich import print
from scholaros.storage.cache import ensure_cache

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

    provider = TranscriptProvider()

    transcript = provider.get(url)

    transcript = clean_transcript(transcript)

    print("[cyan]Generating Concept Inventory...[/cyan]")

    concepts = generate_concepts(transcript)

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