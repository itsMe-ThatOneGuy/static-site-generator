import unittest
from helper import *

class TestHTMLNode(unittest.TestCase):
    def test_extract_title_with_title(self):
        md_title = """
        # Tolkien Fan Club
        """
        self.assertEqual(
            extract_title(md_title),
            'Tolkien Fan Club'
        )

    def test_extract_title_no_title(self):    
        md_no_title = """
        This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items
        """
        with self.assertRaises(Exception):
            extract_title(md_no_title)
        


if __name__ == "__main__":
    unittest.main()
