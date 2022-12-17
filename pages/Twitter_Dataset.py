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

st.set_page_config(layout="wide")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.header('Raw Twitter Data')
st.sidebar.success("This section helps you to scrub through the raw twitter dataset used in this analysis.")

DATA_URL = ('/Users/nimish/Documents/Important Documents/UBC - MM/Subjects/Period 2/BA 515 Fundamentals of Analysis and Tech/Streamlit Project/worldcup_tweets.csv')
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, index_col=0)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(6000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("")

st.write(data)