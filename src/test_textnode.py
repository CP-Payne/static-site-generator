import unittest

from textnode import TextNode


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


if __name__ == "__main__":
    unittest.main()
