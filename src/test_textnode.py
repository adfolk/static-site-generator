import unittest

from textnode import *
from htmlnode import *

# 5 tests


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_diff(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("But this one is different", "bold")
        self.assertNotEqual(node, node2)

    def test_url_diff(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "https://google.com")
        self.assertNotEqual(node, node2)

    def test_url_eq(self):
        node = TextNode("This is a text node", "bold", "https://google.com")
        node2 = TextNode("This is a text node", "bold", "https://google.com")
        self.assertEqual(node, node2)

    def test_convert_img_props(self):
        txtnode = TextNode(text="Italian Trulli", text_type="image", url="pic_trulli.jpg")
        test_html = text_node_to_html_node(txtnode)
        self.assertEqual(test_html.props, {'src': 'pic_trulli.jpg', 'alt': 'Italian Trulli'})

    def test_convert_img_io(self):
        txtnode = TextNode(text="Italian Trulli", text_type="image", url="pic_trulli.jpg")
        test_html = text_node_to_html_node(txtnode)
        expected_output = '<img src="pic_trulli.jpg" alt="Italian Trulli"></img>'
        func_out = test_html.to_html()
        self.assertEqual(func_out, expected_output)

if __name__ == "__main__":
    unittest.main()

