import typer
from rich import print

from scholaros.transcripts.provider import TranscriptProvider
from scholaros.youtube.cleaner import clean_transcript
from scholaros.generators.notes import generate_notes
from scholaros.storage.vault import save_note

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
    """
    Ingest a YouTube video and save notes.
    """

    print("[yellow]Downloading transcript...[/yellow]")

    provider = TranscriptProvider()
    text = provider.get(url)
    text = clean_transcript(text)

    print("[cyan]Generating notes...[/cyan]")

    notes = generate_notes(text)

    save_path = save_note(
        subject,
        lecture,
        notes,
    )

    print(f"[bold green]Saved:[/bold green] {save_path}")


if __name__ == "__main__":
    app()