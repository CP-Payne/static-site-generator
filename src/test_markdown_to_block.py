from block_markdown import markdown_to_blocks
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

if __name__ == "__main__":
    unittest.main()
