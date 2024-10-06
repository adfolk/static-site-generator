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

    def test_node_splitter(self):
        unsplit_node = TextNode(text= 'This is an *italic* text *sample* with *too many* italics. Ironically, *italics* was not italicized.', text_type=text_type_text)
        list_to_split = [unsplit_node]
        expected_output = [
                TextNode(text='This is an ', text_type=text_type_text),
                TextNode(text='italic', text_type=text_type_italic),
                TextNode(text=' text ', text_type=text_type_text),
                TextNode(text='sample', text_type=text_type_italic),
                TextNode(text=' with ', text_type=text_type_text),
                TextNode(text='too many', text_type=text_type_italic),
                TextNode(text=' italics. Ironically, ', text_type=text_type_text),
                TextNode(text='italics', text_type=text_type_italic),
                TextNode(text=' was not italicized.', text_type=text_type_text),
        ]

        #splits = split_nodes_delimiter(list_to_split, '*', text_type_italic)
        #print('\nBegin multi italic function test\n')
        #for node in splits:
            #print(node.__repr__())

        #print('\nEnd of multi italic function test\n')

        #for node in expected_output:
            #print(node.__repr__())



        self.assertEqual(split_nodes_delimiter(list_to_split, '*', text_type_italic), expected_output)

    def test_node_splitter_first_word(self):
        unsplit_node = TextNode(text= '*This* is an italic text sample.', text_type=text_type_text)
        list_to_split = [unsplit_node]
        expected_output = [
                TextNode(text='This', text_type=text_type_italic),
                TextNode(text=' is an italic text sample.', text_type=text_type_text),
        ]

        #splits = split_nodes_delimiter(list_to_split, '*', text_type_italic)
        #print('\nBegin function test\n')
        #for node in splits:
        #    print(node.__repr__())

        #print('\nEnd of function test\n')

        #for node in expected_output:
        #    print(node.__repr__())
            
        self.assertEqual(split_nodes_delimiter(list_to_split, '*', text_type_italic), expected_output)


if __name__ == "__main__":
    unittest.main()

