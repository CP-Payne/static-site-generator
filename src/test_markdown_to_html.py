import unittest
from htmlnode import *

class TestMarkdownToHTML(unittest.TestCase):

    def test_paragraph(self):
        node = block_to_html_node("This is a simple paragraph.", block_type_paragraph)
        self.assertEqual(node.to_html(), "<p>This is a simple paragraph.</p>")

    def test_heading(self):
        node = block_to_html_node("# Heading", block_type_heading)
        self.assertEqual(node.to_html(), "<h1>Heading</h1>")

    def test_list(self):
        block = "* Item 1\n* Item 2"
        node = block_to_html_node(block, block_type_unordered_list)
        self.assertEqual(node.to_html(), "<ul><li>Item 1</li><li>Item 2</li></ul>")

    def test_quote(self):
        node = block_to_html_node("> This is a quote", block_type_quote)
        self.assertEqual(node.to_html(), "<blockquote><p>This is a quote</p></blockquote>")

if __name__ == "__main__":
    unittest.main()