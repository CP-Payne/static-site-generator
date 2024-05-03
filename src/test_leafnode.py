import unittest
from htmlnode import LeafNode, text_node_to_html_node
from textnode import TextNode


class TestLeafNode(unittest.TestCase):

    def test_valid_html(self):
        node = LeafNode(value="Hello", tag="p", props={"class": "text"})
        expected = '<p class="text">Hello</p>'
        self.assertEqual(node.to_html(), expected)

    def test_empty_value(self):
        with self.assertRaises(ValueError):
            LeafNode(value="", tag=None).to_html()
        with self.assertRaises(ValueError):
            LeafNode(value=None, tag=None).to_html()

    def test_missing_tag(self):
        node = LeafNode(value="Content", tag=None)
        expected = 'Content'
        self.assertEqual(node.to_html(), expected)

    def test_no_props(self):
        node = LeafNode(value="Content", tag="span", props=None)
        expected = '<span>Content</span>'
        self.assertEqual(node.to_html(), expected)

    def test_empty_props(self):
        node = LeafNode(value="Content", tag="div", props={})
        expected = '<div>Content</div>'
        self.assertEqual(node.to_html(), expected)

    # TEXTNODE TO HTMLNODE

    def test_text_node(self):
        node = TextNode("Sample Text", "text")
        expected = LeafNode(tag= None, value="Sample Text")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_bold_node(self):
        node = TextNode("Bold Text", "bold")
        expected = LeafNode(tag="b", value="Bold Text")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_italic_node(self):
        node = TextNode("Italic Text", "italic")
        expected = LeafNode(tag="i", value="Italic Text")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_code_node(self):
        node = TextNode("Code Snippet", "code")
        expected = LeafNode(tag="code", value="Code Snippet")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_link_node(self):
        node = TextNode("Link Text", "link", url="http://example.com")
        expected = LeafNode(tag="a", value="Link Text", props={"href": "http://example.com"})
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_image_node(self):
        node = TextNode("Image Alt", "image", url="http://example.com/image.png")
        expected = LeafNode(tag="img", value="http://example.com/image.png", props={"alt": "Image Alt"})
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_unsupported_node(self):
        node = TextNode("Unsupported Text", "unsupported")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()