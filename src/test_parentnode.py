import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):

    def test_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[LeafNode(tag="b", value="Bold text")])

    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="p", children=None)

    def test_valid_html(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode(value="Bold text", tag="b"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(value="italic text", tag="i"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)

    def test_nested_parentnodes(self):
        nested_node = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="p",
                    children=[LeafNode(tag=None, value="Nested paragraph")]
                )
            ]
        )
        expected = "<div><p>Nested paragraph</p></div>"
        self.assertEqual(nested_node.to_html(), expected)

    def test_mixed_children(self):
        mixed_node = ParentNode(
            tag="div",
            children=[
                LeafNode(value="Hello", tag="span"),
                ParentNode(
                    tag="p",
                    children=[LeafNode(value="World", tag=None)]
                )
            ]
        )
        expected = "<div><span>Hello</span><p>World</p></div>"
        self.assertEqual(mixed_node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()
