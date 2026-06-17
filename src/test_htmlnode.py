import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_empty_props_to_html(self):
        node = HTMLNode("p", "This is a html node")
        return self.assertEqual(
            "",
            node.props_to_html()
        )
    
    def test_one_prop_to_html(self):
        node = HTMLNode("p", "This is a html node", None, {"href": "https://www.google.com",})
        return self.assertEqual(
            " href=\"https://www.google.com\"",
            node.props_to_html()
        )
    
    def test_two_props_to_html(self):
        node = HTMLNode("p", "This is a html node", None, {
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        return self.assertEqual(
            " href=\"https://www.google.com\" target=\"_blank\"",
            node.props_to_html()
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
    
    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Just a container", {"styles": "background: red"})
        self.assertEqual(node.to_html(), "<div styles=\"background: red\">Just a container</div>")


if __name__ == "__main__":
    unittest.main()