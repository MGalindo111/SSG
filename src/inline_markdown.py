from textnode import TextNode, TextType
from htmlnode import LeafNode
def split_nodes_delimiter(old_notes,delimiter,text_type):
    new_notes = []
    
    for note in old_notes:
        if delimiter in note.text:
            split_note = note.text.split(delimiter)
            for i in range(len(split_note)):
                new_notes.append(TextNode(split_note[i],text_type))
        else:
            new_notes.append(note)
    return new_notes
    