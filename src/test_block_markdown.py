import unittest
from block_markdown import *

class TestBlockMarkdownFuncs(unittest.TestCase):
    def test_markdown_to_blocks(self):
        input = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
        print("#### test markdown to blocks ####")
        print(markdown_to_blocks(input))

    #TODO: 1) multiple newline characters of even and odd numbers

