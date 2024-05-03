from textnode import TextNode
from htmlnode import HTMLNode

p = HTMLNode(tag="p", value="some paragraph text")
htmlnode = HTMLNode(tag="a", value="testing value", children=[p], props={"href": "http://google.com"})
node = HTMLNode()

print(p)

