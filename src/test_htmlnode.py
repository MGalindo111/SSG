import unittest

from htmlnode import HTMLNode
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

  
    

if __name__ == "__main__":
    unittest.main() 