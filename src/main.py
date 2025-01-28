from textnode import TextNode, TextType
from htmlnode import HtmlNode, LeafNode, ParentNode



def main():
    # Create a new instance of the TextNode class
    my_node = TextNode("Hello, World!", TextType.Normal, "www.google.com")
    print (my_node.__repr__())




main()