import os
import shutil


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f __pycache__ copystatic.py htmlnode.py inline_markdown.py main.py markdown_blocks.py test_htmlnode.py test_inline_markdown.py test_markdown_blocks.py test_textnode.py textnode.py {from_path} -
