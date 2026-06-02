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



# Total tracks
total_tracks = df.shape[0]


# Total Genres
total_genres = df['track_genre'].nunique()


# Total artists
total_artists = df['artists'].nunique()


# Average popularity
average_popularity = df['popularity'].mean()


col1, col2, col3, col4 = st.columns(4)


# --TOTAL TRACKS--
with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Tracks</div>
        <div class="kpi-value">{total_tracks:,}</div>
        <div class="kpi-meta">songs analyzed</div>
    </div>
    """, unsafe_allow_html=True)


# --TOTAL GENRES--
with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Genres</div>
        <div class="kpi-value">{total_genres:,}</div>
        <div class="kpi-meta">music categories</div>
    </div>
    """, unsafe_allow_html=True)


# --TOTAL ARTISTS--
with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Artists</div>
        <div class="kpi-value">{total_artists:,}</div>
        <div class="kpi-meta">unique artists</div>
    </div>
    """, unsafe_allow_html=True)


# --AVERAGE POPULARITY--
with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Total Tracks</div>
        <div class="kpi-value">{round(average_popularity, 2):,}</div>
        <div class="kpi-meta">out of 100</div>
    </div>
    """, unsafe_allow_html=True)



# Genre Analysis
st.markdown('<div class="section-title">🎼 Genre Analysis</div>', unsafe_allow_html=True)

top_genres = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(10)

fig = px.bar(
    top_genres,
    x=top_genres.values,      # valores numéricos
    y=top_genres.index,      # categorías
    orientation='h',    # horizontal
    color_discrete_sequence=['#1DB954'],  # color Spotify
    labels={'y': '', 'x': 'Average Popularity'},
    title='Top 10 Genres by Average Popularity'
)

st.plotly_chart(fig, use_container_width=True)



# Top 10 Artists by Average Popularity
st.markdown('<div class="section-title">🎼 Artists Analysis</div>', unsafe_allow_html=True)

top_artists = df.groupby('artists')['popularity'].mean().sort_values(ascending = False).head(10)

fig = px.bar(
    top_artists,
    x=top_artists.values,      # valores numéricos
    y=top_artists.index,      # categorías
    orientation='h',    # horizontal
    color_discrete_sequence=['#1DB954'],  # color Spotify
    labels={'y': '', 'x': 'Average Popularity'},
    title='Top 10 Artists by Average Popularity'
)

st.plotly_chart(fig, use_container_width=True)



# Top 10 Genres by Average Energy
st.markdown('<div class="section-title">🎼 Average Energy Analysis</div>', unsafe_allow_html=True)

top_genres_energy = df.groupby('track_genre')['energy'].mean().sort_values(ascending = False).head(10)

fig = px.bar(
    top_genres_energy,
    x=top_genres_energy.values,      # valores numéricos
    y=top_genres_energy.index,      # categorías
    orientation='h',    # horizontal
    color_discrete_sequence=['#1DB954'],  # color Spotify
    labels={'y': '', 'x': 'Average Energy'},
    title='Top 10 Genres by Average Energy'
)

st.plotly_chart(fig, use_container_width=True)



# Song duration vs Popularity
st.markdown('<div class="section-title">⏱️ Duration Analysis</div>', unsafe_allow_html=True)

df_filtered = df[df['duration_min'] < 10]

fig = px.scatter(
    df_filtered,
    title='Song Duration vs Popularity',
    labels={'x': 'Duration (minutes)', 'y': 'Popularity'},
    x = df_filtered['duration_min'],
    y = df_filtered['popularity'],
    color_discrete_sequence=['#1DB954']
)

st.plotly_chart(fig, use_container_width=True)



# Explicit vs Loudness
st.markdown('<div class="section-title">🎼 Explicit vs Loudness Analysis</div>', unsafe_allow_html=True)

explicit_loudness = df.groupby('explicit')['loudness'].mean()

fig = px.bar(
    explicit_loudness,
    x=['Non-Explicit', 'Explicit'],      # valores numéricos
    y=explicit_loudness.values,      # categorías
    orientation='v',    # vertical
    color_discrete_sequence=['#1DB954'],  # color Spotify
    labels={'x': 'Song Type', 'y': 'Average Loudness (dB)'},
    title='Explicit vs Non-Explicit Songs: Average Loudness'
)

st.plotly_chart(fig, use_container_width=True)



# Key Conclusions
st.markdown('<div class="section-title">📝 Key Conclusions</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Finding 01</div>
        <div style="font-size:0.9rem; color:#FFFFFF; margin-top:8px;">
            1. Genre popularity drives platform and artist strategy: 
                Knowing which genres and artists are the most popular can significantly benefit both Spotify's 
                algorithm and artists themselves. Artists can identify which genres are gaining more relevance 
                among listeners, while Spotify's algorithm can use this information to recommend songs of these 
                genres more frequently.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Finding 02</div>
        <div style="font-size:0.9rem; color:#FFFFFF; margin-top:8px;">
            2. Collaborations significantly boost artist popularity: 
                Artists can leverage collaborations to boost both their own popularity and
                that of their songs. Beyond popularity metrics, collaborations can also accelerate
                career growth and help build a larger combined fan base between the artists involved.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Finding 03</div>
        <div style="font-size:0.9rem; color:#FFFFFF; margin-top:8px;">
            3. Song duration impacts popularity: 
                Understanding that song duration significantly influences popularity can improve the creative
                process for both producers and artists. Knowing that songs between 3 and 4 minutes tend to perform
                better can guide them toward an optimal duration: not too short, and not too long.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; color:#535353; font-size:0.75rem; 
            margin-top:48px; padding:20px; border-top:1px solid #2a2a2a;">
    Spotify Music Analysis · Emmanuel Mora Grajales · Portfolio Project · 2026
</div>
""", unsafe_allow_html=True)