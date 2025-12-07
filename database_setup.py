
"""
database_setup.py

Provides functions to create database schema. By default it will create an SQLite database at ./models/movies.db
For PostgreSQL, set environment variables and use the create_postgres_schema function.
"""
import os
import sqlite3

def create_sqlite_schema(db_path=None):
    if db_path is None:
        db_path = os.path.join(os.path.dirname(__file__), "..", "models", "movies.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # create simplified tables
    cur.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        imdb_id TEXT PRIMARY KEY,
        title TEXT,
        year INTEGER,
        genre TEXT,
        director TEXT,
        actors TEXT,
        budget INTEGER,
        worldwide_gross INTEGER,
        imdb_rating REAL,
        imdb_votes INTEGER
    )
    """)
    conn.commit()
    conn.close()
    print(f"SQLite schema created at {db_path}")
    return db_path
