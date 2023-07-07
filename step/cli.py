from pathlib import Path

import typer

from step.markdown import from_markdown_to_steps

app = typer.Typer()


def generate_cli_from(cli_name: str, markdown_filepath: Path):
    cli_path = Path(cli_name)
    name, description, checklist = from_markdown_to_steps(markdown_filepath)
    # TODO create python file
    return cli_path


@app.command()
def main(cli_name: str, markdown_checklist: Path):
    filepath = generate_cli_from(cli_name, markdown_checklist)  # TODO generate cli
    typer.echo(f"Your CLI is available in: {filepath}.")


if __name__ == "__main__":
    app()
