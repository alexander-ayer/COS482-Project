# src/boxoffice_scraper.py
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; MovieSuccessBot/1.0; +https://example.com/bot)"
}

def fetch_the_numbers_movie(url):
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    # Example selectors — adapt to the site's actual structure
    budget = None
    worldwide = None
    # Example: look for table rows with 'Production Budget' or 'Worldwide Box Office'
    for tr in soup.select("table"):  # narrow down to the right table
        txt = tr.get_text(separator=" ").lower()
        if "production budget" in txt or "domestic box office" in txt:
            # parse numbers heuristically
            pass
    # A specific The Numbers page often has id=box_office or similar.
    # Return dictionary
    return {"budget": budget, "worldwide_gross": worldwide}

def fetch_batch(urls, sleep=1.0):
    records = []
    for u in urls:
        try:
            rec = fetch_the_numbers_movie(u)
            records.append(rec)
        except Exception as e:
            print("Error", u, e)
        time.sleep(sleep)
    return pd.DataFrame(records)
