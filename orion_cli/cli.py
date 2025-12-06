"""Typer application entrypoint for Orion CLI."""

import typer

from orion_cli.commands import identity_app, ingest_app, memory_app, tools_app
from orion_cli.shared.config import load_config

app = typer.Typer(help="Orion CLI for managing ingestion, memory, and identity workflows.")


@app.callback()
def main() -> None:
    """Initialize configuration on startup."""

    # Preload configuration to surface errors early. In future phases, inject into commands.
    load_config()


app.add_typer(ingest_app, name="ingest", help="Ingestion-related commands.")
app.add_typer(memory_app, name="memory", help="Memory management commands.")
app.add_typer(identity_app, name="identity", help="Identity management commands.")
app.add_typer(tools_app, name="tools", help="Maintenance and utility commands.")


if __name__ == "__main__":
    app()
