from enum import Enum

from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    markdown_blocks = markdown.split("\n\n")
    filtered_blocks = filter(lambda block: block != "", markdown_blocks)
    return list(map(lambda block: block.strip(), filtered_blocks))


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    # is_quote_block = all(line.startswith(">") for line in lines)
    # if is_quote_block:
    #     return BlockType.QUOTE

    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    # is_unordered_list = True
    # for line in lines:
    #     if not line.startswith("- "):
    #         is_unordered_list = False
    #         break
    
    # if is_unordered_list:
    #     return BlockType.UNORDERED_LIST

    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    
    # is_ordered_list = True
    # count = 1
    # for line in lines:
    #     if not line.startswith(f"{count}. "):
    #         is_ordered_list = False
    #         break
    #     count += 1
    
    # if is_ordered_list:
    #     return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes


def paragraph_to_html_node(block: str) -> ParentNode:
    children = text_to_children(block.replace("\n", " "))
    return ParentNode("p", children)


def heading_to_html_node(block: str) -> ParentNode:
    level = 0
    while block[level] == "#":
        level += 1

    children = text_to_children(block[level+1:])
    return ParentNode(f"h{level}", children)


def codeblock_to_html_node(block: str) -> ParentNode:
    text_node = TextNode(block[4:-3], TextType.CODE)
    html_node = text_node_to_html_node(text_node)
    return ParentNode("pre", [html_node])


def list_to_html_node(block: str, tag: str) -> ParentNode:
    # list_items = []
    # for line in block.split("\n"):
    pass



def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                nodes.append(paragraph_to_html_node(block))
            case BlockType.HEADING:
                nodes.append(heading_to_html_node(block))
            case BlockType.CODE:
                nodes.append(codeblock_to_html_node(block))
            case BlockType.QUOTE:
                lines = block.split("\n")
                clean_lines = list(map(lambda l: l[2:] if len(l) > 1 and l[1] == " " else l[1:], lines))
                children = text_to_children(" ".join(clean_lines))
                nodes.append(ParentNode("blockquote", children))
            case BlockType.UNORDERED_LIST:
                lines = block.split("\n")
                clean_lines = list(map(lambda l: l[2:] if len(l) > 1 and l[1] == " " else l[1:], lines))
                list_nodes = []
                for line in clean_lines:
                    children = text_to_children(line)
                    list_nodes.append(ParentNode("li", children))
                nodes.append(ParentNode("ul", list_nodes))
            case BlockType.ORDERED_LIST:
                lines = block.split("\n")
                clean_lines = list(map(lambda l: l[2:] if len(l) > 1 and l[1] == " " else l[1:], lines))
                list_nodes = []
                for line in clean_lines:
                    children = text_to_children(line)
                    list_nodes.append(ParentNode("li", children))
                nodes.append(ParentNode("ol", list_nodes))
            case _:
                raise ValueError("invalid block type")

    root = ParentNode("div", nodes)
    return root


if __name__ == "__main__":
    md = """
# Hello World
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print("XD", html)
        