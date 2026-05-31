import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Spotify Music Analysis",
    page_icon="🎵",
    layout="wide"
)

# ─── SPOTIFY THEME ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;900&display=swap');

    html, body, [class*="css"] {
        background-color: #121212;
        color: #FFFFFF;
        font-family: 'Montserrat', sans-serif;
    }
    .stApp { background-color: #121212; }

    .main-header {
        background: linear-gradient(135deg, #1DB954 0%, #158a3e 50%, #121212 100%);
        border-radius: 16px;
        padding: 36px 40px;
        margin-bottom: 32px;
    }
    .main-header h1 {
        font-size: 2.2rem;
        font-weight: 900;
        color: #FFFFFF;
        margin: 0 0 6px 0;
    }
    .main-header p {
        font-size: 0.95rem;
        color: rgba(255,255,255,0.75);
        margin: 0;
    }
    .spotify-logo {
        font-size: 1rem;
        font-weight: 700;
        color: #1DB954;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    .section-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #FFFFFF;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin: 32px 0 16px 0;
        padding-left: 12px;
        border-left: 3px solid #1DB954;
    }
    .kpi-card {
        background: #1E1E1E;
        border-radius: 12px;
        padding: 20px 24px;
        border: 1px solid #2a2a2a;
    }
    .kpi-label {
        font-size: 0.72rem;
        font-weight: 600;
        color: #b3b3b3;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 10px;
    }
    .kpi-value {
        font-size: 2.1rem;
        font-weight: 900;
        color: #1DB954;
        line-height: 1;
    }
    .kpi-meta {
        font-size: 0.78rem;
        color: #727272;
        margin-top: 6px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ─── LOAD DATA ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv('data/dataset.csv')
    df = df.drop(columns='Unnamed: 0')
    df = df.dropna()
    df = df.drop_duplicates()
    df['duration_min'] = df['duration_ms'] / 60000
    return df

df = load_data()

# ─── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <div class="spotify-logo">🎵 Spotify · Music Analysis</div>
    <h1>Spotify Music Analysis Dashboard</h1>
    <p>Exploratory Data Analysis of 113,000+ tracks across 125 genres</p>
    <p>Author: Emmanuel Mora Grajales · Portfolio Project · 2026</p>
</div>
""", unsafe_allow_html=True)