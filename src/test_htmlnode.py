import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        print("Running Props to HTML Test...")
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

    def test_leafnode(self):
        print("Running LeafNode Tests...")
        node1 = LeafNode(tag="p", value="Hello, Boot.dev!")
        node2 = LeafNode(tag="a", value="Click me", props={"href": "https://example.com"})
        node3 = LeafNode(value="Just text without a tag")
        self.assertEqual(node1.to_html(), '<p>Hello, Boot.dev!</p>')
        self.assertEqual(node2.to_html(), '<a href="https://example.com">Click me</a>')
        self.assertEqual(node3.to_html(), 'Just text without a tag')

    def test_leaf_to_html_no_value(self):
        print("Running LeafNode No Value Error Test...")
        node = LeafNode(tag="p")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children(self):
        print("Running ParentNode test 1...")
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        print("Running ParentNode test 2...")
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
