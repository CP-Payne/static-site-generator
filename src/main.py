from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode, text_node_to_html_node
from parentnode import ParentNode

p = HTMLNode(tag="p", value="some paragraph text")
htmlnode = HTMLNode(tag="a", value="testing value", children=[p], props={"href": "http://google.com"})
node = HTMLNode()
leaf =  LeafNode(value="This is a paragraph", tag="p", props={"class": "bolder"})
leaf_link = LeafNode(tag="a", value="Click me!", props={"href": "http://google.com"})

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
textnode = TextNode("This is a paragraph", "image", url="http://google.com")
text_to_leaf = text_node_to_html_node(textnode)
# print(node.children)
node = TextNode("Sample Text", "text")
expected = LeafNode(tag=None, value="Sample Text")

print(expected)
print(text_node_to_html_node(node))

