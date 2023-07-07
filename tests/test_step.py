from pathlib import Path

from step.step import from_markdown_to_steps


def test_convert_markdown_to_steps():
    markdown_filepath = Path.cwd() / "tests/fixtures/manual_deploy.md"
    expected_description = (
        "Currently, our deployment is executed by a human being.\n"
        "Fear not, this is a step-by-step to guide you through it.\n"
        "Ready?"
    )
    expected_step_description = (
        "After the deployment don't forget about notifying people in "
        "the team's Slack channel."
    )
    # nested code is rendered as HTML
    expected_html = (
        "<li>\n"
        "<p>Configure the environment</p>\n"
        "<ol>\n"
        "<li>Configure the environment variables in the <code>.env</code> file</li>\n"
        "<li>Install the dependencies with:</li>\n"
        "</ol>\n"
        '<pre><code class="language-bash">pip install -r requirements.txt\n'
        "</code></pre>\n"
        "</li>\n"
    )

    name, description, checklist = from_markdown_to_steps(markdown_filepath)

    assert name == "Deploy 🚀"
    assert description == expected_description
    assert len(checklist) == 2
    assert checklist[0].title == "Checklist"
    assert checklist[0].description == ""
    assert len(checklist[0].sub_steps) == 4
    assert checklist[0].sub_steps[1].description == expected_html
    assert checklist[1].title == "After deploy"
    assert checklist[1].description == expected_step_description
    assert checklist[1].sub_steps == []
