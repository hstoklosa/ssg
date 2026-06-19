import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_nodes = []
        text_sections = node.text.split(delimiter)
        n = len(text_sections)

        if n % 2 == 0:
            raise Exception("a matching closing delimiter is missing")
        
        for i in range(n):
            curr_section = text_sections[i]

            if curr_section == "":
                continue

            if i % 2 == 0:
                split_nodes.append(TextNode(curr_section, TextType.TEXT, node.url))
            else:
                split_nodes.append(TextNode(curr_section, text_type, node.url))

        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


# if __name__ == "__main__":
#     text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
#     res = extract_markdown_links(
#         text
#     )
#     print(res)