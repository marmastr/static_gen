import unittest

from htmlnode import HTMLNode,LeafNode,ParentNode

class TestTextNode(unittest.TestCase):
    # ============================== Start HTMLNode tests ==============================
    def test_props(self):
        self_props = HTMLNode(props={"href": "http://www.pig.co.uk", "target": "_blank"})
        props_string = ' href="http://www.pig.co.uk" target="_blank"'
        self.assertEqual(self_props.props_to_html(),props_string)

    def test_props_src(self):
        self_props = HTMLNode(props={"src":"img.jpg"})
        props_string = ' src="img.jpg"'
        self.assertEqual(self_props.props_to_html(),props_string)

    def test_props_style(self):
        self_props = HTMLNode(props={"style":"color:blue;"})
        props_string = ' style="color:blue;"'
        self.assertEqual(self_props.props_to_html(),props_string)
    # ============================== End HTMLNode tests ==============================
    # ============================== Start LeafNode tests ============================
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode(tag="a", value="DONOTCLICK", props={"href":"http://didntlisten.huh", "alt":"should listen"})
        self.assertEqual(node.to_html(), '<a href="http://didntlisten.huh" alt="should listen">DONOTCLICK</a>')

    def test_leaf_to_html_tag_none(self):
        node = LeafNode(None, "NOTAG", {"test":"nothing"})
        self.assertEqual(node.to_html(), 'NOTAG')

    def test_leaf_to_html_value_none(self):
        node = LeafNode("div", "Example DIV", {"test":"nothing"})
        self.assertEqual(node.to_html(), '<div test="nothing">Example DIV</div>')
    # ============================== End LeafNode tests ==============================
    # ============================== Start ParentNode tests ==========================
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b></span></div>")
    # ============================== End ParentNode tests ==========================
