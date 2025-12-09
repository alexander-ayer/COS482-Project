
<!-- PROJECT TITLE -->
<h1 align="center">🎬 Predicting Movie Success using Machine Learning</h1>

<p align="center">
  <img src="https://img.shields.io/badge/ML-Prediction-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/WebScraping-Data-orange?style=for-the-badge" />
</p>

<p align="center">
  Predicting movie success using OMDb API metadata, The Numbers box-office scraping, and machine learning pipelines.
  <br />
  <a href="#-features"><strong>Explore the features »</strong></a>
  <br />
  <a href="https://colab.research.google.com/drive/12ZMoM0faPVrxqWPihBCswuiV1XC78IEp#scrollTo=IMsC35bK03Ty">View Notebook</a>
  ·
  <a href="issues">Report Bug</a>
  ·
  <a href="issues">Request Feature</a>
</p>

---

## 🌟 Overview

This project builds a complete end-to-end machine learning system for **predicting worldwide box-office performance** using:

- 🎥 **OMDb API** → Movie metadata  
- 💰 **The Numbers** → Budget & worldwide gross scraping  
- 🧹 **Data Cleaning** + Feature engineering  
- 🤖 **ML Models** → Random Forest, Gradient Boosting, Linear Regression  
- 📊 **Visualizations** → Scatter plots, histograms, feature importances  
- 🧪 **Synthetic fallback dataset** for testing  
- 🚀 **Google Colab support**

---

## 🗂 Project Structure

```
movie-success-project/
│
├── data_raw/               
├── data_clean/             
│
├── src/
│   ├── data_collection.py 
│   ├── boxoffice_scraper.py
│   ├── cleaning.py         
│   ├── modeling.py         
│   └── utils.py
│
├── notebooks/
│   ├── movie_pipeline.ipynb
│   └── EDA.ipynb
│
├── visuals/
│   ├── scatter_budget_vs_worldwide.png
│   ├── hist_worldwide_gross.png
│   └── rf_feature_importances.png
│
├── models/
│   └── best_model.pkl 
│
├── report/
│   └── final_report.md
│
└── README.md
```

---

## 🚀 Features

### 🔍 **Data Collection**
- OMDb API metadata  
- Budget + box‑office scraping  
- Fuzzy title matching  
- Synthetic dataset generator  

### 🧹 **Data Cleaning**
- Numeric normalization  
- Missing value handling  
- Genre & cast parsing  
- Release decade extraction  

### 🤖 **ML Modeling**
- Random Forest  
- Gradient Boosting  
- Linear Regression  

Metrics:
- RMSE  
- MAE  
- R²  

---

## 🛠 Installation

```bash
git clone https://github.com/alexander-ayer/COS482-Project
cd movie-success-project
pip install -r requirements.txt
```

---

## 🔑 OMDb API Setup

```bash
export OMDB_API_KEY="cdd03cf8"
```

---

## 📥 Usage

### Synthetic data
```bash
python src/data_collection.py --generate-synthetic 2000
```

### OMDb fetch
```bash
python src/data_collection.py --omdb-key $OMDB_API_KEY --titles-file titles.txt
```

### Scraping budgets
```bash
python src/boxoffice_scraper.py
```

### Cleaning
```bash
python src/cleaning.py
```

### Training
```bash
python src/modeling.py
```

---

## 📊 Visualizations

- Budget vs Gross  
- Gross distribution  
- Feature importance  

---

## 🧠 Future Work

- TMDB API integration  
- NLP analysis of plots  
- Deep learning models  

---

## 👨‍💻 Author

**Vasu Patel & Alex Ayer**  
Computer Science | DATA Science  
