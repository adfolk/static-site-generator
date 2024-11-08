from inline_markdown import *
import unittest

imgur = "[imgur](https://imgur.com)"
wikipedia = "[wikipedia](https://wikipedia.com)"
reddit = "[reddit](https://reddit.com)"
fourChan = "[4chan](https://4chan.com)"

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

    def test_image_splitter_middle(self):
        text = [TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and nothing else.", text_type=text_type_text),]
        print("\n************ START IMAGE SPLITTER MIDDLE OUTPUT ************\n")
        print(f"Input text: {text}")
        print(split_nodes_image(text))
        print("\n************ END IMAGE SPLITTER MIDDLE OUTPUT ************\n")

    def test_image_splitter_bi(self):
        text = [TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type=text_type_text),]
        print("\n************ START IMAGE SPLITTER BI OUTPUT ************\n")
        print(f"Input text: {text}\n")
        output = split_nodes_image(text)
        for object in output:
            print(object)
        print("\n\n************ END IMAGE SPLITTER BI OUTPUT ************\n")

    def test_image_splitter_multi(self):
        text = [TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif), an ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg), a ![cat meme](https://goatse.com/goatse.jpeg), and ![your mom](https://onlyfans.com/yourmom/yourmom.png), and here's the rest of the text too.", text_type=text_type_text),]

        print("\n************ START IMAGE SPLITTER MULTI OUTPUT ************\n")
        print(f"Input text: {text}\n")
        output = split_nodes_image(text)
        for object in output:
            print(object)
        print("\n\n************ END IMAGE SPLITTER MULTI OUTPUT ************\n")

    def test_image_splitter_beginningAndEnd(self):
        text = [TextNode(text="![This text starts with a rick roll](https://i.imgur.com/aKaOqIh.gif), and it ends with an ![obi wan and no punctuation](https://i.imgur.com/fJRm4Vk.jpeg)", text_type=text_type_text),]

        print("\n************ START IMAGE SPLITTER BOOKENDED OUTPUT ************\n")
        print(f"Input text: {text}\n")
        output = split_nodes_image(text)
        for object in output:
            print(object)
        print("\n\n************ END IMAGE SPLITTER BOOKENDED OUTPUT ************\n")

    def test_image_splitter_beginningOnly(self):
        text = [TextNode(text="![This text starts with a rick roll](https://i.imgur.com/aKaOqIh.gif), and it ends with an ![obi wan meme](https://i.imgur.com/fJRm4Vk.jpeg), followed by closing text.", text_type=text_type_text),]

        print("\n************ START IMAGE SPLITTER BEGINNING ONLY OUTPUT ************\n")
        print(f"Input text: {text}\n")
        output = split_nodes_image(text)
        for object in output:
            print(object)
        print("\n\n************ END IMAGE SPLITTER BEGINNING ONLY OUTPUT ************\n")

    def test_image_splitter_endOnly(self):
        text = [TextNode(text="This text ends with an ![obi wan meme](https://i.imgur.com/fJRm4Vk.jpeg)", text_type=text_type_text),]

        print("\n************ START IMAGE SPLITTER END ONLY OUTPUT ************\n")
        print(f"Input text: {text}\n")
        output = split_nodes_image(text)
        for object in output:
            print(object)
        print("\n\n************ END IMAGE SPLITTER END ONLY OUTPUT ************\n")

    # Test Link Splitter

    # MIDDLE
    def test_link_splitter_middle(self):
        text = [TextNode(text=f"This text has an {imgur} link and nothing else", text_type=text_type_text),]

        print("\n************ START LINK SPLITTER MIDDLE OUTPUT ************\n")
        print(f"Input text: {text}\n")
        output = split_nodes_link(text)
        for object in output:
            print(object)
        print("\n\n************ END LINK SPLITTER MIDDLE OUTPUT ************\n")

    # BI
    def test_link_splitter_bi(self):
        text = [TextNode(text=f"This text has an {imgur} link and a {wikipedia} link", text_type=text_type_text),]

        print("\n************ START LINK SPLITTER BI OUTPUT ************\n")
        print(f"Input text: {text}\n")
        output = split_nodes_link(text)
        for object in output:
            print(object)
        print("\n\n************ END LINK SPLITTER BI OUTPUT ************\n")

    # TRI
    def test_link_splitter_tri(self):
        text = [TextNode(text=f"This text has an {imgur} link, a {wikipedia} link, and a {reddit} link", text_type=text_type_text),]

        print("\n************ START LINK SPLITTER TRI OUTPUT ************\n")
        print(f"Input text: {text}\n")
        output = split_nodes_link(text)
        for object in output:
            print(object)
        print("\n\n************ END LINK SPLITTER TRI OUTPUT ************\n")

    # BOOKENDED
    def test_link_splitter_bookended(self):
        text = [TextNode(text=f"{imgur} starts this text, and at the end is a link to {wikipedia}", text_type=text_type_text),]

        print("\n************ START LINK SPLITTER BOOKEND OUTPUT ************\n")
        print(f"Input text: {text}\n")
        output = split_nodes_link(text)
        for object in output:
            print(object)
        print("\n\n************ END LINK SPLITTER BOOKEND OUTPUT ************\n")
    # BEGINNING ONLY
    def test_link_splitter_beginning(self):
        text = [TextNode(text=f"{imgur} starts this text", text_type=text_type_text),]

        print("\n************ START LINK SPLITTER BEGINNING OUTPUT ************\n")
        print(f"Input text: {text}\n")
        output = split_nodes_link(text)
        for object in output:
            print(object)
        print("\n\n************ END LINK SPLITTER BOOKEND OUTPUT ************\n")
    # END ONLY

