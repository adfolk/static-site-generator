import unittest
from markdown_to_html import *


text_only_para_doc_md = '''
This markdown doc is plain text.

But it does have multiple paragraphs.

Like this one.
'''

text_only_para_doc_html = "<div><p>This markdown doc is plain text.</p><p>But it does have multiple paragraphs.</p><p>Like this one.</p></div>"

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

mixed_doc_md = '''
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
code_block_html = '<div><code># This is a code block of python:\nprint("Hello, world!")</code></div>'

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

ol_block_md = '''
    ## header

    1. first item
    2. item 2
    3. item 3
    4. fourth
    5. fiff
    '''

para_block_md = '''
    ###### smol header

    This is a paragraph

    This one has **some really strong** text in it. Plus, some *really Italian* text.

    Then there's this third paragraph. It doesn't say much.
    '''
para_block_html = "<div><h6>smol header</h6><p>This is a paragraph</p><p>This one has <b>some really strong</b> text in it. Plus, some <i>really Italian</i> text.</p><p>Then there's this third paragraph. It doesn't say much.</p></div>"

class TestMarkdownToHTML(unittest.TestCase):
    def test_get_header_lvl(self):
        header = '#### This header has an "#" in it'
        self.assertEqual(get_header_lvl(header), 'h4')

    def test_text_to_children_codeLine(self):
        pass
        #self.assertEqual(text_to_children(code_line_md), None)

    def test_markdown_to_html_header(self):
        header = '### Basic ass h3 header'
        expected_output = '<div><h3>Basic ass h3 header</h3></div>'
        header_node = markdown_to_html(header)
        self.assertEqual(header_node.to_html(), expected_output)

    def test_markdown_to_html_codeblock(self):
        output = markdown_to_html(code_block_md)
        self.assertEqual(output.to_html(), code_block_html)

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

    def test_markdown_to_html_ol(self):
        output = markdown_to_html(ol_block_md)
        print('\n', output, '\n')

    def test_markdown_to_html_paras(self):
        output = markdown_to_html(para_block_md)
        self.assertEqual(output.to_html(), para_block_html)
        #print(output.to_html())

