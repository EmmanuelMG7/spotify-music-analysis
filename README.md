# Spotify Music Analysis

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.2.3-green)
![Plotly](https://img.shields.io/badge/Plotly-6.1.2-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45.0-red)

## Data Source

Dataset: [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)  
Author: [MaharshiPandya](https://www.kaggle.com/maharshipandya)  
Platform: Kaggle  
License: This dataset is used for educational and portfolio purposes only.

## 📋 Overview

This project is an Exploratory Data Analysis (EDA) of a Spotify tracks dataset containing 113,000+ songs across 125 genres. 
The goal is to identify patterns and insights that could help artists, producers, and music platforms make data-driven decisions 
to maximize song popularity and listener engagement.

The dataset was sourced from Kaggle (MaharshiPandya) and includes audio features such as energy, danceability, loudness, tempo, and more.

## Business Questions

1. Which genres have the highest average popularity?
2. Which artists have the highest average popularity?
3. Do the most popular artists belong to the most popular genres?
4. Does an artist's popularity change if it's not a collaboration?
5. Do more energetic and danceable songs tend to be more popular?
6. Which genres have the highest average energy?
7. Are explicit songs more popular than non-explicit ones?
8. Does song duration influence popularity?
9. Does tempo influence popularity?
10. Do live songs have the same impact as instrumental or acoustic ones?
11. Do the most popular songs of an artist belong to the same album?
12. Does an explicit or danceable song necessarily have to be loud?


## 📊 Key Findings

**1. Genre popularity drives platform and artist strategy**
Knowing which genres and artists are the most popular can significantly benefit both Spotify's algorithm and artists themselves. Artists can identify which genres are gaining more relevance among listeners, while Spotify's algorithm can use this information to recommend songs of these genres more frequently.

**2. Collaborations significantly boost artist popularity**
Artists can leverage collaborations to boost both their own popularity and that of their songs. Beyond popularity metrics, collaborations can also accelerate career growth and help build a larger combined fan base between the artists involved.

**3. Song duration impacts popularity**
Understanding that song duration significantly influences popularity can improve the creative process for both producers and artists. Knowing that songs between 3 and 4 minutes tend to perform better can guide them toward an optimal duration: not too short, and not too long.


## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Main programming language |
| Pandas | Data manipulation and analysis |
| Matplotlib & Seaborn | Static visualizations in the notebook |
| Plotly | Interactive charts in the dashboard |
| Streamlit | Interactive web dashboard |
| Jupyter Notebook | Exploratory data analysis |
| Git & GitHub | Version control |


## 📁 Project Structure

```
spotify-music-analysis/
├── 📁 data/                 # Dataset and documentation
├── 📁 notebooks/            # Data Exploration
├── 📄 app.py                # Streamlit Dashboard
├── 📄 requirements.txt      # Dependencies
├── 📄 .gitignore
└── 📄 README.md             # Project Documentation
```


## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/emmanuelmg7/spotify-music-analysis.git
cd spotify-music-analysis
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the dataset
Download the dataset from [Kaggle](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset) and place it in the `data/` folder as `dataset.csv`.

### 5. Run the notebook
```bash
jupyter notebook notebooks/01_exploration.ipynb
```

### 6. Run the dashboard
```bash
streamlit run app.py
```



## 📈 Dashboard

**Live Dashboard:** [(https://spotify-music-analysis-emmanuelmg7.streamlit.app/)]

The dashboard includes:
- KPI Cards with Total Tracks, Total Genres, Total Artists & Average Popularity
- 


