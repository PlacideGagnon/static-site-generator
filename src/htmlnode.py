class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        string_props = ""
        if self.props:
            for prop in self.props:
                string_props = string_props + f' {prop}="{self.props[prop]}"'
            return string_props
        return ""

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Value Required in LeafNode")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode (HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag Required in ParentNode")
        if self.children == None:
            raise ValueError("Children Required in ParentNode")
        concatenated = ""
        for child in self.children:
            concatenated += child.to_html()
        return f"<{self.tag}>{concatenated}</{self.tag}>"
