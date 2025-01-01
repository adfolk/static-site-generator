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

def text_to_children(text, block_type):
    if block_type == heading_type:




def markdown_to_html(md_doc: str):
    blocks = markdown_to_blocks(md_doc)
    block_types = list(map(block_to_block_type, blocks))

    for i in range(len(blocks)):

