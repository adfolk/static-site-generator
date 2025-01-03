from htmlnode import *
from textnode import *
from inline_markdown import *
from block_markdown import *

def get_header_lvl(md_line: str):
# Returns the html tag name of a header level as a string, e.g., 'h1', 'h3', 'h6', etc.
# Requires that you first use the block_to_block_type() from the block_markdown module to find out which blocks are headers
    space = md_line.find(' ')
    num_hashes = md_line[:space].count('#')
    return f'h{num_hashes}'

def text_to_children(text):
# Takes in a string of markdown text and outputs a list of LeafNodes broken down by inline text type.
# If a plain text paragraph block is encountered, this function should simply return None.
    text_nodes = text_to_text_nodes(text)
    if text_nodes != None:
        for i in text_nodes:
            i = text_node_to_html_node(i)
    return text_nodes

#def markdown_to_html(md_doc: str):
#    blocks = markdown_to_blocks(md_doc)
#    block_types = list(map(block_to_block_type, blocks))

