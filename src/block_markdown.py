import re

# Block type definitions
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def block_to_block_type(block):
    # Check for code block
    if block.startswith("```") and block.endswith("```"):
        return block_type_code

    # Check for heading
    if re.match(r'^#{1,6}\s', block):
        return block_type_heading

    # Check for quote
    if all(line.strip().startswith('>') for line in block.split('\n')):
        return block_type_quote

    # Check for unordered list
    if all(re.match(r'^(\*|-)\s', line.strip()) for line in block.split('\n')):
        return block_type_unordered_list

    # Check for ordered list
    if all(re.match(r'^\d+\.\s', line.strip()) for line in block.split('\n')):
        return block_type_ordered_list

    # Default to paragraph
    return block_type_paragraph

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    cleaned_blocks = [block.strip() for block in blocks if block.strip()]
    return cleaned_blocks