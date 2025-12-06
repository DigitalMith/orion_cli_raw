"""Ingestion commands for Orion data flows."""

import typer

app = typer.Typer(help="Manage ingestion pipelines and source material.")


@app.command()
def sources() -> None:
    """List configured ingestion sources (placeholder)."""
    typer.echo("Listing ingestion sources is not yet implemented.")


@app.command()
def run(source: str = typer.Argument(..., help="Source identifier to ingest.")) -> None:
    """Execute an ingestion run for the specified source (placeholder)."""
    typer.echo(f"Ingestion run for '{source}' is not yet implemented.")
