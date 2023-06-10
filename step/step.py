from dataclasses import dataclass
from pathlib import Path
from typing import List, Any, Callable

from markdown_it import MarkdownIt
from markdown_it.tree import SyntaxTreeNode


@dataclass
class Step:
    title: str
    description: str
    sub_steps: List[Any]  # to handle the lack of self
    function: Callable = lambda x: x


def break_by_headings(node_list):
    headings = []
    buffer = []

    # break by headings
    for child in node_list:
        if child.type == "heading" and buffer:
            headings.append(buffer)
            buffer = []
        buffer.append(child)
    if buffer:
        headings.append(buffer)
    return headings


def cli_name_and_description(first_head):
    name = "CLI Name"
    description = "Add a nice description here"
    if first_head:
        name = get_text_from_children(first_head[0])
        description = get_text_from_children(first_head[1])
    return name, description


def tree_to_steps(heading):
    pass


def from_markdown_to_steps(markdown_filepath: Path):
    md = MarkdownIt("commonmark").enable("strikethrough")
    tokens = md.parse(markdown_filepath.read_text())

    node = SyntaxTreeNode(tokens)
    headings = break_by_headings(node.children)
    first_head = headings.pop()
    name, description = cli_name_and_description(first_head)
    checklist = []
    for heading in headings:
        # TODO for each heading, a step
        tree_to_steps(heading)  # FIXME

    return name, description, checklist


def get_text_from_children(node, content=None, children=None):
    if content is None:
        content = ""
    if children is None:
        children = []
    if node.is_root:
        return ""

    children.extend(node.children)
    if children:
        child = children.pop()
        if child.type == "inline":
            content += child.content
        return get_text_from_children(child, content, children)
    return content


def generate_cli_from(cli_name: str, markdown_filepath: Path):
    cli_path = Path(cli_name)
    name, description, checklist = from_markdown_to_steps(markdown_filepath)
    # TODO create python file
    return cli_path
