from pathlib import Path

from step.step import Step
from step.markdown import from_markdown_to_steps


expected_checklist = [
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
    ),
]


def test_convert_markdown_to_steps():
    markdown_filepath = Path.cwd() / "tests/fixtures/manual_deploy.md"
    expected_description = (
        "Currently, our deployment is executed by a human being.\n"
        "Fear not, this is a step-by-step to guide you through it.\n"
        "Ready?"
    )
    name, description, checklist = from_markdown_to_steps(markdown_filepath)

    assert name == "Deploy 🚀"
    assert description == expected_description
    assert len(checklist) == 2
    assert checklist == expected_checklist
