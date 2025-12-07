
# Movie Success Prediction — Final Report

## 1. Introduction
This project predicts worldwide box-office gross using metadata and engineered features.

## 2. Data Sources
- OMDb API (movie metadata)
- Box Office Mojo / The Numbers (budget & gross) — add CSVs into `data_raw/`

## 3. Methodology
- Data collection -> cleaning -> feature engineering -> modeling using scikit-learn

## 4. EDA
See `notebooks/EDA.ipynb` for exploratory plots. Key analyses to include:
- Distribution of budgets and worldwide gross
- Correlation heatmap
- Revenue by genre and decade

## 5. Modeling
Models trained: Linear Regression, Random Forest, Gradient Boosting.
Evaluation metrics: RMSE, MAE, R². The saved model is `models/best_model.pkl`

## 6. Ethics & Limitations
- Historical bias in box office and reviewer demographics
- Missing data and survivorship bias
- Use caution when using models for decision-making

## 7. Reproducibility
- See `README.md` for instructions.
