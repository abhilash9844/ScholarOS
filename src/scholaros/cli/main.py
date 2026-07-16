import typer
from rich import print

from scholaros.transcripts.provider import TranscriptProvider
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
):
    """Ingest a YouTube video."""

    print("[yellow]Downloading transcript...[/yellow]")

    provider = TranscriptProvider()

    text = provider.get(url)

    print("[cyan]Generating notes...[/cyan]")

    notes = generate_notes(text)

    save_path = save_note(
        subject,
        "Lecture Notes",
        notes,
    )

    print(f"[bold green]Saved:[/bold green] {save_path}")


if __name__ == "__main__":
    app()