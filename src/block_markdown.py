def markdown_to_blocks(markdown):
    raw_split = markdown.split('\n\n')
    clean_blocks = []

    for item in raw_split:
        if item != '':
            clean_blocks.append(item)

    return clean_blocks

