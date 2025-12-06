# Orion CLI

A lightweight command-line interface for the Orion cognitive architecture. This skeleton provides the foundational structure for managing ingestion, memory, identity, and tooling workflows using Typer.

## Installation

```bash
pip install -e .
```

## Usage

Run the CLI root to explore available commands:

```bash
orion-cli --help
```

Examples:

```bash
# Inspect available ingest commands
orion-cli ingest --help

# Display configured workspace paths
orion-cli tools paths
```

## Project Layout

- `orion_cli/cli.py`: Typer application entrypoint.
- `orion_cli/commands/`: Command groups with placeholder implementations.
- `orion_cli/shared/`: Shared helpers for configuration, paths, embeddings, and memory primitives.
- `orion_cli/settings/`: Configuration loading utilities backed by Pydantic and YAML.
- `orion_cli/data/`: Packaged default templates and schema placeholders.
- `workspace/`: User workspace directory (ignored by git).

This initial structure is intentionally minimal and ready for future expansion.
