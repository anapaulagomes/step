from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, List

from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode
from mdformat.renderer import MDRenderer

from step.markdown import (
    get_text_from_children,
    convert_section_to_steps,
    break_by_headings,
)

md = MarkdownIt("commonmark").enable("strikethrough")
renderer = MDRenderer()


@dataclass
class Step:
    title: str
    description: str = ""
    sub_steps: List[Any] = field(default_factory=list)
    function: Callable = lambda x: x  # noqa


def cli_name_and_description(first_head):
    name = "CLI Name"
    description = "Add a nice description here"
    if first_head:
        name = get_text_from_children(first_head[0])
        description = get_text_from_children(first_head[1])
    return name, description


def from_markdown_to_steps(markdown_filepath: Path):
    tokens = md.parse(markdown_filepath.read_text())

    node = SyntaxTreeNode(tokens)
    sections = break_by_headings(node.children)
    first_head = sections.pop(0)
    name, description = cli_name_and_description(first_head)
    checklist = []
    for section in sections:
        checklist.append(convert_section_to_steps(section))

    return name, description, checklist


def generate_cli_from(cli_name: str, markdown_filepath: Path):
    cli_path = Path(cli_name)
    name, description, checklist = from_markdown_to_steps(markdown_filepath)
    # TODO create python file
    return cli_path
