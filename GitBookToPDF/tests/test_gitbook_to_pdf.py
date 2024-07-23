import unittest
from src.gitbook_to_pdf import fetch_gitbook_content, parse_gitbook_content

class TestGitBookToPDF(unittest.TestCase):

    def test_fetch_gitbook_content(self):
        url = "https://some.gitbook.url"
        content = fetch_gitbook_content(url)
        self.assertTrue(content.startswith("<!DOCTYPE html>"))

    def test_parse_gitbook_content(self):
        html_content = "<div class='book-body'><p>Test Content</p></div>"
        parsed_content = parse_gitbook_content(html_content)
        self.assertIn("Test Content", parsed_content)

if __name__ == "__main__":
    unittest.main()
