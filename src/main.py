from textnode import TextNode, TextType ,text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import  extract_markdown_images,extract_markdown_links,split_nodes_images, split_nodes_delimiter, split_nodes_links, text_to_textnodes
from markdown_blocks import  markdown_to_blocks,block_to_block_type,markdown_to_html_node, text_to_text_children
from copystatic import src_to_public
from pagegenerator import generate_page,generate_pages_recursive





def main():
    content = "/Users/mgalindo/workspace/github.com/MGalindo111/SSG/content"
    src = "/Users/mgalindo/workspace/github.com/MGalindo111/SSG/static"
    public = "/Users/mgalindo/workspace/github.com/MGalindo111/SSG/public"
    template = "/Users/mgalindo/workspace/github.com/MGalindo111/SSG/template.html"
    src_to_public(src,public)
    
   
    a = generate_pages_recursive(content,template,public)

    
    
    
main()