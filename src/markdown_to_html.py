from htmlnode import *
from textnode import *
from inline_markdown import *
from block_markdown import *

def get_header_lvl(md_line: str):
    space = md_line.find(' ')
    num_hashes = md_line[:space].count('#')
    return f'h{num_hashes}'

