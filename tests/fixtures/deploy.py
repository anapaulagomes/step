import typer
from rich.prompt import Prompt

from step.step import Step

app = typer.Typer()

# TODO generate this from a markdown file
steps = [
    Step(
        title="Pull the code from the main branch",
        description="",
        sub_steps=[],
    ),
    Step(
        title="Configure the environment",
        description="",
        sub_steps=[
            Step(
                title="Configure the environment variables in the `.env` file",
                description="",
                sub_steps=[],
            ),
            Step(
                title="Install the dependencies with...",
                description="...",
                sub_steps=[],
            ),
        ],
    ),
    Step(
        title="Run the migrations: `python manage.py migrate`",
        description="",
        sub_steps=[],
    ),
    Step(
        title="Done!",
        description="",
        sub_steps=[],
    ),
]


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


@app.command()
def checklist():
    for number, step in enumerate(steps, start=1):
        number_of_sub_steps = len(step.sub_steps)
        message_number_of_sub_steps = (
            f"({number_of_sub_steps} sub_steps)" if number_of_sub_steps else ""
        )

        typer.secho(f"{number}. {step.title} {message_number_of_sub_steps}", bold=True)
        for sub_step in step.sub_steps:
            typer.echo(f"-- {sub_step.title}")
            # TODO implement nested options
            typer.echo(confirmation_to_emoji())
        else:
            typer.echo(confirmation_to_emoji())


@app.command()
def after_deploy():
    print(
        "After the deploy don't forget about notifying people "
        "in the team's Slack channel."
    )


if __name__ == "__main__":
    typer.secho("--- Deploy ---", fg=typer.colors.BRIGHT_BLACK)  # TODO text before h2
    app()
