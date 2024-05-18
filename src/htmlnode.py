from block_markdown import *

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        attributes = ''
        if self.props is None:
            return attributes
        for key, value in self.props.items():
           attributes += f'{key}="{value}" '
        attributes = attributes.rstrip()
        return attributes

    def __repr__(self):
        return f'<HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})>'

class LeafNode(HTMLNode):
    def __init__(self, tag, value,props=None):
        if value is None or value == '':
            raise ValueError('LeafNode value cannot be empty')
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):


        if self.tag is None or self.tag == '':
            return f"{self.value}"

        open_tag = f"<{self.tag} {self.props_to_html()}"
        open_tag = open_tag.rstrip() + ">"
        close_tag = f"</{self.tag}>"

        if self.tag == 'img':
            return f'<img src="{self.value}" {self.props_to_html()}/>'
        return f"{open_tag}{self.value}{close_tag}"

    def __eq__(self, other):
        if not isinstance(other, LeafNode):
            return False
        return self.tag == other.tag and self.value == other.value and self.props == other.props

    def __repr__(self):
        return self.to_html()

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(tag=None, value=text_node.text)

    elif text_node.text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)

    elif text_node.text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)

    elif text_node.text_type == "code":
        return LeafNode(tag="code", value=text_node.text)

    elif text_node.text_type == "link":
        props = {"href": text_node.url}
        return LeafNode(tag="a", value=text_node.text, props=props)

    elif text_node.text_type == "image":
        props = { "alt": text_node.text}
        return LeafNode(tag="img", value=text_node.url , props=props)

    else:
        raise ValueError("Unsupported text type")

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("Tag must be provided for a ParentNode")
        if children is None:
            raise ValueError("Children must be provided for a ParentNode")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        open_tag = f"<{self.tag} {self.props_to_html()}"
        open_tag = open_tag.rstrip() + ">"
        close_tag = f"</{self.tag}>"

        html = open_tag
        for child in self.children:
            html += child.to_html()
        html += close_tag
        return html

def block_to_html_node(block, block_type):
    if block_type == block_type_paragraph:
        return LeafNode(tag="p", value=block)
    elif block_type == block_type_heading:
        level = block.count('#')
        return LeafNode(tag=f"h{level}", value=block.strip('# ').strip())
    elif block_type == block_type_code:
        # Assuming the block includes the triple backticks
        content = '\n'.join(block.split('\n')[1:-1])
        return ParentNode(tag="pre", children=[LeafNode(tag="code", value=content)])
    elif block_type == block_type_quote:
        items = [LeafNode(tag="p", value=item.strip('> ').strip()) for item in block.split('\n')]
        # return ParentNode(tag="blockquote", children=[LeafNode(tag="p", value=block.strip('> ').strip())])
        return ParentNode(tag="blockquote", children=items)
    elif block_type == block_type_unordered_list:
        items = [LeafNode(tag="li", value=item.strip('* ').strip("- ").strip()) for item in block.split('\n')]
        return ParentNode(tag="ul", children=items)
    elif block_type == block_type_ordered_list:
        items = [LeafNode(tag="li", value=item.split('. ')[1]) for item in block.split('\n')]
        return ParentNode(tag="ol", children=items)
    else:
        return LeafNode(tag="div", value=block)  # Fallback for any unhandled types

# Utilizes markdown_to_blocks and block_to_block_type and block_to_html_node to build complete HTML structure
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_to_html_node(block, block_type)
        block_nodes.append(html_node)

    return ParentNode(tag="div", children=block_nodes)

# if __name__ == "__main__":
#     markdown = """
# # Heading One
#
# This is a paragraph with **bold** text.
#
# * List Item 1
# * List Item 2
#
# > This is a quote
#
# 1. Ordered Item 1
# 2. Ordered Item 2
# """
# html_node = markdown_to_html_node(markdown)
# print(html_node.to_html())