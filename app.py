import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(
    page_title="Spotify Music Analysis",
    page_icon="🎵",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/dataset.csv')
    df = df.drop(columns='Unnamed: 0')
    df = df.dropna()
    df = df.drop_duplicates()
    df['duration_min'] = df['duration_ms'] / 60000
    return df

df = load_data()

# Header
st.title("🎵 Spotify Music Analysis")
st.markdown("""
Exploratory Data Analysis of 113,000+ Spotify tracks across 125 genres.
This dashboard presents the key findings from the analysis.
""")

st.divider()


# Section 1 - Top genres by popularity
st.header("🎼 Top 10 Genres by Average Popularity")

top_genres = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(top_genres.index[::-1], top_genres.values[::-1], color='lightgreen')
ax.set_xlabel('Average Popularity')
ax.set_ylabel('Genre')
plt.tight_layout()

st.pyplot(fig)


st.divider()

# Section 2 - Top artists by popularity
st.header("🎤 Top 10 Artists by Average Popularity")

top_artists = df.groupby('artists')['popularity'].mean().sort_values(ascending=False).head(10)

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.barh(top_artists.index[::-1], top_artists.values[::-1], color='lightblue')
ax2.set_xlabel('Average Popularity')
ax2.set_ylabel('Artists')
plt.tight_layout()

st.pyplot(fig2)