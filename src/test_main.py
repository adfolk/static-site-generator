import unittest
from textnode import TextNode
from main import text_node_to_html_node

# 1 test

# tests for text_node_to_html_node function
class TestNodeConversion(unittest.TestCase):
    def check_img(self):
        txtnode = TextNode(text="Italian Trulli", text_type="image", url="pic_trulli.jpg")
        test_html = text_node_to_html_node(txtnode)
        expected_output = '<img src="pic_trulli.jpg" alt="Italian Trulli"></img>'
        self.AssertEqual(test_html.to_html, expected_output)

if __name__ == "__main__":
    unittest.main()

