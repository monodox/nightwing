"""CLI entry point for Nightwing."""

import typer

from nightwing.config import get_settings

app = typer.Typer(help="Nightwing forensic assistant CLI")


@app.command()
def run(case_id: str = typer.Option("demo-case", help="Case identifier")) -> None:
    """Run a basic Nightwing workflow placeholder."""
    settings = get_settings()
    typer.echo(f"Nightwing started for {case_id}")
    typer.echo(f"Evidence path: {settings.evidence_path}")


if __name__ == "__main__":
    app()
