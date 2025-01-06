import unittest
from markdown_to_html import *

full_md_doc = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

full_htmlnode_doc = ParentNode(
    tag='div',
    children = [
        LeafNode(
            tag='h1',
            value='This is a heading',),
        ParentNode(
            tag='p',
            children = [
                LeafNode('This is a paragraph of text. It has some '),
                LeafNode('bold', tag='b'),
                LeafNode(' and '),
                LeafNode('italic', tag='i'),
                LeafNode(' words inside of it'),
            ]
        ),
        ParentNode(
            tag='ul',
            children = [
                LeafNode('This is the first list item in a list block', tag='li'),
                LeafNode('This is a list item', tag='li'),
                LeafNode('This is another list item', tag='li'),
            ]
        )
    ]
)
code_line_md = '`This is just a line of code`'

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

code_block_md = '''
```
# This is a code block of python:
print("Hello, world!")
```
'''

formatted_header = "## Header with some **bold** text.\n\n### This header has nothing going on."

quote_block_md = '''
    ### Header block

    > First line
    > Second line
    > Third line
    > Fourth line
    '''
ul_block_md = '''
    # Header block

    * item 1
    * item 2
    * item 3
    '''

class TestMarkdownToHTML(unittest.TestCase):
    def test_get_header_lvl(self):
        header = '#### This header has an "#" in it'
        self.assertEqual(get_header_lvl(header), 'h4')

    #def test_markdown_to_html(self):
        #self.assertEqual(markdown_to_html(mixed_para_doc_md), )
    def test_text_to_children(self):
        #self.assertEqual(text_to_children(text_only_para_doc_md), None)
        pass

    def test_text_to_children_mixed_para_line(self):
        output = text_to_children(mixed_type_para_line_md)
        for i in range(len(output)):
            self.assertEqual(output[i].value, mixed_type_para_line_children[i].value)
            self.assertEqual(output[i].tag, mixed_type_para_line_children[i].tag)

    def test_text_to_children_codeLine(self):
        pass
        #self.assertEqual(text_to_children(code_line_md), None)

    def test_markdown_to_html_header(self):
        header = '### Basic ass h3 header'
        #expected_output = 
        #print(markdown_to_html(header))
        #print('\n')
        pass

    def test_markdown_to_html_codeblock(self):
        output = markdown_to_html(code_block_md)
        #for i in output:
            #print(i, '\n')
        pass

    def test_markdown_to_html_formatted_header(self):
        output = markdown_to_html(formatted_header)
        #print('\n', output, '\n')
        pass

    def test_markdown_to_html_quoteblock(self):
        output = markdown_to_html(quote_block_md)
        print('\n', output, '\n')

    def test_markdown_to_html_ul(self):
        output = markdown_to_html(ul_block_md)
        print('\n', output, '\n')

