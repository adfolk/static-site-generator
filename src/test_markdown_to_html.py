import unittest
from markdown_to_html import *

simple_doc = '''
### This is the header

This is a paragraph of text. It has **bold** and *italic* text.

```
# This is a code block of python:
print("Hello, world!")
```

'''

class TestMarkdownToHTML(unittest.TestCase):
    def test_get_header_lvl(self):
        header = '#### This header has an "#" in it'
        self.assertEqual(get_header_lvl(header), 'h4')

    def test_markdown_to_html(self):
        print(markdown_to_html(simple_doc))
