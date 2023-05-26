import typer
from typing_extensions import Annotated


"""
Notes:

name of the file -> h1 of markdown
text of intro -> text just after h1
commands -> h2 of markdown
"""

app = typer.Typer()
Confirmation = Annotated[
    bool, typer.Option(prompt="Was this step executed?")
]
steps = {
    "Pull the code from the main branch" : [],
    "Configure the environment": [
        "Configure the environment variables in the .env file",
        "Install the dependencies with: `pip install -r requirements.txt`",
        "Run the migrations: `python manage.py migrate`",
        "Done!"
    ]
}  # TODO ordered dict


@app.command()
def checklist(confirmation: Confirmation):
    for step, substeps in steps.items():
        print(step)
        for substep in substeps:
           print(f"-- {substep}")
        # if confirmation:
        #     print("Done, onto the next!")
        # else:
        #     break
        print("\n")


@app.command()
def after_deploy(confirmation: Confirmation):
    print("After the deploy don't forget about notifying people in the team's Slack channel.")


if __name__ == "__main__":
    print("Deploy")  # TODO text before h2
    app()
