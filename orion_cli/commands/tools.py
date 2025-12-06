"""Utility and maintenance commands."""

import typer

from orion_cli.shared.paths import OrionPaths

app = typer.Typer(help="Maintenance and debugging tools.")


@app.command()
def paths() -> None:
    """Show resolved workspace-related paths."""

    orion_paths = OrionPaths()
    orion_paths.ensure_workspace()
    for label, path in orion_paths.path_summary().items():
        typer.echo(f"{label}: {path}")


@app.command()
def health() -> None:
    """Simple health check placeholder."""

    typer.echo("Orion CLI is initialized. Detailed diagnostics are not yet implemented.")
