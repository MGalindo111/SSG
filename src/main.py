from textnode import TextNode, TextType ,text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import  extract_markdown_images,extract_markdown_links,split_nodes_images, split_nodes_delimiter, split_nodes_links, text_to_textnodes
from markdown_blocks import  markdown_to_blocks,block_to_block_type,markdown_to_html_node, text_to_text_children
import re









def main():
    # Create a new instance of the TextNode class
    my_node = TextNode("Hello, World!", TextType.NORMAL, "www.google.com")
    #print (my_node.__repr__())

    heading="#####This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.* This is the first list item in a list block* This is a list item* This is another list item"
    test = "1. this *is* an **block**\n2. `hello`\n3. hi"

    
    y = markdown_to_html_node(test)
    
    

    print(y.to_html())




     


main()