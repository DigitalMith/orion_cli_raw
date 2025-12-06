"""Identity commands for Orion self-state management."""

import typer

app = typer.Typer(help="Manage identity, persona, and self-state artifacts.")


@app.command()
def show() -> None:
    """Display the current identity configuration (placeholder)."""
    typer.echo("Identity display is not yet implemented.")


@app.command()
def reset(confirm: bool = typer.Option(False, "--confirm", help="Confirm identity reset.")) -> None:
    """Reset identity artifacts to packaged defaults (placeholder)."""
    if not confirm:
        typer.echo("Use --confirm to proceed with identity reset.")
        raise typer.Exit(code=1)
    typer.echo("Identity reset is not yet implemented.")
