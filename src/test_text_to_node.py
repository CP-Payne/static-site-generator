import unittest
from textnode import *
from inline_markdown import *


class TestTextToTextNodes(unittest.TestCase):

    def test_complete_text_conversion(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("image", "image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev")
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_text_with_no_special_formatting(self):
        text = "This is plain text with no special formatting."
        expected = [
            TextNode(text, "text")
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_text_with_only_bold(self):
        text = "Only **bold** here."
        expected = [
            TextNode("Only ", "text"),
            TextNode("bold", "bold"),
            TextNode(" here.", "text")
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_text_with_multiple_images(self):
        text = "Image ![img1](url1) and ![img2](url2)"
        expected = [
            TextNode("Image ", "text"),
            TextNode("img1", "image", "url1"),
            TextNode(" and ", "text"),
            TextNode("img2", "image", "url2")
        ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)

    def test_empty_input(self):
        text = ""
        expected = []
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()
