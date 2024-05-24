import os
import re
import os
from pathlib import Path

from copystatic import copy_static
from htmlnode import *
from inline_markdown import *


def extract_title(markdown_data):

    match = re.search(r'^#\s+(.+)$', markdown_data, re.MULTILINE)
    if match:
        return match.group(1).strip()
    else:
        raise ValueError("No header found the the markdown document.")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Ensure the destination directory exists
    os.makedirs(dest_dir_path, exist_ok=True)

    # Read the template content once
    with open(template_path, 'r', encoding='utf-8') as file:
        template_content = file.read()

    # Recursively process each entry in the directory
    for entry in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, entry)
        if os.path.isdir(full_path):
            # Recursively handle subdirectories
            new_dest_path = os.path.join(dest_dir_path, entry)
            generate_pages_recursive(full_path, template_path, new_dest_path)
        elif full_path.endswith('.md'):
            # Process markdown files
            with open(full_path, 'r', encoding='utf-8') as file:
                markdown_content = file.read()

            # Convert markdown to HTML content
            html_node = markdown_to_html_node(markdown_content)

            html_outer_content = html_node.to_html()
            text_nodes = text_to_textnodes(html_outer_content)
            html_full_content = "".join([text_node_to_html_node(node).to_html() for node in text_nodes])

            # Extract the title from the markdown content
            title = extract_title(markdown_content)

            # Replace placeholders in the template
            final_content = template_content.replace("{{ Title }}", title)
            final_content = final_content.replace("{{ Content }}", html_full_content)

            # Write the HTML content to a new file in the destination directory
            dest_file_path = Path(dest_dir_path) / (Path(entry).stem + '.html')
            with open(dest_file_path, 'w', encoding='utf-8') as file:
                file.write(final_content)
            print(f"Generated page: {dest_file_path}")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown content from from_path
    with open(from_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Read HTML template from template_path
    with open(template_path, 'r', encoding='utf-8') as file:
        template_content = file.read()

    # Convert markdown to HTML node and generate HTML content
    html_node = markdown_to_html_node(markdown_content)
    # TESTING

    html_outer_content = html_node.to_html()

    text_nodes = text_to_textnodes(html_outer_content)
    html_full_content = "".join([text_node_to_html_node(node).to_html() for node in text_nodes])

    # Extract the title from the markdown content
    title = extract_title(markdown_content)

    # Replace placeholders in the template
    final_content = template_content.replace("{{ Title }}", title)
    final_content = final_content.replace("{{ Content }}", html_full_content)

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the final content to the destination path
    with open(dest_path, 'w', encoding='utf-8') as file:
        file.write(final_content)

    print(f"Page successfully generated at {dest_path}")


if __name__ == '__main__':
    copy_static()
    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content/", "template.html", "public/")