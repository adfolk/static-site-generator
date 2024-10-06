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

# TextNode processing functions

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # TODO: handle invalid markdown
    # For each node in the list of old_nodes, split into new nodes based on the delimiter
    new_nodes = []
    def splitter(node):
        # split on the first instance of the delimiter using str.partition(delimiter)
        nonlocal new_nodes
        nonlocal delimiter
        nonlocal text_type

        split = node.text.partition(delimiter) # result is a tuple

        if split[0] == '': # this means the string starts with the delimiter
            new_split = split[2].partition(delimiter)
            textnode = TextNode(text=new_split[0], text_type=text_type)
            new_nodes.append(textnode)

            if new_split[2] == '':
                return
            else:
                remaining_string = new_split[2]
                text_split = remaining_string.partition(delimiter)
                plaintext_node = TextNode(text=text_split[0], text_type=text_type_text)
                new_nodes.append(plaintext_node)

                if text_split[1] == '':
                    return
                else:
                    leftover_node = TextNode(text=text_split[2], text_type=text_type)
                    splitter(leftover_node)

        else:
            textnode = TextNode(text=split[0], text_type=text_type_text)
            new_nodes.append(textnode)

            if split[1] == '':
                return
            else:
                remaining_string = split[2]
                format_split = remaining_string.partition(delimiter)
                format_node = TextNode(text=format_split[0], text_type=text_type)
                new_nodes.append(format_node)

                if format_split[1] == '':
                    return
                else:
                    alt_leftover_node = TextNode(text=format_split[2], text_type=text_type_text)
                    splitter(alt_leftover_node)

    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            splitter(node)
    return new_nodes

# Functions for converting TextNodes to HTMLNodes

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
    if text_node.text_type == text_type_code:
        props = {'href': text_node.url}
        return LeafNode(tag="a", value=text_node.text, props=props)

    # Image leaf node
    if text_node.text_type == text_type_image:
        props = {'src': text_node.url, 'alt': text_node.text}
        return LeafNode(tag="img", value='', props=props)
        
    raise Exception('Text type must be one of: text, bold, italic, code, link, image')

