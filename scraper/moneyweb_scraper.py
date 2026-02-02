import requests
from bs4 import BeautifulSoup
from requests.exceptions import ReadTimeout, RequestException

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    )
})

def fetch_moneyweb_headlines(query: str, limit: int = 30) -> list[str]:

    url = f"https://www.moneyweb.co.za/search/{query}"
    try:
        
        response = SESSION.get(
            url,
            timeout=(5, 25)
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        headlines = []
        for item in soup.select("h3.title.list-title.m0005")[:limit]:
            headlines.append(item.get_text(strip=True))

        return headlines
    except ReadTimeout:
        print(f"[WARN] Moneyweb timeout for {query}")
        return []

    except RequestException as e:
        print(f"[ERROR] Moneyweb request failed: {e}")
        return []