import os
import shutil
from textnode import *
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_html import markdown_to_html
from copy_static import copy_dir_to_new_dir


def main():
    src_dir = 'static/'
    dest_dir = 'public/'
    copy_dir_to_new_dir(src_dir, dest_dir)

main()

