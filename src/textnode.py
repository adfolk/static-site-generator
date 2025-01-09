from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
        ):
            return True

        else:
            return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


# Function for converting TextNodes to HTMLNodes
def text_node_to_html_node(text_node):

    # Plain text leaf node
    if text_node.text_type == text_type_text:
        return LeafNode(tag=None, value=text_node.text)

    # Bold text leaf node
    if text_node.text_type == text_type_bold:
        return LeafNode(tag="b", value=text_node.text)

    # Italic text leaf node
    if text_node.text_type == text_type_italic:
        return LeafNode(tag="i", value=text_node.text)

    # Code block leaf node
    if text_node.text_type == text_type_code:
        return LeafNode(tag="code", value=text_node.text)

    # Link leaf node
    if text_node.text_type == text_type_link:
        props = {'href': text_node.url}
        return LeafNode(tag="a", value=text_node.text, props=props)

    # Image leaf node
    if text_node.text_type == text_type_image:
        props = {'src': text_node.url, 'alt': text_node.text}
        return LeafNode(tag="img", value='', props=props)
        
    raise Exception('Text type must be one of: text, bold, italic, code, link, image')

