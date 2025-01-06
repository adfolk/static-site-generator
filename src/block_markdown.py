import re

heading_type = 'heading'
code_type = 'code'
quote_type = 'quote'
ul_type= 'unordered_list'
ol_type = 'ordered_list'
para_type = 'paragraph'

def markdown_to_blocks(markdown: str):
    # Takes an entire markdown doc as a string and eturns a list of strings, each of which represents a unique block of markdown (ex headers, paras, etc)
    raw_split = markdown.split('\n\n')
    clean_blocks = []

    for item in raw_split:
        if item == "":
            continue
        block = item.strip()
        clean_blocks.append(block)

    return clean_blocks

def block_to_block_type(md_block):
    header_match = re.match(r'(#{1,6} )', md_block)
    if header_match:
        return heading_type

    if md_block.startswith('```') and md_block.endswith('```'):
        return code_type

    if md_block.startswith('>'):
        return quote_type

    if md_block.startswith('* ') or md_block.startswith('- '):
        return ul_type

    if md_block[0].isnumeric() and md_block.startswith('. ', 1):
        return ol_type
    
    return para_type

