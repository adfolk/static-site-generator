import unittest
from block_markdown import *
from htmlnode import *
from textnode import *

class TestBlockMarkdownFuncs(unittest.TestCase):
    def test_markdown_to_blocks(self):
        input = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        print("#### test markdown to blocks ####")
        print(markdown_to_blocks(input))

    #TODO: 1) multiple newline characters of even and odd numbers
    def test_markdown_to_blocks_multiple_spaces(self):
        input = "# This is a heading\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        print("#### test markdown blocks multi ####")
        print(markdown_to_blocks(input))

    def test_block_type_heading(self):
        input = "### This is a heading"
        self.assertEqual(block_to_block_type(input), 'heading')

    def test_block_type_code(self):
        input = "```\nThis is the first line of the code block\nThis is the second\nThis is the third\n```"
        self.assertEqual(block_to_block_type(input), 'code')

    def test_block_type_quote(self):
        input = ">quote line 1\n>quote line 2\n>quote line 3"
        self.assertEqual(block_to_block_type(input), 'quote')

    def test_block_type_unordered_list(self):
        input = "* list item 1\n* list item 2\n* list item 3"
        self.assertEqual(block_to_block_type(input), 'unordered_list')

    def test_block_type_ordered_list(self):
        input = "1. list item 1\n2. list item 2\n3. list item 3"
        self.assertEqual(block_to_block_type(input), 'ordered_list')

    def test_markdown_to_html_node(self):
        input = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

        expected_output = HTMLNode(
            tag='div',
            children = [
                HTMLNode(
                    tag='h1',
                    value='This is a heading',
                    children = [
                        HTMLNode(
                            tag='p',
                            children = [
                                LeafNode('This is a paragraph of text. It has some '),
                                LeafNode('bold', tag='b'),
                                LeafNode(' and '),
                                LeafNode('italic', tag='i'),
                            ]
                        ),
                        HTMLNode(
                            tag='ul',
                            children = [
                                LeafNode('This is the first list item in a list block'),
                                LeafNode('This is a list item'),
                                LeafNode('This is another list item'),
                            ]
                        )
                    ]
                )
            ]
        )
        self.assertEqual(expected_output, markdown_to



