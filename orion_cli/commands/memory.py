"""Memory commands for Orion long-term memory operations."""

import typer

app = typer.Typer(help="Inspect and debug long-term memory stores.")


@app.command()
def recall(query: str = typer.Argument(..., help="Text to recall from memory.")) -> None:
    """Stub command to recall related memory entries."""
    typer.echo(f"Memory recall for '{query}' is not yet implemented.")


@app.command()
def stats() -> None:
    """Stub command to show memory statistics."""
    typer.echo("Memory statistics are not yet implemented.")
