from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node 

def markdown_to_blocks(markdown):
    
    blocks = markdown.split("\n\n")
    filtered_blocks=[]
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(text):
    lines = text.split("\n")
    
    match (lines):  
        case list() if lines[0].startswith("#"):
             return("Heading")
        case list() if lines[0].startswith("```") and lines[len(lines)-1].endswith("```"):
            return("Code")

        case list() if all(line.startswith(">") for line in lines if line):
            return("Quote")
        case list() if all(line.startswith("* ") or line.startswith("- ") for line in lines if line):
            return("Unordered List")
        case list() if all(f"{i + 1}. " in lines[i] for i in range(len(lines))):
            return("Ordered List")
        case _:
            return("Paragraph")
        

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    new_nodes = []
    for block in blocks:
        type = block_to_block_type(block)
        new_block = markdowntype_to_html_node(block,type)
        
        new_nodes.append(new_block)

    
    parentnode1 = ParentNode("div",new_nodes,)
    return parentnode1


def text_to_text_children(text):
    list = []
    text = text_to_textnodes(text)
    for a in text:
        result = text_node_to_html_node(a)
        list.append(result)
        
    return list




def markdowntype_to_html_node(block,type):
    if type == "Heading":
        count = block.count("#")
        block = block.lstrip("# ")
        children = text_to_text_children(block)
        return ParentNode(f"h{count}",children)
    if type == "Code":
        block = block.strip("```")
        children = text_to_text_children(block)
        x = ParentNode("code",children)
        y = ParentNode("pre",[x])
        return y
    if type == "Quote":
        lines2= []
        lines= block.split("\n")
        for line in lines:
            line = line.lstrip("> ")
            lines2.append(line)
        children = " ".join(lines2)
        children = text_to_text_children(children)
        return ParentNode("blockquote",children)
    if type == "Unordered List":
        line=[]
        blocks = block.split("\n")
        for arry in blocks:
            arry= arry.lstrip("- ")
            arry = arry.lstrip("* ")
            text= text_to_text_children(arry)
            line.append(ParentNode("li",text))
                
        return ParentNode("ul",line)
    if type == "Ordered List":
        line=[]
        blocks = block.split("\n")
        for i in range(len(blocks)):
            arry= blocks[i].lstrip(f"{i+1}. ")
            
            text= text_to_text_children(arry)
            line.append(ParentNode("li",text))
                
        return ParentNode("ol",line)
    if type == "Paragraph":
        lines = block.split("\n")
        parragraph = " ".join(lines)
        children = text_to_text_children(parragraph)
        return ParentNode("p",children)
    raise ValueError("Invalid TextType")

