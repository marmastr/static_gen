import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
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
