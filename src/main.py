from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import  extract_markdown_images,extract_markdown_links,split_nodes_images, split_nodes_delimiter, split_nodes_links
from markdown_blocks import  markdown_to_blocks
import re










def main():
    # Create a new instance of the TextNode class
    my_node = TextNode("Hello, World!", TextType.NORMAL, "www.google.com")
    #print (my_node.__repr__())

    heading="      # This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    print(markdown_to_blocks(heading))
    
    

   


     


main()