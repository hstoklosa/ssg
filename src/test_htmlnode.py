import unittest

from htmlnode import HTMLNode


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