import unittest
from markdown_to_html import *

mixed_type_para_line_md = 'The second paragraph has some **bold**, *italic*, and `inline code` text.'

mixed_type_para_line_children = [
        LeafNode('The second paragraph has some ', None),
        LeafNode('bold', 'b'),
        LeafNode(', ', None),
        LeafNode('italic', 'i'),
        LeafNode(', and ', None),
        LeafNode('inline code', 'code'),
        LeafNode(' text.', None)
        ]


text_only_para_doc_md = '''
This markdown doc is plain text.

But it does have multiple paragraphs.

Like this one.

'''
text_only_para_doc_html_nodes = [
        LeafNode('This markdown doc is plain text.', tag='p'),
        LeafNode('But it does have multiple paragraphs.', tag='p'),
        LeafNode('Like this one.', tag='p')
        ]

mixed_para_doc_md = '''
This markdown doc consists solely of paragraphs.

The second paragraph has some **bold**, *italic*, and `inline code` text.

The third paragraph is text again.

'''

mixed_para_doc_html_nodes = [
        LeafNode('This markdown doc consists solely of paragraphs.'),
        ParentNode(
            'p',
            [
                LeafNode('The second paragraph has some'),
                LeafNode('bold', tag='b'),
                LeafNode(', '),
                LeafNode('italic', tag='i'),
                LeafNode(', and '),
                LeafNode('inline code', tag='code'),
                LeafNode('text.')
            ]
        ),
        LeafNode('The third paragraph is text again.')
    ]

complex_doc_md = '''
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

    #def test_markdown_to_html(self):
        #self.assertEqual(markdown_to_html(mixed_para_doc_md), )
    def test_text_to_children(self):
        self.assertEqual(text_to_children(text_only_para_doc_md), None)

    def test_text_to_children_mixed_para_line(self):
        output = text_to_children(mixed_type_para_line_md)
        for i in range(len(output)):
            self.assertEqual(output[i].value, mixed_type_para_line_children[i].value)
            self.assertEqual(output[i].tag, mixed_type_para_line_children[i].tag)

