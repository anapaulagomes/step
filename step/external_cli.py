import typer
from rich.prompt import Prompt


def confirmation_to_emoji():
    confirmation = Prompt.ask("Completed?", choices=["y", "n", "s", "q"], default="y")

    if confirmation.lower() == "y":
        return "✅"
    elif confirmation.lower() == "n":
        return "❌"
    elif confirmation.lower() == "s":
        return "⏭️"
    elif confirmation.lower() == "q":
        raise typer.Exit()


def handle_substeps(sub_steps):
    for number, step in enumerate(sub_steps, start=1):
        number_of_sub_steps = len(step.sub_steps)
        message_number_of_sub_steps = (
            f"({number_of_sub_steps} sub_steps)" if number_of_sub_steps else ""
        )

        typer.secho(f"{number}. {step.title} {message_number_of_sub_steps}", bold=True)
        for sub_step in step.sub_steps:
            typer.echo(f"-- {sub_step.title}")
            typer.echo(confirmation_to_emoji())
        else:
            typer.echo(confirmation_to_emoji())
