import unittest

from parser import split_nodes_delimiter
from textnode import TextType,TextNode

class TestParser(unittest.TestCase):
    def test_code(self):
        node = TextNode("test for `code` blocks",TextType.TEXT)
        self.assertEqual(split_nodes_delimiter(node,"`", TextType.CODE),
                    [TextNode("test for ", TextType.TEXT, None),
                    TextNode("code", TextType.CODE, None),
                    TextNode(" blocks", TextType.TEXT, None)])

    def test_multiple_italics(self):
        node = TextNode("test _for_ multiple _italics_ in _a_ text _node_", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter(node, "_", TextType.ITALIC),
                    [TextNode('test ',TextType.TEXT,None),
                    TextNode("for",TextType.ITALIC,None),
                    TextNode(" multiple ",TextType.TEXT,None),
                    TextNode("italics",TextType.ITALIC,None),
                    TextNode(' in ',TextType.TEXT,None),
                    TextNode('a',TextType.ITALIC,None),
                    TextNode(' text ',TextType.TEXT,None),
                    TextNode('node', TextType.ITALIC,None)])

    def test_start_with_bold(self):
        node = TextNode('**Starting** with bold text',TextType.TEXT)
        self.assertEqual(split_nodes_delimiter(node, '**', TextType.BOLD),
                    [TextNode('Starting',TextType.BOLD, None),
                    TextNode(' with bold text',TextType.TEXT, None)])
