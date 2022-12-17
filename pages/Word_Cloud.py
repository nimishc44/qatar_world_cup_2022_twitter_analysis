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
from pages.Twitter_Dataset import data

st.set_page_config(layout="wide")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.sidebar.success("This section helps you to visualize the Word Cloud created using the most popular words used in the tweets. The bigger the font size of the word, the more frequently the word was mentioned in the tweets.")

# Creating a new list to store all the tweets from the column tweet_text from our 5000 tweets
def funWordcloud():
    tweet_list = list(data['tweet_text'])
    # Creating an empty string to store all the elements of the tweet_list we created above
    # Running a for loop in our tweet_list and each element of our tweet_list in a single string! 
    tweet_long_string = ''
    for t in tweet_list:
        tweet_long_string = tweet_long_string + t
    w = WordCloud()
    stop_words = list(w.stopwords)
    custom_stop_words = ['https','user', 'need', 'tweet','rt','t','co', 'amp','IDR','min','XT','MINS', 'will']
    stop_words = set(stop_words + custom_stop_words)

    wordcloud = WordCloud(background_color = '#0f1116', width = 1920, height = 1080, collocations = False, stopwords = stop_words).generate(tweet_long_string)

    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Display the generated image:
    plt.axis("off")
    plt.figure( figsize=(20,10), facecolor='#0f1116')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
    st.pyplot()
    return

def deleteWordcloud():
    return

st.header("Word Cloud")
generateWordCloudCheckbox = st.checkbox('Display Word Cloud')
if generateWordCloudCheckbox:
    funWordcloud()