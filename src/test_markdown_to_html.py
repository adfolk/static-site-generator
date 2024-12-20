import unittest
from markdown_to_html import *

class TestMarkdownToHTML(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), 'Hello world')
