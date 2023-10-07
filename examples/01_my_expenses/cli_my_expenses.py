from step.step import Step
from step.external_cli import handle_sub_steps

import typer


app = typer.Typer()


@app.command()
def retrieving_the_data():
    typer.echo(
        """

    """
    )
    sub_steps = [
        Step(
            title="Go to https://mybrazilianbank.br and download data from the "
            "last month",
            description="Go to https://mybrazilianbank.br and download data from "
            "the last month\n",
            sub_steps=[],
        ),
        Step(
            title="Go to https://mygermanbank.de and download data from the last "
            "month",
            description="Go to https://mygermanbank.de and download data from the "
            "last month\n",
            sub_steps=[],
        ),
    ]
    handle_sub_steps(sub_steps)


@app.command()
def parse_the_data():
    typer.echo(
        """

    """
    )
    sub_steps = [
        Step(
            title="Get a quote from **BRL** to **EUR**",
            description="Get a quote from **BRL** to **EUR**\n",
            sub_steps=[],
        ),
        Step(
            title="Run the script that puts everything in one format",
            description="Run the script that puts everything in one format\n",
            sub_steps=[],
        ),
        Step(
            title="The data generated in the previous step should be moved to "
            "`~/workspace/my-expenses`",
            description="The data generated in the previous step should be moved "
            "to `~/workspace/my-expenses`\n",
            sub_steps=[],
        ),
    ]
    handle_sub_steps(sub_steps)


@app.command()
def generate_the_report():
    typer.echo(
        """
    Well done!
    """
    )


if __name__ == "__main__":
    typer.secho("My expenses", fg=typer.colors.BRIGHT_BLACK)
    typer.secho(
        """
    This is a step by step on how to retrieve data from
my banks and generate a report with it.""",
        fg=typer.colors.BRIGHT_BLACK,
    )
    app()
