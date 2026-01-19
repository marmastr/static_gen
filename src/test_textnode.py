import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_link_eq(self):
        node1 = TextNode("simple text", TextType.LINK, "http://img.com/")
        node2 = TextNode("simple text", TextType.LINK, "http://img.com/")
        self.assertEqual(node1, node2)

    def test_link_case_insensetive(self):
        node1 = TextNode("simple text", TextType.IMG, "http://img.com/")
        node2 = TextNode("simple text", TextType.IMG, "Http://Img.Com/")
        self.assertEqual(node1, node2)

    def test_link_not_equal(self):
        node1 = TextNode("simple text", TextType.IMG, "http://img.com/")
        node2 = TextNode("simple text", TextType.IMG)
        self.assertNotEqual(node1, node2)

    def test_link_not_eq(self):
        node1 = TextNode("simple text", TextType.LINK, "http://img.com/")
        node2 = TextNode("simple text", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_missing_text_not_equal(self):
        node1 = TextNode("", TextType.BOLD, "http://notalink.com")
        node2 = TextNode("", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_type_not_eq(self):
        node1 = TextNode("simple text", TextType.IMG, "http://img.com/")
        node2 = TextNode("simple text", TextType.LINK, "http://img.com/")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
