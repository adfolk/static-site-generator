from inline_markdown import *
import unittest

imgur = "[imgur](https://imgur.com)"
wikipedia = "[wikipedia](https://wikipedia.com)"
reddit = "[reddit](https://reddit.com)"
fourChan = "[4chan](https://4chan.com)"

para_block_md = '''
    ###### smol header

    This is a paragraph

    This one has **some really strong** text in it. Plus, some *really Italian* text.

    Then there's this third paragraph. It doesn't say much.
    '''

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

        self.assertEqual(split_nodes_delimiter(list_to_split, '*', text_type_italic), expected_output)

    def test_node_splitter_first_word(self):
        unsplit_node = TextNode(text= '*This* is an italic text sample.', text_type=text_type_text)
        list_to_split = [unsplit_node]
        expected_output = [
                TextNode(text='This', text_type=text_type_italic),
                TextNode(text=' is an italic text sample.', text_type=text_type_text),
        ]
            
        self.assertEqual(split_nodes_delimiter(list_to_split, '*', text_type_italic), expected_output)

    def test_image_extraction(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        pass

    def test_link_extraction(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        pass

    def test_image_splitter_middle(self):
        text = [TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and nothing else.", text_type=text_type_text),]
        pass

    def test_image_splitter_bi(self):
        text = [TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", text_type=text_type_text),]
        output = split_nodes_image(text)
        pass

    def test_image_splitter_multi(self):
        text = [TextNode(text="This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif), an ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg), a ![cat meme](https://goatse.com/goatse.jpeg), and ![your mom](https://onlyfans.com/yourmom/yourmom.png), and here's the rest of the text too.", text_type=text_type_text),]
        output = split_nodes_image(text)
        pass

    def test_image_splitter_beginningAndEnd(self):
        text = [TextNode(text="![This text starts with a rick roll](https://i.imgur.com/aKaOqIh.gif), and it ends with an ![obi wan and no punctuation](https://i.imgur.com/fJRm4Vk.jpeg)", text_type=text_type_text),]
        output = split_nodes_image(text)
        pass

    def test_image_splitter_beginningOnly(self):
        text = [TextNode(text="![This text starts with a rick roll](https://i.imgur.com/aKaOqIh.gif), and it ends with an ![obi wan meme](https://i.imgur.com/fJRm4Vk.jpeg), followed by closing text.", text_type=text_type_text),]
        output = split_nodes_image(text)
        pass

    def test_image_splitter_endOnly(self):
        text = [TextNode(text="This text ends with an ![obi wan meme](https://i.imgur.com/fJRm4Vk.jpeg)", text_type=text_type_text),]
        output = split_nodes_image(text)
        pass

    def test_link_splitter_middle(self):
        text = [TextNode(text=f"This text has an {imgur} link and nothing else", text_type=text_type_text),]
        output = split_nodes_link(text)
        pass

    def test_link_splitter_bi(self):
        text = [TextNode(text=f"This text has an {imgur} link and a {wikipedia} link", text_type=text_type_text),]
        output = split_nodes_link(text)
        pass

    def test_link_splitter_tri(self):
        text = [TextNode(text=f"This text has an {imgur} link, a {wikipedia} link, and a {reddit} link", text_type=text_type_text),]
        output = split_nodes_link(text)
        pass

    def test_link_splitter_bookended(self):
        text = [TextNode(text=f"{imgur} starts this text, and at the end is a link to {wikipedia}", text_type=text_type_text),]
        output = split_nodes_link(text)
        pass

    def test_link_splitter_beginning(self):
        text = [TextNode(text=f"{imgur} starts this text", text_type=text_type_text),]
        output = split_nodes_link(text)
        pass

    def test_interim_textstr_delimit_split(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        output = text_to_text_nodes(text)
        pass

    def test_plain_text_textToTextNodes(self):
        text = "This is just a string of text."
        expected_output = [TextNode("This is just a string of text.", text_type_text)]
        self.assertEqual(text_to_text_nodes(text), expected_output)

    def test_problem_child(self):
        output = text_to_text_nodes(para_block_md)
        print(output)

    def test_link_regex(self):
        md_text = "**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)"
        text_node = [TextNode(text=md_text, text_type=text_type_text)]
        output = split_nodes_link(text_node)
        print("\n", output, "\n")

