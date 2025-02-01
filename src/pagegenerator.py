from textnode import TextNode, TextType ,text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import  extract_markdown_images,extract_markdown_links,split_nodes_images, split_nodes_delimiter, split_nodes_links, text_to_textnodes
from markdown_blocks import  markdown_to_blocks,block_to_block_type,markdown_to_html_node, text_to_text_children
from copystatic import src_to_public
import os

def generate_page(from_path,template_path,dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    sourcedata = open(from_path).read()
    templatedata= open(template_path).read()
    title = extract_title(sourcedata)
    print(f"this is the title:{title}")
    
    sourcehtml = (markdown_to_html_node(sourcedata)).to_html()
    
    finaldata=templatedata.replace("{{ Title }}",title)
    finaldata=finaldata.replace("{{ Content }}",sourcehtml)
    
    finalpath = os.path.join(dest_path,)
    finalpath = finalpath.replace("md","html")
    dirname = os.path.dirname(dest_path)
    os.makedirs(dirname,exist_ok = True)
    
    with open(finalpath, "w", encoding="utf-8") as file:
        file.write(finaldata)

    print(f"HTML file saved at {finalpath}")






def extract_title(markdown):
    blocks = markdown.split("\n\n")
    
    if not blocks[0].startswith("#"):
        print(False)
        raise Exception("No header detected")
    return((blocks[0].lstrip("# ")).rstrip())

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f" * {dir_path_content} -> {dest_dir_path}")
    for filename in os.listdir(dir_path_content):
        
        
        from_path = os.path.join(dir_path_content, filename)
        
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            print(f"{from_path}  is file")
            #print(from_path)
            #print(dest_path)
            #print(template_path)

            generate_page(from_path,template_path,dest_path)
            
        else:
            generate_pages_recursive(from_path,template_path, dest_path)
            print(f"{from_path} is not file")
        
        
    
        
    
        