import requests
from bs4 import BeautifulSoup

def fetch_headlines(query: str, limit: int = 15) -> list[str]:
    url = f"https://www.bing.com/news/search?q={query}"

    response = requests.get(
        url,
        headers= {"User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    )
},
    timeout=(5, 25)
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for item in soup.select("a.title")[:limit]:
        headlines.append(item.get_text(strip=True))

    return headlines
