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
