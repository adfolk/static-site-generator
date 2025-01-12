from copy_static import copy_dir_to_new_dir
from generate_page import generate_page, generate_pages_recursive


def main():
    src_dir = 'static/'
    dest_dir = 'public/'
    content = 'content/'
    doc_template = 'template.html'

    copy_dir_to_new_dir(src_dir, dest_dir)
    generate_pages_recursive(content, doc_template, dest_dir)

main()

