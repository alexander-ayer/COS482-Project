
"""
modeling.py

Loads data_clean/processed.csv, trains 3 models (LinearRegression, RandomForest, GradientBoosting),
evaluates with RMSE, MAE, R2, and stores the best model to models/best_model.pkl

Usage:
    python src/modeling.py
"""
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

def load_data(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "..", "data_clean", "processed.csv")
    df = pd.read_csv(path)
    return df

def prepare_features(df):
    df = df.copy()
    # select numeric features and some engineered features
    features = ["budget","imdb_rating","imdb_votes","num_genres","actor_count","release_decade"]
    for f in features:
        if f not in df.columns:
            df[f] = 0
    X = df[features].fillna(0)
    y = df["worldwide_gross"].fillna(0)
    return X, y

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    rmse = mean_squared_error(y_test, preds, squared=False)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    return {"rmse":rmse, "mae":mae, "r2":r2}

def main():
    df = load_data()
    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    models = {
        "LinearRegression": LinearRegression(),
        "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
        "GradientBoosting": GradientBoostingRegressor(n_estimators=200, random_state=42)
    }
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        scores = evaluate_model(model, X_test, y_test)
        results[name] = {"model": model, "scores": scores}
        print(f"{name}: RMSE={scores['rmse']:.2f}, MAE={scores['mae']:.2f}, R2={scores['r2']:.3f}")
    # pick best by RMSE
    best_name = min(results.keys(), key=lambda n: results[n]["scores"]["rmse"])
    best_model = results[best_name]["model"]
    os.makedirs(os.path.join(os.path.dirname(__file__), "..", "models"), exist_ok=True)
    path = os.path.join(os.path.dirname(__file__), "..", "models", "best_model.pkl")
    joblib.dump(best_model, path)
    print(f"Best model: {best_name}. Saved to {path}")

if __name__ == "__main__":
    main()
