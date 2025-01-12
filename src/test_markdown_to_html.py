import unittest
from markdown_to_html import *

majesty_md = '''
# The Unparalleled Majesty of "The Lord of the Rings"

[Back Home](/)

![LOTR image artistmonkeys](/images/rivendell.png)

> "I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to detect its presence.
> I much prefer history, true or feigned, with its varied applicability to the thought and experience of readers.
> I think that many confuse 'applicability' with 'allegory'; but the one resides in the freedom of the reader, and the other in the purposed domination of the author."

In the annals of fantasy literature and the broader realm of creative world-building, few sagas can rival the intricate tapestry woven by J.R.R. Tolkien in *The Lord of the Rings*. You can find the [wiki here](https://lotr.fandom.com/wiki/Main_Page).

## Introduction

This series, a cornerstone of what I, in my many years as an **Archmage**, have come to recognize as the pinnacle of imaginative creation, stands unrivaled in its depth, complexity, and the sheer scope of its *legendarium*. As we embark on this exploration, let us delve into the reasons why this monumental work is celebrated as the finest in the world.

## A Rich Tapestry of Lore

One cannot simply discuss *The Lord of the Rings* without acknowledging the bedrock upon which it stands: **The Silmarillion**. This compendium of mythopoeic tales sets the stage for Middle-earth's history, from the creation myth of Eä to the epic sagas of the Elder Days. It is a testament to Tolkien's unparalleled skill as a linguist and myth-maker, crafting:

1. An elaborate pantheon of deities (the `Valar` and `Maiar`)
2. The tragic saga of the Noldor Elves
3. The rise and fall of great kingdoms such as Gondolin and Númenor

```
print("Lord")
print("of")
print("the")
print("Rings")
```

## The Art of **World-Building**

### Crafting Middle-earth

Tolkien's Middle-earth is a realm of breathtaking diversity and realism, brought to life by his meticulous attention to detail. This world is characterized by:

- **Diverse Cultures and Languages**: Each race, from the noble Elves to the sturdy Dwarves, is endowed with its own rich history, customs, and language. Tolkien, leveraging his expertise in philology, constructed languages such as Quenya and Sindarin, each with its own grammar and lexicon.
- **Geographical Realism**: The landscape of Middle-earth, from the Shire's pastoral hills to the shadowy depths of Mordor, is depicted with such vividness that it feels as tangible as our own world.
- **Historical Depth**: The legendarium is imbued with a sense of history, with ruins, artifacts, and lore that hint at bygone eras, giving the world a lived-in, authentic feel.

## Themes of *Timeless* Relevance

### The *Struggle* of Good vs. Evil

At its heart, *The Lord of the Rings* is a timeless narrative of the perennial struggle between light and darkness, a theme that resonates deeply with the human experience. The saga explores:

- The resilience of the human (and hobbit) spirit in the face of overwhelming odds
- The corrupting influence of power, epitomized by the One Ring
- The importance of friendship, loyalty, and sacrifice

These universal themes lend the series a profound philosophical depth, making it a beacon of wisdom and insight for generations of readers.

## A Legacy **Unmatched**

### The Influence on Modern Fantasy

The shadow that *The Lord of the Rings* casts over the fantasy genre is both vast and deep, having inspired countless authors, artists, and filmmakers. Its legacy is evident in:

- The archetypal "hero's journey" that has become a staple of fantasy narratives
- The trope of the "fellowship," a diverse group banding together to face a common foe
- The concept of a richly detailed fantasy world, which has become a benchmark for the genre

## Conclusion

As we stand at the threshold of this mystical realm, it is clear that *The Lord of the Rings* is not merely a series but a gateway to a world that continues to enchant and inspire. It is a beacon of imagination, a wellspring of wisdom, and a testament to the power of myth. In the grand tapestry of fantasy literature, Tolkien's masterpiece is the gleaming jewel in the crown, unmatched in its majesty and enduring in its legacy. As an Archmage who has traversed the myriad realms of magic and lore, I declare with utmost conviction: *The Lord of the Rings* reigns supreme as the greatest legendarium our world has ever known.

Splendid! Then we have an accord: in the realm of fantasy and beyond, Tolkien's creation is unparalleled, a treasure trove of wisdom, wonder, and the indomitable spirit of adventure that dwells within us all.
'''

