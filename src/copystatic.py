import os
import shutil
def src_to_public(source,public):
       
    if os.path.exists(public):
        shutil.rmtree(public)
        os.mkdir(public)
    
    dir_to_copy = os.listdir(source)
    
    
    for dir in dir_to_copy:
        folder_explorer(source,public,dir)
def folder_explorer(src="",pth="", element=""):
    
    
    path=os.path.join(src,element)
    dest=os.path.join(pth,element)
    
    if os.path.isfile(path) == True:
        shutil.copy(path,dest)
        print(f"copying {element}from {src} to {pth} ")
    else:
        os.mkdir(dest)
        print(f"creating folder {dest}")
        dir_to_copy = os.listdir(path)
        for dir in dir_to_copy:
            
            folder_explorer(path,dest,dir)



def copy_files_recursive_web(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive_web(from_path, dest_path)