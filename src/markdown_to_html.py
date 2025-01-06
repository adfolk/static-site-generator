from htmlnode import ParentNode, LeafNode
from textnode import *
from inline_markdown import *
from block_markdown import *

def get_header_lvl(md_line: str):
# Returns the html tag name of a header level as a string, e.g., 'h1', 'h3', 'h6', etc.
# Requires that you first use the block_to_block_type() from the block_markdown module to find out which blocks are headers
    space = md_line.find(' ')
    num_hashes = md_line[:space].count('#')
    return f'h{num_hashes}'

def text_to_children(text: str):
# Takes in a string of markdown text and returns a list of leaf nodes. If multiple nodes are returned, these should be assigned to a parent node.
    text_nodes = text_to_text_nodes(text)
    html_nodes = []
    for i in text_nodes:
        node = text_node_to_html_node(i)
        html_nodes.append(node)
    return html_nodes

def markdown_to_html(md_doc: str):
    blocks = markdown_to_blocks(md_doc)
    block_types = list(map(block_to_block_type, blocks))
    html_nodes = []
    blen = len(blocks)

    for i in range(blen):
        block = blocks[i]
        if block_types[i] == code_type:
            # Assume only plain text inside code blocks
            txt = block.strip('```').strip()
            html_nodes.append(LeafNode(txt, 'code'))

        if block_types[i] == heading_type:
            header = get_header_lvl(block)
            split_header = block.split('# ', 1)
            header_txt = split_header[1]
            offspring = text_to_children(header_txt)
            if len(offspring) > 1:
                parent_header = ParentNode(children=offspring, tag=header)
                html_nodes.append(parent_header)
            if len(offspring) == 1:
                offspring[0].tag = header
                html_nodes.append(offspring[0])

        if block_types[i] == quote_type:
            cleaned_quote = block.replace('> ', '')
            offspring = text_to_children(cleaned_quote)
            quote_block = ParentNode(children=offspring, tag='blockquote')
            html_nodes.append(quote_block)

        if block_types[i] == ul_type:
            # TODO: split ul block into lines
            cleaned_quote = block.replace('* ', '')
            offspring = text_to_children(cleaned_quote)
            ul_block = ParentNode(children=offspring, tag='ul')
            html_nodes.append(ul_block)

    return html_nodes

