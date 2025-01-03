import functools
from htmlnode import *
from textnode import *
from inline_markdown import *
from block_markdown import *

def concatenate(accumulator: str, string: str):
    return accumulator + string + " "

def get_header_lvl(md_line: str):
# Returns the html tag name of a header level as a string, e.g., 'h1', 'h3', 'h6', etc.
# Requires that you first use the block_to_block_type() from the block_markdown module to find out which blocks are headers
    space = md_line.find(' ')
    num_hashes = md_line[:space].count('#')
    return f'h{num_hashes}'

def text_to_children(text: str):
# Takes in a string of markdown text and outputs a list of LeafNodes broken down by inline text type.
# If a plain block is encountered, this function should simply return None.
# When iterating over a list of markdown blocks, remember that if this function returns None, it is because the block should be a LeafNode and must be converted to one outside separately.
    text_nodes = text_to_text_nodes(text)
    html_nodes = []
    for i in text_nodes:
        node = text_node_to_html_node(i)
        html_nodes.append(node)
    if len(html_nodes) < 2:
        return None
    return html_nodes

def markdown_to_html(md_doc: str):
    blocks = markdown_to_blocks(md_doc)
    block_types = list(map(block_to_block_type, blocks))
    html_nodes = []
    blen = len(blocks)

    for i in range(blen):
        block = blocks[i]
        if block_types[i] == code_type:
            txt = functools.reduce(concatenate, block[1:(blen - 1)]).strip()
            html_nodes.append(LeafNode(txt, 'code'))
        if block_types[i] == heading_type:
            header = get_header_lvl(block)
