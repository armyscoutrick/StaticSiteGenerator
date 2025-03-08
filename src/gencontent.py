import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"Scanning directory: {dir_path_content}")
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):  # Process files
            print(f"Found file: {from_path}")
            if filename.endswith(".md"):
                dest_path = os.path.splitext(dest_path)[0] + ".html"
                print(f"Generating page: {from_path} -> {dest_path}")
                generate_page(from_path, template_path, dest_path)
            else:
                print(f"Skipping non-markdown file: {from_path}")

        else:  # Process directories
            print(f"Found directory: {from_path}")
            os.makedirs(dest_path, exist_ok=True)
            print(f"Ensuring directory exists in destination: {dest_path}")
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating HTML: {from_path} -> {dest_path}")
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")
