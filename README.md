
# Predicting Movie Success - Project

Structure:

- data_raw/: raw CSVs and scraped data
- data_clean/: cleaned and processed data
- src/: python scripts (collection, cleaning, modeling)
- notebooks/: EDA and analysis notebooks
- models/: saved models
- visuals/: saved plots
- report/: final writeup

Quickstart (without external APIs):
1. Generate synthetic data:
    python src/data_collection.py --generate-synthetic 1000
2. Clean:
    python src/cleaning.py
3. Train:
    python src/modeling.py

For OMDb: set "cdd03cf8" and provide titles file to fetch real metadata.
