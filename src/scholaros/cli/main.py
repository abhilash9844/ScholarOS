import typer
from rich import print

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
def ingest(url: str):
    """Ingest a YouTube video."""
    print(f"[green]URL:[/green] {url}")
    print("[yellow]Ingest pipeline started...[/yellow]")


if __name__ == "__main__":
    app()