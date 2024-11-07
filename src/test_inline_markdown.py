from inline_markdown import *
import unittest

class TestInlineMarkdownFuncs(unittest.TestCase):
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

    def test_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        print(extract_markdown_images(text))
        # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    def test_link_extraction(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        print(extract_markdown_links(text))
        # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

    def test_image_splitter_bi(self):
        text = [TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type=text_type_text),]
        print("\n************ START IMAGE SPLITTER BI OUTPUT ************\n")
        print(split_nodes_image(text))
        print("\n************ END IMAGE SPLITTER BI OUTPUT ************\n")

    def test_image_splitter_multi(self):
        text = [TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif), an ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg), a ![cat meme](https://goatse.com/goatse.jpeg), and ![your mom](https://onlyfans.com/yourmom/yourmom.png), and here's the rest of the text too.", text_type=text_type_text),]

        print("\n************ START IMAGE SPLITTER MULTI OUTPUT ************\n")
        print(split_nodes_image(text))
        print("\n************ END IMAGE SPLITTER MULTI OUTPUT ************\n")

