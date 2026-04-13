"""CLI entry point for Nightwing investigations."""

from __future__ import annotations

import typer
from rich.console import Console

from nightwing.agents.graph import run_case
from nightwing.config import get_settings

app = typer.Typer(help="Nightwing autonomous incident response CLI")
console = Console()


@app.callback()
def main() -> None:
    """Nightwing command group."""


@app.command()
def run(
    case_id: str = typer.Option("demo-case", help="Case identifier"),
    evidence_path: str | None = typer.Option(
        None, help="Override the configured evidence directory."
    ),
) -> None:
    """Run the full Nightwing evidence pipeline."""

    settings = get_settings()
    target_evidence = evidence_path or str(settings.evidence_path)
    state = run_case(case_id=case_id, evidence_root=target_evidence)

    console.print(f"[bold]Case:[/bold] {state.case_id}")
    console.print(f"[bold]Artifacts:[/bold] {len(state.evidence)}")
    console.print(f"[bold]Findings:[/bold] {len(state.findings)}")
    console.print(f"[bold]Report:[/bold] {state.report_markdown_path}")
    console.print(f"[bold]JSON:[/bold] {state.report_json_path}")


if __name__ == "__main__":
    app()
