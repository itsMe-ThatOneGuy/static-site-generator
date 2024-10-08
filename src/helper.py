import shutil
import os
from markdown_blocks import *

def copy_static_to_public(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for filename in os.listdir(src):
        from_path = os.path.join(src, filename)
        dest_path = os.path.join(dest, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_static_to_public(from_path, dest_path)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block.strip("# ")
    raise Exception("No title")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md:
        md_data = md.read()
    with open(template_path) as html:
        html_data = html.read()

    title = extract_title(md_data)
    md_to_html = markdown_to_html_node(md_data).to_html()
    
    updated_html = html_data.replace("{{ Title }}", title).replace("{{ Content }}", md_to_html)
    with open(dest_path, 'w') as new_file:
        print(updated_html, file=new_file)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename.replace("md", "html"))
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
    