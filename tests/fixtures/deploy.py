import typer

from rich.prompt import Prompt

"""
Notes:

name of the file -> h1 of markdown
text of intro -> text just after h1
commands -> h2 of markdown
"""

# from rich.console import Console
# from rich.markdown import Markdown
# from pathlib import Path
# console = Console()
# md = Markdown(Path("tests/fixtures/manual_deploy.md").read_text())
# console.print(md)

app = typer.Typer()
steps = {
    "1. Pull the code from the main branch": {
        "steps": [],
        "done": ""
    },
    "2. Configure the environment": {
        "steps": [
            "Configure the environment variables in the .env file",
            "Install the dependencies with: `pip install -r requirements.txt`",
            "Run the migrations: `python manage.py migrate`"
        ],
        "done": ""
    },
    "3. Done!": {
        "steps": [],
        "done": ""
    }
}  # TODO ordered dict


def confirmation_to_emoji():
    confirmation = Prompt.ask("Done?", choices=["y", "n", "s", "q"], default="y")

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
    for step, info in steps.items():
        typer.secho(f"{step} ({len(info['steps'])} steps)", fg=typer.colors.BLUE)
        for substep in info["steps"]:
            typer.echo(f"-- {substep}")
            typer.echo(confirmation_to_emoji())
        else:
            typer.echo(confirmation_to_emoji())


@app.command()
def after_deploy():
    print("After the deploy don't forget about notifying people in the team's Slack channel.")


if __name__ == "__main__":
    typer.secho("--- Deploy ---", fg=typer.colors.BRIGHT_BLACK)  # TODO text before h2
    app()
