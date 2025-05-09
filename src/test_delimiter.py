import unittest

from textnode import *
from delimiter import *

class TestDelimiter(unittest.TestCase):
    def test_split_delimiter(self):
        print("Testing Split Delimiter...")
        # Test with code blocks using backticks
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

            # Assert we got 3 nodes back
        self.assertEqual(len(new_nodes), 3)

                # Check the content and type of each node
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)

        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_missing_closing_delimiter(self):
        print("Testing Missing Closing Delimiter...")
                # Test with missing closing delimiter
        node = TextNode("This is text with a `code block without closing", TextType.TEXT)

                # Should raise an exception
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()
