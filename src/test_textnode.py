import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("Running Node Test...")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_none(self):
        print("Running None-URL Test...")
        url = TextNode("This is normal text", TextType.TEXT, None)
        url2 = TextNode("This is normal text", TextType.TEXT)
        self.assertEqual(url, url2)

    def test_not_eq(self):
        print("Running Not Equal Test...")
        not_equal = TextNode("This is text", TextType.TEXT)
        not_equal2 = TextNode("This is text", TextType.BOLD)
        self.assertNotEqual(not_equal, not_equal2)

        print("Running Different Text Test...")
        diff_text = TextNode("This is some text", TextType.TEXT)
        diff_text2 = TextNode("This is some other text", TextType.TEXT)
        self.assertNotEqual(diff_text, diff_text2)

        print("Running Different URL Test...")
        node_with_url = TextNode("Link text", TextType.LINK, "https://example.com")
        node_with_different_url = TextNode("Link text", TextType.LINK, "https://different.com")
        self.assertNotEqual(node_with_url, node_with_different_url)


if __name__ == "__main__":
    unittest.main()