text_only_para_doc_md = '''
This markdown doc is plain text.

But it does have multiple paragraphs.

Like this one.
'''

text_only_para_doc_html = "<div><p>This markdown doc is plain text.</p><p>But it does have multiple paragraphs.</p><p>Like this one.</p></div>"

mixed_para_doc_md = '''
This markdown doc consists solely of paragraphs.

The second paragraph has some **bold**, *italic*, and `inline code` text.

The third paragraph is text again.

'''

mixed_para_doc_html_nodes = [
        LeafNode('This markdown doc consists solely of paragraphs.'),
        ParentNode(
            'p',
            [
                LeafNode('The second paragraph has some'),
                LeafNode('bold', tag='b'),
                LeafNode(', '),
                LeafNode('italic', tag='i'),
                LeafNode(', and '),
                LeafNode('inline code', tag='code'),
                LeafNode('text.')
            ]
        ),
        LeafNode('The third paragraph is text again.')
    ]

mixed_doc_md = '''
### This is the header

This is a paragraph of text. It has **bold** and *italic* text.

```
# This is a code block of python:
print("Hello, world!")
```
'''

code_block_md = '''
```
# This is a code block of python:
print("Hello, world!")
```
'''
code_block_html = '<div><code># This is a code block of python:\nprint("Hello, world!")</code></div>'

formatted_header = "## Header with some **bold** text.\n\n### This header has nothing going on."

quote_block_md = '''
    ### Header block

    > First line
    > Second line
    > Third line
    > Fourth line
    '''
ul_block_md = '''
    # Header block

    * item 1
    * item 2
    * item 3
    '''

ol_block_md = '''
    ## header

    1. first item
    2. item 2
    3. item 3
    4. fourth
    5. fiff
    '''

para_block_md = '''
    ###### smol header

    This is a paragraph

    This one has **some really strong** text in it. Plus, some *really Italian* text.

    Then there's this third paragraph. It doesn't say much.
    '''
para_block_html = "<div><h6>smol header</h6><p>This is a paragraph</p><p>This one has <b>some really strong</b> text in it. Plus, some <i>really Italian</i> text.</p><p>Then there's this third paragraph. It doesn't say much.</p></div>"

class TestMarkdownToHTML(unittest.TestCase):
    def test_get_header_lvl(self):
        header = '#### This header has an "#" in it'
        self.assertEqual(get_header_lvl(header), 'h4')

    def test_text_to_children_codeLine(self):
        pass
        #self.assertEqual(text_to_children(code_line_md), None)

    def test_markdown_to_html_header(self):
        header = '### Basic ass h3 header'
        expected_output = '<div><h3>Basic ass h3 header</h3></div>'
        header_node = markdown_to_html(header)
        self.assertEqual(header_node.to_html(), expected_output)

    def test_markdown_to_html_codeblock(self):
        output = markdown_to_html(code_block_md)
        self.assertEqual(output.to_html(), code_block_html)

    def test_markdown_to_html_formatted_header(self):
        output = markdown_to_html(formatted_header)
        #print('\n', output, '\n')
        pass

    def test_markdown_to_html_quoteblock(self):
        output = markdown_to_html(quote_block_md)
        print('\n', output, '\n')

    def test_markdown_to_html_ul(self):
        output = markdown_to_html(ul_block_md)
        print('\n', output, '\n')

    def test_markdown_to_html_ol(self):
        output = markdown_to_html(ol_block_md)
        print('\n', output, '\n')

    def test_markdown_to_html_paras(self):
        output = markdown_to_html(para_block_md)
        self.assertEqual(output.to_html(), para_block_html)
        #print(output.to_html())

