import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str):
    # input: string, a char that will serve as the delimiter (e.g. *, `, etc), and a text_type variable.
    # output: a list of TextNodes. The list will alternate nodes of type "text" with any nodes that matched the delimiter.
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text: str):
    # this function returns a list of tuples of strings that match the pattern variable.
    # if no matches are found, returns an empty list
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text: str):
    # this function returns a list of tuples of strings that match the pattern variable.
    # if no matches are found, returns an empty list
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes: list):
    def match_splitter(match_list, text):
        split_nodes = []
        for i in range(len(match_list)):
            image = matches[i]
            image_alt = image[0]
            image_link = image[1]
            section = text.split(f"![{image_alt}]({image_link})", 1)

            if section[0] == '':
                split_nodes.append(TextNode(text=image_alt, text_type=text_type_image, url=image_link))

                if len(match_list) < 2:
                    split_nodes.append(TextNode(text=section[1], text_type=text_type_text))

                text = section[1]
                continue

            split_nodes.extend([
                TextNode(text=section[0], text_type=text_type_text),
                TextNode(text=image_alt, text_type=text_type_image, url=image_link),
            ])
            
            if i == (len(match_list) - 1) and section[1] != '':
                split_nodes.append(TextNode(text=section[1], text_type=text_type_text))

            text = section[1]

        return split_nodes

    new_nodes = []
    for old_node in old_nodes:
        matches = extract_markdown_images(old_node.text)
        if matches == []:
            new_nodes.append(old_node)
            continue
        new_nodes.extend(match_splitter(matches, old_node.text))
        return new_nodes

def split_nodes_link(old_nodes: list):
    def match_splitter(match_list, text):
        split_nodes = []
        for i in range(len(match_list)):
            link = matches[i]
            link_alt = link[0]
            normal_link = link[1]
            section = text.split(f"[{link_alt}]({normal_link})", 1)

            if section[0] == '':
                split_nodes.append(TextNode(text=link_alt, text_type=text_type_link, url=normal_link))

                if len(match_list) < 2:
                    split_nodes.append(TextNode(text=section[1], text_type=text_type_text))

                text = section[1]
                continue

            split_nodes.extend([
                TextNode(text=section[0], text_type=text_type_text),
                TextNode(text=link_alt, text_type=text_type_link, url=normal_link),
            ])
            
            if i == (len(match_list) - 1) and section[1] != '':
                split_nodes.append(TextNode(text=section[1], text_type=text_type_text))

            text = section[1]

        return split_nodes

    new_nodes = []
    for old_node in old_nodes:
        matches = extract_markdown_links(old_node.text)
        if matches == []:
            new_nodes.append(old_node)
            continue
        new_nodes.extend(match_splitter(matches, old_node.text))
        return new_nodes

def text_to_text_nodes(input_text: str):
    bold_delim = "**"
    ital_delim = "*"
    code_delim = "`"

    unsplit_node = TextNode(text=input_text, text_type=text_type_text)
    unsplit_list = [unsplit_node]
    split_bold = split_nodes_delimiter(unsplit_list, bold_delim, text_type_bold)
    split_ital = split_nodes_delimiter(split_bold, ital_delim, text_type_italic)
    split_code = split_nodes_delimiter(split_ital, code_delim, text_type_code)
    split_img = split_nodes_image(split_code)
    if split_img == None:
        split_lnk = split_nodes_link(split_code)
        if split_lnk == None:
            return split_code
        return split_lnk
    split_final = split_nodes_link(split_img)
    return split_final

