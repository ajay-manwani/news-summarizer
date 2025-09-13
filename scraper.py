import requests
from bs4 import BeautifulSoup

def scrape_page(url: str, selector: str) -> str:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    elements = soup.select(selector)
    paragraphs = [el.get_text(strip=True) for el in elements]
    return "\n".join(paragraphs)
