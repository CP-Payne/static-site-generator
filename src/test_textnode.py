import unittest

from textnode import TextNode
from inline_markdown import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq_same_properties(self):
        node1 = TextNode("Hello", "bold")
        node2 = TextNode("Hello", "bold")
        self.assertEqual(node1, node2)

    def test_eq_different_url(self):
        node1 = TextNode("Hello", "bold", "http://example.com")
        node2 = TextNode("Hello", "bold", "http://different.com")
        self.assertNotEqual(node1, node2)

    def test_eq_different_text_type(self):
        node1 = TextNode("Hello", "bold")
        node2 = TextNode("Hello", "italic")
        self.assertNotEqual(node1, node2)

    def test_eq_different_text(self):
        node1 = TextNode("Hello", "bold")
        node2 = TextNode("Goodbye", "bold")
        self.assertNotEqual(node1, node2)

    def test_eq_url_none(self):
        node1 = TextNode("Hello", "bold", None)
        node2 = TextNode("Hello", "bold", None)
        self.assertEqual(node1, node2)

    def test_eq_with_non_textnode(self):
        node1 = TextNode("Hello", "bold")
        self.assertNotEqual(node1, "Hello")

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


if __name__ == "__main__":
    unittest.main()
