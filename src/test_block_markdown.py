import unittest

from block_markdown import BlockType, markdown_to_blocks, block_to_block_type, markdown_to_html_node


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_multiple_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        ) 


    # def test_block_to_block_type_paragraph(self):
    #     md = "hello world"
    #     self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    # def test_block_to_block_type_heading_one(self):
    #     md = "# hello world"
    #     self.assertEqual(block_to_block_type(md), BlockType.HEADING)
    
    # def test_block_to_block_type_heading_two(self):
    #     md = "## hello world"
    #     self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    # def test_block_to_block_type_heading_two(self):
    #     md = "### hello world"
    #     self.assertEqual(block_to_block_type(md), BlockType.HEADING)
    
#     def test_block_to_block_type_code(self):
#         md = "```print('hello world')```"
#         self.assertEqual(block_to_block_type(md), BlockType.CODE)

#     def test_block_to_block_type_code_multiline(self):
#         md = """```
# print('hello world')
# print('hello world')
# print('hello world')
# ```
# """
#         self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
# Hello World
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Hello World</h1></div>"
        )

    def test_heading_with_inline(self):
        md = """
# **Hello** _World_
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1><b>Hello</b> <i>World</i></h1></div>"
        )

    def test_quote(self):
        md = """
> This is a quote
> with **bold** and _italic_ text
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with <b>bold</b> and <i>italic</i> text</blockquote></div>",
        )


    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )


if __name__ == "__main__":
    unittest.main()