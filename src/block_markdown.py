import re

heading_type = 'heading'
code_type = 'code'
quote_type = 'quote'
ul_type= 'unordered_list'
ol_type = 'ordered_list'
para_type = 'paragraph'

def markdown_to_blocks(markdown):
    raw_split = markdown.split('\n\n')
    clean_blocks = []

    for item in raw_split:
        if item != '':
            clean_blocks.append(item.strip())

    return clean_blocks

def block_to_block_type(md_block):
    header_match = re.match(r'(#{1,6} )', md_block)
    if header_match:
        return heading_type

    if md_block.startswith('```') and md_block.endswith('```'):
        return code_type

    lines = md_block.splitlines()

    if md_block.startswith('>'):
        is_quote = True
        for line in lines:
            if line.startswith('>') == False:
                is_quote = False
                break
        if is_quote:
            return quote_type

    if md_block.startswith('* ') or md_block.startswith('- '):
        is_unord_list = True
        for line in lines:
            if line.startswith('* ') or line.startswith('- '):
                continue
            else:
                is_unord_list = False
                break
        if is_unord_list:
            return ul_type

    if md_block[0].isnumeric() and md_block.startswith('. ', 1):
        is_ord_list = True
        num = 0
        for line in lines:
            if int(line[0]) == (num + 1) and line.startswith('. ', 1):
                num += 1
            else:
                is_ord_list = False
                break
        if is_ord_list:
            return ol_type
    else:
        return para_type

def markdown_to_html_node(markdown):
    pass

def markdown_to_html_node(markdown):
    pass

