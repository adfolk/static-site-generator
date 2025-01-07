from re import sub
from types import new_class
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
            if block.startswith('- '):
                cleaned_ul_block = block.split('- ')
            else:
                cleaned_ul_block = block.split('* ')
            cleaned_ul_block.remove('')
            offspring = []
            for line in cleaned_ul_block:
                sub_children = text_to_children(line)
                if len(sub_children) > 1:
                    child_parent =ParentNode(children=sub_children, tag='li')
                    offspring.append(child_parent)
                else:
                    sub_children[0].tag = 'li'
                    offspring.append(sub_children[0])
            ul_html_node = ParentNode(children=offspring, tag='ul')
            html_nodes.append(ul_html_node)

        if block_types[i] == ol_type:
            ol_lines = block.split('. ')
            cleaned_ol_lines = []
            for line in ol_lines[1:-1]:
                new_line = line[:-1]
                cleaned_ol_lines.append(new_line)
            cleaned_ol_lines.append(ol_lines[-1])
            offspring = []
            for ol_line in cleaned_ol_lines:
                sub_children = text_to_children(ol_line)
                if len(sub_children) > 1:
                    child_parent =ParentNode(children=sub_children, tag='li')
                    offspring.append(child_parent)
                else:
                    sub_children[0].tag = 'li'
                    offspring.append(sub_children[0])
            ol_html_node = ParentNode(children=offspring, tag='ol')
            html_nodes.append(ol_html_node)

        if block_types[i] == para_type:
                offspring = text_to_children(block)
                if len(offspring) > 1:
                    parent_para = ParentNode(children=offspring, tag='p')
                    html_nodes.append(parent_para)
                else:
                    offspring[0].tag = 'p'
                    html_nodes.append(offspring[0])

    return ParentNode(children=html_nodes, tag='div')

