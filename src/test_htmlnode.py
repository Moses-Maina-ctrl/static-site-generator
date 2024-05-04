import unittest

from htmlnode import HTMLNode

class html_test(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a","BootDev", None, {"class":"link", "href":"https://boot.dev"})
