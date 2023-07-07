import typer

from step.external_cli import handle_substeps
from step.step import Step

app = typer.Typer()


steps = [
    Step(
        title="Checklist",
        description="",
        sub_steps=[
            Step(
                title="Pull the code from the `main` branch\n"
                "from the main project repo",
                description="Pull the code from the `main` branch\n"
                "from the main project repo\n",
                sub_steps=[],
            ),
            Step(
                title="Configure the environment",
                description="Configure the environment\n"
                "\n"
                "1. Configure the environment variables in "
                "the `.env` file\n"
                "1. Install the dependencies with:\n"
                "\n"
                "```bash\n"
                "pip install -r requirements.txt\n"
                "```\n",
                sub_steps=[],
            ),
            Step(
                title="Run the migrations: `python manage.py migrate`",
                description="Run the migrations: `python manage.py " "migrate`\n",
                sub_steps=[],
            ),
            Step(title="Done!", description="Done!\n", sub_steps=[]),
        ],
    ),
    Step(
        title="After deploy",
        description="After the deployment don't forget about notifying people in "
        "the team's Slack channel.",
        sub_steps=[],
        # function= # you can add a callback in any step
    ),
]


@app.command()
def checklist():
    typer.echo("")
    sub_steps = [
        Step(
            title="Pull the code from the `main` branch\n" "from the main project repo",
            description="Pull the code from the `main` branch\n"
            "from the main project repo\n",
            sub_steps=[],
        ),
        Step(
            title="Configure the environment",
            description="Configure the environment\n"
            "\n"
            "1. Configure the environment variables in "
            "the `.env` file\n"
            "1. Install the dependencies with:\n"
            "\n"
            "```bash\n"
            "pip install -r requirements.txt\n"
            "```\n",
            sub_steps=[],
        ),
        Step(
            title="Run the migrations: `python manage.py migrate`",
            description="Run the migrations: `python manage.py " "migrate`\n",
            sub_steps=[],
        ),
        Step(title="Done!", description="Done!\n", sub_steps=[]),
    ]
    handle_substeps(sub_steps)


@app.command()
def after_deploy():
    typer.echo(
        "After the deploy don't forget about notifying people "
        "in the team's Slack channel."
    )


if __name__ == "__main__":
    typer.secho("Deploy 🚀", fg=typer.colors.BRIGHT_BLACK)
    typer.echo(
        "Currently, our deployment is executed by a human being.\Fear not, this is a step-by-step to guide you through it.\nReady?"
    )
    app()
