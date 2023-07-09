import pprint
from pathlib import Path

import typer

from step.markdown import from_markdown_to_steps

app = typer.Typer()


class InvalidMethodName(Exception):
    pass


def convert_to_python_method_name(phrase):
    if not phrase:
        raise InvalidMethodName(f"Cannot convert it into a method name: {phrase}")

    phrase = phrase.lower().replace(" ", "_")
    only_alpha_numeric = "".join(
        [char for char in phrase if char.isalnum() or char == "_"]
    )

    if not only_alpha_numeric or only_alpha_numeric[0].isdigit():
        raise InvalidMethodName(
            f"Cannot convert it into a method name: {only_alpha_numeric}"
        )

    return only_alpha_numeric


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
        title = convert_to_python_method_name(step.title)
        command_template = Path("step/templates/command.py.template").read_text()
        command_template = command_template.replace("STEP_TITLE_HERE", title)
        command_template = command_template.replace(
            "STEP_DESCRIPTION_HERE", step.description
        )
        sub_steps_template = ""
        if step.sub_steps:
            pretty_sub_steps = pprint.pformat(step.sub_steps, indent=4)
            declaration = f"sub_steps = {pretty_sub_steps}"
            sub_steps_template = Path(
                "step/templates/sub_steps.py.template"
            ).read_text()
            sub_steps_template = sub_steps_template.replace(
                "STEP_SUB_STEPS_DECLARATION", declaration
            )
        command_template = command_template.replace(
            "STEP_SUB_STEPS", sub_steps_template
        )

        commands.append(command_template)

    commands = "\n\n".join(commands)
    cli_template = cli_template.replace("STEP_CHECKLIST_HERE", commands)
    cli_filepath.write_text(cli_template)

    return cli_filepath


@app.command()
def main(markdown_checklist: Path, cli_name: str = ""):
    filepath = generate_cli_from(cli_name, markdown_checklist)  # TODO generate cli
    typer.echo(f"Your CLI is available in: {filepath}.")


if __name__ == "__main__":
    app()
