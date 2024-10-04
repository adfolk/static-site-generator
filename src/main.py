from textnode import *
from htmlnode import HTMLNode, LeafNode, ParentNode


def text_node_to_html_node(text_node):
    if (
            text_node.text_type != text_type_text 
            and text_node.text_type != text_type_bold 
            and text_node.text_type != text_type_italic
            and text_node.text_type != text_type_code 
            and text_node.text_type != text_type_link
            and text_node.text_type != text_type_image
    ):
        raise Exception('Text type must be one of: text, bold, italic, code, link, image')

    # Plain text leaf node
    elif text_node.text_type == text_type_text:
        text_leaf = LeafNode(tag=None, value=text_node.text)
        return text_leaf

    # Bold text leaf node

    elif text_node.text_type == text_type_bold:
        bold_leaf = LeafNode(tag="b", value=text_node.text)
        return bold_leaf


    # Italic text leaf node

    elif text_node.text_type == text_type_italic:
        italic_leaf = LeafNode(tag="i", value=text_node.text)
        return italic_leaf


    # Code block leaf node

    elif text_node.text_type == text_type_code:
        code_leaf = LeafNode(tag="code", value=text_node.text)
        return code_leaf


    # Link leaf node

    elif text_node.text_type == text_type_code:
        props = {'href': text_node.url}
        link_leaf = LeafNode(tag="a", value=text_node.text, props=props)
        return link_leaf

    # Image leaf node

    elif text_node.text_type == text_type_image:
        props = {'src': text_node.url, 'alt': text_node.text}
        img_leaf = LeafNode(tag="img", value='', props=props)
        return img_leaf

def main():
    test_txtnode = TextNode(text="Italian Trulli", text_type="image", url="pic_trulli.jpg")
    print(test_txtnode.__repr__())
    test_leaf = text_node_to_html_node(test_txtnode)
    print(test_leaf.to_html())
    print(test_leaf.__repr__())


main()

