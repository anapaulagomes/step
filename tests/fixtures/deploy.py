import typer
from rich.prompt import Prompt

"""
Notes:

name of the file -> h1 of markdown
text of intro -> text just after h1
commands -> h2 of markdown
"""

app = typer.Typer()
steps = {
    "Pull the code from the main branch" : [],
    "Configure the environment": [
        "Configure the environment variables in the .env file",
        "Install the dependencies with: `pip install -r requirements.txt`",
        "Run the migrations: `python manage.py migrate`",
    ],
    "Done!": []
}  # TODO ordered dict


@app.command()
def checklist():
    for step, substeps in steps.items():
        typer.echo(step)
        for substep in substeps:
           typer.echo(f"-- {substep}")
        # if confirmation:
        #     print("Done, onto the next!")
        # else:
        #     break
        confirmation = Prompt.ask("Continue? (y/n/s)")
        if confirmation.lower() == "y":
            typer.echo(":checked: ✅")
        elif confirmation.lower() == "n":
            raise typer.Exit()
        else:
            typer.echo("⏭")


@app.command()
def after_deploy():
    print("After the deploy don't forget about notifying people in the team's Slack channel.")


if __name__ == "__main__":
    typer.echo("Deploy")  # TODO text before h2
    app()
