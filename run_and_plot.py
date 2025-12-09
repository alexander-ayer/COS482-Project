# src/run_and_plot.py
import os
from pathlib import Path
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor

BASE = Path(__file__).resolve().parents[1]
DATA_CLEAN = BASE / "data_clean" / "processed.csv"
VIS = BASE / "visuals"
MODELS = BASE / "models"
VIS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_CLEAN)

# Basic train/test split for evaluation
features = ["budget", "imdb_rating", "imdb_votes", "num_genres", "actor_count", "release_decade"]
for f in features:
    if f not in df.columns:
        df[f] = 0
X = df[features].fillna(0)
y = df["worldwide_gross"].fillna(0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForest to get feature importances
rf = RandomForestRegressor(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
preds = rf.predict(X_test)
print("RandomForest: RMSE", mean_squared_error(y_test, preds, squared=False))
print("RandomForest: MAE", mean_absolute_error(y_test, preds))
print("RandomForest: R2", r2_score(y_test, preds))

# Histogram of worldwide_gross
plt.figure(figsize=(8,4))
plt.hist(df["worldwide_gross"].dropna(), bins=50)
plt.title("Distribution of Worldwide Gross")
plt.xlabel("Worldwide Gross (USD)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(VIS / "hist_worldwide_gross.png")
plt.close()

# Scatter budget vs worldwide_gross
plt.figure(figsize=(6,5))
plt.scatter(df["budget"], df["worldwide_gross"], alpha=0.6)
plt.title("Budget vs Worldwide Gross")
plt.xlabel("Budget (USD)")
plt.ylabel("Worldwide Gross (USD)")
plt.tight_layout()
plt.savefig(VIS / "scatter_budget_vs_worldwide.png")
plt.close()

# Feature importances
importances = rf.feature_importances_
idx = np.argsort(importances)[::-1]
plt.figure(figsize=(6,4))
plt.bar(range(len(features)), importances[idx])
plt.xticks(range(len(features)), [features[i] for i in idx], rotation=45, ha="right")
plt.title("Feature Importances (Random Forest)")
plt.tight_layout()
plt.savefig(VIS / "rf_feature_importances.png")
plt.close()

print("Plots saved to:", VIS)
