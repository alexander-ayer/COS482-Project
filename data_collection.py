
"""
data_collection.py

- Primary functions:
    - fetch_omdb(api_key, titles): fetch metadata from OMDb API (requires API key)
    - generate_synthetic_data(n): create a synthetic dataset for testing & development
    - save_raw_csv(df, path): save dataframe to data_raw/master_raw.csv

Usage:
    python src/data_collection.py --generate-synthetic 200
    OR set OMDB_API_KEY environment variable and call fetch_omdb from another script.
"""
import os
import requests
import pandas as pd
import argparse
import time
from typing import List

OMDB_URL = "http://www.omdbapi.com/"

# fetch using OMDb
from src.data_collection import fetch_omdb, save_raw_csv
with open("titles.txt") as f:
    titles = [t.strip() for t in f if t.strip()]
df = fetch_omdb("cdd03cf8", titles)
save_raw_csv(df, path="data_raw/omdb_master.csv")


def fetch_omdb(api_key: str, titles: List[str], sleep: float=0.2):
    records = []
    for t in titles:
        params = {"apikey": api_key, "t": t}
        r = requests.get(OMDB_URL, params=params, timeout=10)
        if r.status_code != 200:
            print(f"Warning: {t} returned status {r.status_code}")
            continue
        j = r.json()
        if j.get("Response") == "False":
            print(f"OMDb: no result for '{t}': {j.get('Error')}")
            continue
        # keep a subset of fields
        rec = {
            "title": j.get("Title"),
            "year": j.get("Year"),
            "rated": j.get("Rated"),
            "released": j.get("Released"),
            "runtime": j.get("Runtime"),
            "genre": j.get("Genre"),
            "director": j.get("Director"),
            "actors": j.get("Actors"),
            "plot": j.get("Plot"),
            "language": j.get("Language"),
            "country": j.get("Country"),
            "awards": j.get("Awards"),
            "imdb_rating": j.get("imdbRating"),
            "imdb_votes": j.get("imdbVotes"),
            "imdb_id": j.get("imdbID"),
            "type": j.get("Type")
        }
        records.append(rec)
        time.sleep(sleep)
    df = pd.DataFrame(records)
    return df

def generate_synthetic_data(n=500, seed=42):
    import numpy as np
    np.random.seed(seed)
    titles = [f"Movie {i}" for i in range(n)]
    years = np.random.randint(1980, 2023, size=n)
    budgets = np.random.randint(1_000_000, 200_000_000, size=n)
    worldwide = budgets * (np.random.uniform(0.2, 6.0, size=n))
    genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Documentary"]
    directors = [f"Director {i%50}" for i in range(n)]
    actors = [f"Actor {i%200}, Actor {(i+1)%200}" for i in range(n)]
    imdb_rating = np.round(np.random.uniform(3.0, 8.5, size=n),1)
    imdb_votes = np.random.randint(100, 500_000, size=n)
    data = {
        "title": titles,
        "year": years,
        "genre": [genres[i % len(genres)] for i in range(n)],
        "director": directors,
        "actors": actors,
        "budget": budgets,
        "worldwide_gross": worldwide.astype(int),
        "imdb_rating": imdb_rating,
        "imdb_votes": imdb_votes
    }
    df = pd.DataFrame(data)
    return df

def save_raw_csv(df, path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "data_raw", "master_raw.csv")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved raw CSV to {path}")
    return path

def base_dir():
    # attempt to find project root relative to this file
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--generate-synthetic", type=int, default=0, help="Generate synthetic data with N rows")
    parser.add_argument("--omdb-key", type=str, default=os.environ.get("OMDB_API_KEY"), help="OMDb API key")
    parser.add_argument("--titles-file", type=str, default=None, help="File with one title per line to fetch from Omdb")
    args = parser.parse_args()

    if args.generate_synthetic and args.generate_synthetic > 0:
        df = generate_synthetic_data(args.generate_synthetic)
        save_raw_csv(df)
    elif args.omdb_key and args.titles_file:
        with open(args.titles_file, "r") as f:
            titles = [l.strip() for l in f if l.strip()]
        df = fetch_omdb(args.omdb_key, titles)
        save_raw_csv(df)
    else:
        print("No action taken. Use --generate-synthetic N or provide --omdb-key and --titles-file.")
