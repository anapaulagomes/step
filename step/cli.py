# import pprint
from pathlib import Path

import typer

from step.markdown import from_markdown_to_steps

app = typer.Typer()


def generate_cli_from(cli_name: str, markdown_filepath: Path):
    name, description, checklist = from_markdown_to_steps(markdown_filepath)
    if not cli_name:
        cli_name = name

    cli_template = Path("step/templates/cli.py.template").read_text()
    cli_template = cli_template.replace("STEP_NAME_HERE", cli_name)
    cli_template = cli_template.replace("STEP_DESCRIPTION_HERE", description)

    cli_filepath = (
        markdown_filepath.parent / f"cli_{cli_name.lower().replace(' ', '_')}.py"
    )

    commands = []
    for step in checklist:
        title = step.title.lower().replace(
            " ", "_"
        )  # TODO make sure it is valid python
        command_template = Path("step/templates/command.py.template").read_text()
        command_template = command_template.replace("STEP_TITLE_HERE", title)
        command_template = command_template.replace(
            "STEP_DESCRIPTION_HERE", step.description
        )
        commands.append(command_template)
        # TODO add sub_steps (STEP_SUB_STEPS)
        # FIXME deal with break lines from markdown

    # pretty_commands = pprint.pformat(commands, indent=4)
    cli_template = cli_template.replace("STEP_CHECKLIST_HERE", "\n\n".join(commands))
    cli_filepath.write_text(cli_template)

    return cli_filepath


@app.command()
def main(markdown_checklist: Path, cli_name: str = ""):
    filepath = generate_cli_from(cli_name, markdown_checklist)  # TODO generate cli
    typer.echo(f"Your CLI is available in: {filepath}.")


if __name__ == "__main__":
    app()
