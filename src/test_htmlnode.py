import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href": "www.example.com", "class": "someCSSclass"})
        expected='href="www.example.com" class="someCSSclass"'
        self.assertEqual(node.props_to_html(), expected)


    def test_props_single(self):
        node = HTMLNode(None, None, None, {"id": "uniqueID"})
        expected = 'id="uniqueID"'
        self.assertEqual(node.props_to_html(), expected)



if __name__ == "__main__":
    unittest.main()