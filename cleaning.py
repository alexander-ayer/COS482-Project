
"""
cleaning.py

Load raw CSV, perform cleaning and feature engineering, save processed CSV.

Produces:
  data_clean/processed.csv
"""
import os
import pandas as pd
import numpy as np

def load_raw(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "data_raw", "master_raw.csv")
    df = pd.read_csv(path)
    return df

def clean_df(df):
    # Basic cleaning
    df = df.copy()
    # normalize column names
    df.columns = [c.strip() for c in df.columns]
    # fill missing numeric with median
    for c in ["budget","worldwide_gross","imdb_votes","imdb_rating"]:
        if c in df.columns:
            if df[c].dtype == object:
                # remove commas / dollar signs
                df[c] = df[c].astype(str).str.replace("[\\$,]", "", regex=True)
            df[c] = pd.to_numeric(df[c], errors="coerce")
            df[c] = df[c].fillna(df[c].median())
    # Year to integer
    if "year" in df.columns:
        df["year"] = pd.to_numeric(df["year"].astype(str).str.slice(0,4), errors="coerce").fillna(2000).astype(int)
    # Create profit and ROI
    if "budget" in df.columns and "worldwide_gross" in df.columns:
        df["profit"] = df["worldwide_gross"] - df["budget"]
        df["ROI"] = df.apply(lambda r: (r["worldwide_gross"] - r["budget"]) / r["budget"] if r["budget"]>0 else 0, axis=1)
    else:
        df["profit"] = 0
        df["ROI"] = 0
    # Number of genres (if genre string)
    if "genre" in df.columns:
        df["num_genres"] = df["genre"].fillna("").apply(lambda s: len([g.strip() for g in s.split(",") if g.strip()]))
    else:
        df["num_genres"] = 0
    # Actor count
    if "actors" in df.columns:
        df["actor_count"] = df["actors"].fillna("").apply(lambda s: len([a.strip() for a in s.split(",") if a.strip()]))
    else:
        df["actor_count"] = 0
    # Release decade
    if "year" in df.columns:
        df["release_decade"] = (df["year"] // 10) * 10
    else:
        df["release_decade"] = 2000
    # drop duplicates on title+year if present
    if all(c in df.columns for c in ["title","year"]):
        df = df.drop_duplicates(subset=["title","year"])
    return df

def save_processed(df, path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "data_clean", "processed.csv")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Processed data saved to {path}")
    return path

if __name__ == "__main__":
    raw = load_raw()
    cleaned = clean_df(raw)
    save_processed(cleaned)
