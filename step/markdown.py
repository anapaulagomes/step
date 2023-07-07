from pathlib import Path

from markdown_it.tree import SyntaxTreeNode
from markdown_it import MarkdownIt
from mdformat.renderer import MDRenderer

from step.step import Step

md = MarkdownIt("commonmark").enable("strikethrough")
renderer = MDRenderer()


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


def convert_section_to_steps(section):
    data = {}
    sub_steps = []

    for item in section:
        if item.tag in ["h1", "h2"]:
            data["title"] = retrieve_content_from_tree(item)
        elif item.tag in ["ol", "ul"]:
            # list of list_item - substeps
            for child in item.children:
                markdown = extract_markdown_from_subtree(child)
                # it would be nice to have the original Markdown code here
                # by now, we can work with HTML in the description
                sub_steps.append(
                    Step(
                        title=retrieve_content_from_tree(child),
                        description=markdown,
                    )
                )
            data["sub_steps"] = sub_steps
        else:
            data["description"] = retrieve_content_from_tree(item)
    return Step(**data)


def extract_markdown_from_subtree(node):
    # make it a tree first
    node.token, node.nester_tokens = None, []
    return renderer.render(node.to_tokens(), md.options, {})


def retrieve_content_from_tree(node: SyntaxTreeNode, content: str = ""):
    if node.type == "inline":
        content += node.content

    if not node.children:
        return content

    for child in node.children:
        return retrieve_content_from_tree(child, content)


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


def cli_name_and_description(first_head):
    name = "CLI Name"
    description = "Add a nice description here"
    if first_head:
        name = get_text_from_children(first_head[0])
        description = get_text_from_children(first_head[1])
    return name, description
