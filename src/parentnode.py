from htmlnode import HTMLNode

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
