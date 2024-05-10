from block_markdown import  *
import unittest

class TestMarkdownToBlocks(unittest.TestCase):

    def test_basic_blocks(self):
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        expected = [
            "This is **bolded** paragraph",
            "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
            "* This is a list\n* with items"
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_excessive_newlines(self):
        markdown = "Paragraph one\n\n\n\nParagraph two\n\n\nParagraph three"
        expected = [
            "Paragraph one",
            "Paragraph two",
            "Paragraph three"
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_empty_input(self):
        markdown = ""
        expected = []
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_whitespace_blocks(self):
        markdown = "\n   \nThis is a paragraph\n\n   \n\nAnother paragraph\n\n"
        expected = [
            "This is a paragraph",
            "Another paragraph"
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_single_block(self):
        markdown = "Only one block of text without any additional newlines."
        expected = [
            "Only one block of text without any additional newlines."
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

    def test_markdown_with_code_blocks(self):
        markdown = "```python\nprint('Hello, world!')\n```\n\nSome text here"
        expected = [
            "```python\nprint('Hello, world!')\n```",
            "Some text here"
        ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected)

        def test_heading(self):
            self.assertEqual(block_to_block_type("# Heading"), block_type_heading)

    def test_code_block(self):
        code_block = "```\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(code_block), block_type_code)

    def test_quote(self):
        quote_block = "> This is a quote\n> This is the second line of the quote"
        self.assertEqual(block_to_block_type(quote_block), block_type_quote)

    def test_unordered_list(self):
        ul_block = "* Item 1\n* Item 2"
        self.assertEqual(block_to_block_type(ul_block), block_type_unordered_list)

    def test_ordered_list(self):
        ol_block = "1. Item 1\n2. Item 2"
        self.assertEqual(block_to_block_type(ol_block), block_type_ordered_list)

    def test_paragraph(self):
        paragraph = "This is a simple paragraph."
        self.assertEqual(block_to_block_type(paragraph), block_type_paragraph)

    def test_mixed_content(self):
        mixed_content = "This is a paragraph with a list:\n- Item 1\n- Item 2"
        # This should ideally be recognized as a paragraph due to mixed content
        self.assertEqual(block_to_block_type(mixed_content), block_type_paragraph)

if __name__ == "__main__":
    unittest.main()
