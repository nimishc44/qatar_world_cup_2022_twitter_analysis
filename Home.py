import streamlit as st
import nltk
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
from pprint import pprint
from wordcloud import WordCloud 
from collections import Counter 
from textblob import TextBlob
from statistics import mean
from st_pages import Page, show_pages, add_page_title
nltk.download('punkt')
nltk.download('stopwords')

st.set_page_config(layout="wide")

hide_streamlit_style = """
            <style>
            footer {visibility: visible;}
            footer:after {content: '© 2022, Nimish Chauhan'; display: block; position: relative; color: indianred;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.session_state.update(st.session_state)

# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("Home.py", "Home", "⚽️"),
        Page("pages/Twitter_Dataset.py", "Twitter Dataset", "🐦"),
        Page("pages/Popularity_Analysis.py", "Popularity Analysis", "👯"),
        Page("pages/Word_Cloud.py", "Word Cloud", "🏟️"),
        Page("pages/Sentiment_Analysis.py", "Sentiment Analysis", "🧐")
    ]
)

st.sidebar.success("Select from the options above")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url("https://assets.foxdcg.com/dpp-uploaded/images/fifa-world-cup-team-previews/chip_soccer_fifa_world_cup_qatar_team_previews_2022-keyart.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

a, b = st.columns([1, 20])

with a:
    st.text("")
    st.image("icons8-twitter-48.png", width=50)
with b:
    st.title("Qatar World Cup 2022")

st.markdown("""
            ## Twitter Analysis
            """)

st.markdown("""
            This application tries to analyze a twitter dataset of 5000 tweets based on the keywords related to Qatar Fifa World Cup 2022.
            """)

st.markdown("""
    **👈 Select a demo from the sidebar** to see some analysis!
    ### Following are some of the challenges that this project tackles:
    - Efficiently scrubbing throught the raw twitter dataset.
    - Popularity analysis of the most common words, popular tweets, retweets and influential users.
    - Creating a **Word Cloud** out of the most popular and frequently occuring words.
    - Sentiment analysis by evaluating the polarity and the subjetivity scores.
""")