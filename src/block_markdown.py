from enum import Enum


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


