import os
import pathlib

from block_markdown import markdown_to_html_node


def generate_page(from_path, template_path, dest_path) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        md_content = f.read()
    
    with open(template_path, "r") as f:
        template_content = f.read()

    html_node = markdown_to_html_node(md_content)
    html = html_node.to_html()
    
    page_title = extract_title(md_content)
    full_page = template_content.replace("{{ Title }}", page_title)
    full_page = full_page.replace("{{ Content }}", html) 

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_page)


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str) -> None:
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            dest_path = os.path.join(dest_dir_path, f"{pathlib.Path(filename).stem}.html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def extract_title(md: str) -> str:
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].rstrip("#").strip()
    raise ValueError("no title found")
