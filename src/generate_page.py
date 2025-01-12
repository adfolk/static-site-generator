import os
from markdown_to_html import get_header_lvl, markdown_to_html
from block_markdown import markdown_to_blocks, block_to_block_type, heading_type

# Extracts the h1 header if it exists. If not, it raises an exception.
def extract_title(markdown: str):
    md_blocks = markdown_to_blocks(markdown)
    for block in md_blocks:
        if block_to_block_type(block) == heading_type:
        # break the markdown doc into blocks and compute the block types.
        # this allows us to be sure that we actually extract an h1 header, and not, e.g., a python comment from a code block.
            header = get_header_lvl(block)
            if header == 'h1':
                return block.removeprefix('# ')
    raise Exception("Markdown document must contain an h1 header. The h1 header will become the title of the webpage.")


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    dir_contents = os.listdir(dir_path_content)
    print(f"contents of {dir_path_content}: {dir_contents}")
    for item in dir_contents:
        print(f"working on dir item: {item}")
        new_item = os.path.join(dir_path_content, item)
        new_dest = os.path.join(dest_dir_path, item)
        if os.path.isfile(new_item) == False:
            print(f"this should be a dir: {new_item}")
            print(f"target dir: {new_dest}")
            generate_pages_recursive(new_item, template_path, new_dest)

        if os.path.isfile(new_item):
            print(f"this should be a file: {new_item}")
            with open(new_item, encoding='utf-8') as f:
                content_md = f.read()

            with open(template_path, encoding='utf-8') as g:
                tpl_md = g.read()

            webpage_title = extract_title(content_md)
            html_node = markdown_to_html(content_md)
            html_string = html_node.to_html()
            titled_html_doc = tpl_md.replace("{{ Title }}", webpage_title)
            final_html_doc = titled_html_doc.replace("{{ Content }}", html_string)

            if not os.path.exists(dest_dir_path) and not os.path.isfile(dest_dir_path):
                print(f"about to mkdir: {dest_dir_path}")
                os.mkdir(dest_dir_path)
            webpage_filename = get_filename(item, '.html')
            webpage_file_dest = os.path.join(dest_dir_path, webpage_filename)
            print(f"new page going here: {webpage_file_dest}")

            with open(webpage_file_dest, mode='x', encoding='utf-8') as h:
                h.write(final_html_doc)

def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, encoding="utf-8") as f:
        content_md = f.read()

    with open(template_path, encoding="utf-8") as g:
        tpl_md = g.read()

    webpage_title = extract_title(content_md)
    html_node = markdown_to_html(content_md)
    html_string = html_node.to_html()
    titled_html_doc = tpl_md.replace("{{ Title }}", webpage_title)
    final_html_doc = titled_html_doc.replace("{{ Content }}", html_string)
    if not os.path.exists(dest_path) and not os.path.isfile(dest_path):
        os.mkdir(dest_path)
    webpage_filename = get_filename(from_path, '.html')
    webpage_file_dest = os.path.join(dest_path, webpage_filename)

    with open(webpage_file_dest, mode='x', encoding='utf-8') as f:
        f.write(final_html_doc)

def get_filename(from_path: str, file_ext: str):
    split_path = os.path.split(from_path)
    old_filename = split_path[1]
    old_filename_split = old_filename.rsplit('.', maxsplit=1)
    old_filename_head = old_filename_split[0]
    new_filename = old_filename_head + file_ext
    return new_filename

