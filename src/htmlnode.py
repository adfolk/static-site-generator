class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        html_string = ""
        for key in self.props:
            html_string += f' {key}="{self.props[key]}"'
        return html_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Value must be provided and cannot be an empty string")
        elif self.tag == None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    
class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):

        if self.tag == None or self.tag == "":
            raise ValueError("Please provide a valid html tag")

        elif self.children == None or self.children == []:
            raise ValueError("Children cannot be None or empty.")

        elif isinstance(self.children, list) == False:
            raise ValueError("Invalid type. Children must be list of HTMLNode objects")

        else:
            html_string = f'<{self.tag}>'
            for node_object in self.children:
                html_string += node_object.to_html()
            html_string += (f'</{self.tag}>')
            return html_string

