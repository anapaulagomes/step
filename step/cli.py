from pathlib import Path

import typer

from step.step import from_markdown_to_steps, generate_cli_from

app = typer.Typer()


@app.command()
def main(cli_name: str, markdown_checklist: Path):
    filepath = generate_cli_from(cli_name, markdown_checklist)  # TODO generate cli
    typer.echo(f"Your CLI is available in: {filepath}.")


if __name__ == "__main__":
    app()
