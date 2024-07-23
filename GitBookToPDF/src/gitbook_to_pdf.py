import requests
from bs4 import BeautifulSoup
import pdfkit

def fetch_gitbook_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch GitBook content")
    return response.text

def parse_gitbook_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    # Extract relevant content for PDF
    content = soup.find("div", {"class": "book-body"})
    return str(content)

def save_as_pdf(content, output_file):
    pdfkit.from_string(content, output_file)

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python gitbook_to_pdf.py <gitbook_url>")
        return

    gitbook_url = sys.argv[1]
    html_content = fetch_gitbook_content(gitbook_url)
    parsed_content = parse_gitbook_content(html_content)
    save_as_pdf(parsed_content, "output.pdf")

if __name__ == "__main__":
    main()
