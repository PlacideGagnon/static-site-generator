import unittest

from conversion import *
from htmlnode import *
from textnode import *

class TestConversion(unittest.TestCase):
    def test_text(self):
        print("Running Test Text for Conversion...")
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()
