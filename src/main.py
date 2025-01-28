from textnode import TextNode, TextType

def main():
    # Create a new instance of the TextNode class
    my_node = TextNode("Hello, World!", TextType.Normal, "www.google.com")
    print (my_node.__repr__())

main()