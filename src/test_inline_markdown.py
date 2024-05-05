import unittest

from textnode import TextNode
from inline_markdown import *


class TestInlineMarkdown(unittest.TestCase):

    # TESTING SPLIT NODE DELIMINATOR
    def test_basic_functionality(self):
        nodes = [TextNode("This is `code` example", "text")]
        result = split_nodes_delimiter(nodes, "`", "code")
        expected = [TextNode("This is ", "text"), TextNode("code", "code"), TextNode(" example", "text")]
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):
        nodes = [TextNode("Some `code` and `more code`", "text")]
        result = split_nodes_delimiter(nodes, "`", "code")
        expected = [TextNode("Some ", "text"), TextNode("code", "code"), TextNode(" and ", "text"), TextNode("more code", "code")]
        self.assertEqual(result, expected)

    def test_nested_delimiters(self):
        nodes = [TextNode("Text `code with *bold* inside` end", "text")]
        result = split_nodes_delimiter(nodes, "`", "code")
        expected = [TextNode("Text ", "text"), TextNode("code with *bold* inside", "code"), TextNode(" end", "text")]
        self.assertEqual(result, expected)

    def test_non_text_type_node(self):
        nodes = [TextNode("Not to be split", "bold")]
        result = split_nodes_delimiter(nodes, "`", "code")
        expected = [TextNode("Not to be split", "bold")]
        self.assertEqual(result, expected)

    def test_empty_text_node(self):
        nodes = [TextNode("", "text")]
        result = split_nodes_delimiter(nodes, "`", "code")
        expected = []
        self.assertEqual(result, expected)

    def test_no_delimiter_in_text(self):
        nodes = [TextNode("No code blocks here", "text")]
        result = split_nodes_delimiter(nodes, "`", "code")
        expected = [TextNode("No code blocks here", "text")]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        nodes = [TextNode("This is `unmatched", "text")]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "`", "code")

    def test_consecutive_delimiters(self):
        nodes = [TextNode("Error with `` consecutive", "text")]
        result = split_nodes_delimiter(nodes, "`", "code")
        expected = [TextNode("Error with ", "text"), TextNode("", "code"), TextNode(" consecutive", "text")]
        self.assertEqual(result, expected)

    # TESTING SPLITING IMAGES AND LINKS
    def test_multiple_images(self):
        node = TextNode("Text ![img1](url1) middle ![img2](url2) end", "text")
        expected = [
            TextNode("Text ", "text"),
            TextNode("img1", "image", "url1"),
            TextNode(" middle ", "text"),
            TextNode("img2", "image", "url2"),
            TextNode(" end", "text")
        ]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_no_images(self):
        node = TextNode("No images here", "text")
        expected = [TextNode("No images here", "text")]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_images_at_edges(self):
        node = TextNode("![img1](url1)Text in between![img2](url2)", "text")
        expected = [
            TextNode("img1", "image", "url1"),
            TextNode("Text in between", "text"),
            TextNode("img2", "image", "url2")
        ]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_adjacent_images(self):
        node = TextNode("![img1](url1)![img2](url2)", "text")
        expected = [
            TextNode("img1", "image", "url1"),
            TextNode("img2", "image", "url2")
        ]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_non_text_node(self):
        node = TextNode("Not to be processed", "code")  # Assume 'code' is a different type
        expected = [TextNode("Not to be processed", "code")]
        result = split_nodes_image([node])
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        node = TextNode("Check this [link1](url1) and this [link2](url2)", "text")
        expected = [
            TextNode("Check this ", "text"),
            TextNode("link1", "link", "url1"),
            TextNode(" and this ", "text"),
            TextNode("link2", "link", "url2")
        ]
        result = split_nodes_link([node])
        self.assertEqual(result, expected)

    def test_no_links(self):
        node = TextNode("No links here", "text")
        expected = [TextNode("No links here", "text")]
        result = split_nodes_link([node])
        self.assertEqual(result, expected)

    def test_links_at_edges(self):
        node = TextNode("[link1](url1)Content goes here[link2](url2)", "text")
        expected = [
            TextNode("link1", "link", "url1"),
            TextNode("Content goes here", "text"),
            TextNode("link2", "link", "url2")
        ]
        result = split_nodes_link([node])
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
