
"""
database_setup.py

Loads cleaned data fro cleaned.py and stores it in a SQLite database.

Workflow:

    1. Run Data_Collection to scrape raw data
    2. Run cleaning.py to get cleaned data
    3. Run database.py to get table "movies"
"""

import os
import sqlite3
from pathlib import Path

import pandas as pd

#Path to processed CSV from cleaning.py
MOVIES_CSV = (
    Path(__file__)
    .resolve()
    .parent
    .joinpath("..", "data_clean", "Processed.csv")
)

DB_PATH = (
    Path(__file__)
    .resolve()
    .parent
    .joinpath("..", "data", "movies.db")
)

TABLE_NAME = "movies"

# Load the data from cleaning.py
def load_data() -> pd.DataFrame:
    if not MOVIES_CSV.exists():
        raise FileNotFoundError(
            f"CSV file not found"
        )
    
    df = pd.read_csv(MOVIES_CSV)

    numerics = [
        "year",
        "runtime_minutes",
        "imdb_rating",
        "imdb_votes",
        "metascore",
        "budget_usd",
        "box_office_usd",
    ]

    for col in numerics:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    
    return df

# Create SQLite DB and return a connection
def create_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parets=True, exists_ok=True) #Ensure data exists
    conn = sqlite3.connect(DB_PATH)
    return conn

# Create/replace movies table from DataFrame
def write_dataframe(df: pd.DataFrame, conn: sqlite3.Connection) -> None:
    df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)


def main():
    print(f"Loading cleaned data from {MOVIES_CSV}...")
    df = load_data()
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
    print(f"Creating SQLite database at {DB_PATH} ...")
    conn = create_connection()
    try:
        print(f"Writing data to table '{TABLE_NAME}' ...")
        write_dataframe(df, conn)
        conn.commit()
        print("Done! Database is ready.")
    finally:
        conn.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()