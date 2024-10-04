import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

# 8 tests

class TestHTMLNode(unittest.TestCase):
    
    #HTMLNode test cases

    def test_props_multi(self):
        test_link = {
                "href": "www.boot.dev",
                "target": "img.jpeg",
                "rel": "preload",
        }
        test_node = HTMLNode(props=test_link)

        test_output = test_node.props_to_html()
        test_answer = ' href="www.boot.dev" target="img.jpeg" rel="preload"'
        self.assertEqual(test_output, test_answer)

    def test_props_single(self):
        test_link = {
                "href": "www.boot.dev",
        }
        test_node = HTMLNode(props=test_link)

        test_output = test_node.props_to_html()
        test_answer = ' href="www.boot.dev"'
        self.assertEqual(test_output, test_answer)

    def test_props_double(self):
        test_link = {
                "href": "www.boot.dev",
                "target": "_blank",
        }
        test_node = HTMLNode(props=test_link)

        test_output = test_node.props_to_html()
        test_answer = ' href="www.boot.dev" target="_blank"'
        self.assertEqual(test_output, test_answer)

    # LeafNode test cases

    def test_value_only(self):
        dummy_leaf = LeafNode(value="This is it")
        self.assertEqual(dummy_leaf.to_html(), "This is it")

    def test_propless_leaf(self):
        dummy_leaf = LeafNode(tag="p", value="This is a paragraph of text")
        self.assertEqual(dummy_leaf.to_html(), "<p>This is a paragraph of text</p>")

    def test_prop_leaf(self):
        dummy_leaf = LeafNode(tag="p", value="This is a paragraph of text", props={"href": "https://google.com"})
        self.assertEqual(dummy_leaf.to_html(), '<p href="https://google.com">This is a paragraph of text</p>')
    
    def test_leaf_repr(self):
        dummy_leaf = LeafNode(tag="p", value="This is a paragraph of text", props={"href": "https://google.com"})
        self.assertEqual(dummy_leaf.__repr__(), "LeafNode(p, This is a paragraph of text, {'href': 'https://google.com'})")


    # ParentNode test cases

    def test_nested_parent(self):
        bold_leaf = LeafNode(tag="b", value="Bold text")
        normal_leaf = LeafNode(tag=None, value="Normal text")
        link_node = LeafNode(tag="a", value="This is also text", props={"href": "https://google.com"})
        normal_parent = ParentNode(
            tag="p",
            children=[
                bold_leaf,
                normal_leaf,
                link_node]
            )

        nested_parent = ParentNode(
            tag="p",
            children=[
                bold_leaf,
                normal_parent,
                bold_leaf]
            )

        self.assertEqual(nested_parent.to_html(), '<p><b>Bold text</b><p><b>Bold text</b>Normal text<a href="https://google.com">This is also text</a></p><b>Bold text</b></p>')

