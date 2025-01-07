import unittest
from block_markdown import *
from htmlnode import *
from textnode import *

class TestBlockMarkdownFuncs(unittest.TestCase):
    def test_markdown_to_blocks(self):
        input = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        print("#### test markdown to blocks ####")
        print(markdown_to_blocks(input))

    def test_markdown_to_blocks_code(self):
        code_block_md = '''
            ```
            # This is a code block of python:
            print("Hello, world!")
            ```
        '''

        md_code_block = '''
            ```
            # This is a hello world script in Python.
            my_first_var = "Hello, world!"
            print(my_first_var)
            ```
        '''
        print(markdown_to_blocks(code_block_md))

    def test_markdown_to_blocks_plain_paras(self):
        para_only_md = '''
            This is a paragraph.

            This is also just a paragraph.

            What does the output look like?
            '''

        print("### Test Plain Paragraphs ###\n")
        print(markdown_to_blocks(para_only_md))

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

