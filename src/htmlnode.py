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
