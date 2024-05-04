import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node","bold")
        node2 = TextNode("This is a text node","bold")
        self.assertEqual(node1, node2)
    def test_type_not_eq(self):
        node1 = TextNode("Cool", "italic")
        node2 = TextNode("Cool", "bold")
        self.assertNotEqual(node1, node2)
    def test_text_not_eq(self):
        node1 = TextNode("Cool", "italic")
        node2 = TextNode("Not Cool", "italic")
        self.assertNotEqual(node1, node2)
    def test_url_eq(self):
        node1 = TextNode("Cool", "italic","http://www.google.com")
        node2 = TextNode("Cool", "italic","http://www.google.com")
        self.assertEqual(node1, node2)
    def test_repr(self):
        node = TextNode("This is not cool","text", "http://www.google.com")
        self.assertEqual("TextNode(This is not cool, text, http://www.google.com)", repr(node))



if __name__ == "__main__":
    unittest.main()
