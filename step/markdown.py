from markdown_it.tree import SyntaxTreeNode

from step.step import Step, renderer, md


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
