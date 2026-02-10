import unittest

from main import extract_title


class TestMain(unittest.TestCase):
    def test_extract_title(self):
        md_headings = ["""
#This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""",
                       """
#This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""",
                       """
#This is **bolded** paragraph




##This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
""",
                       """




This is another paragraph with _italic_ text and `code` here
#This is **bolded** paragraph
This is the same paragraph on a new line

- This is a list
- with items
"""
                       ]
        for md in md_headings:
            self.assertEqual(extract_title(md),"This is **bolded** paragraph")
