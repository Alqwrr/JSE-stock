import requests
from bs4 import BeautifulSoup

def fetch_headlines(query: str, limit: int = 5) -> list[str]:
    url = f"https://www.bing.com/news/search?q={query}"

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for item in soup.select("a.title")[:limit]:
        headlines.append(item.get_text(strip=True))

    return headlines
