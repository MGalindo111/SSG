import unittest

from htmlnode import HTMLNode , LeafNode, ParentNode
node3= HTMLNode()
dict = {"href":"www.google.com","target":"_blank"}
dict2 = {"href2":"www.google2.com","target2":"_blank2"}

class TestHTML(unittest.TestCase):
    def test_eq(self):
        
        node = HTMLNode("This is a text node","Hello World",[node3],dict)
        node2 = HTMLNode("This is a text node","Hello World",[node3],dict)
        
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertEqual(node.props, node2.props)

    def testdict_neq(self):
        
        node = HTMLNode("This is a text node","Hello World",[node3],dict)
        node2 = HTMLNode("This is a text node","Hello World",[node3],dict2)
        
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertEqual(node.children, node2.children)
        self.assertNotEqual(node.props, node2.props)

    def test_props_to_html(self):
        node = HTMLNode("This is a text node","Hello World",[node3],dict)
        self.assertEqual(node.props_to_html(), ' href="www.google.com" target="_blank"')

        
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(  
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
    def test_leaf(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://google.com"})
        leaf2=LeafNode("p", "This is a paragraph of text.")

        self.assertEqual(
            leaf.to_html(),
            '<a href="https://google.com">Click me!</a>',
        )
        self.assertEqual(
            leaf2.to_html(),
            '<p>This is a paragraph of text.</p>',
        )
        self.assertEqual(
            leaf.tag,
            "a",
        )
        self.assertEqual(
            leaf.value,
            "Click me!",
        )
        self.assertEqual(
            leaf.props,
            {"href": "https://google.com"},
        )
        self.assertEqual(
            leaf.children,
            None,
        )
        self.assertEqual(
            leaf.__repr__(),
            "HTMLNode(a, Click me!, children: None, {'href': 'https://google.com'})",
        )
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
   
    def test_ParentNode(self):
        parent = ParentNode(
            "p",
            [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            parent.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            
        )
        self.assertEqual(
            parent.tag,
            "p",
        )
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main() 