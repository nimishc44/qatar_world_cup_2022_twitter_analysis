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
from pages.Popularity_Analysis import tweet_list
import plotly.express as px
import statistics as sx

#st.set_page_config(layout="wide")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.sidebar.success("This section helps to analyze the subjectivity and polarity scores of the tweets.")

st.header("Sentiment Analysis")

tab1, tab2 = st.tabs(["Polarity", "Subjectivity"])

with tab1:
    st.header("Polarity Scores")
    # Creating empty lists for polarity and subjectivity scores respectively and finding out their means
    def polarityHistogram():
        pol_list = []
        for t in tweet_list:
            tb = TextBlob(t)
            pol_list.append(tb.sentiment.polarity)
        pol_avg = mean(pol_list)
        pol_dev = sx.stdev(pol_list)
        st.metric(label="Average Subjectivity Score", value=str(round(pol_avg, 2)), delta=str(round(pol_dev, 2)))
        # Building polarity score histogram
        fig = px.histogram(pol_list, nbins = 20, color_discrete_sequence=['indianred'])
        fig.update_layout(
            xaxis_title_text='Polarity Scores', # xaxis label
            yaxis_title_text='Tweet Count', # yaxis label
            bargap=0.2, # gap between bars of adjacent location coordinates
            bargroupgap=0.1 # gap between bars of the same location coordinates
        )
        st.plotly_chart(fig)
        return

    generatePolarityHistogram = st.checkbox("Display Polarity Score Histogram")
    if generatePolarityHistogram:
        polarityHistogram()

with tab2:
    st.header("Subjectivity Scores")
    def subjectivityHistogram():
        sub_list = []
        for t in tweet_list:
            tb = TextBlob(t)
            sub_list.append(tb.sentiment.subjectivity)
        sub_avg = mean(sub_list)
        sub_dev = sx.stdev(sub_list)
        st.metric(label="Average Subjectivity Score", value=str(round(sub_avg, 2)), delta=str(round(sub_dev, 2)))
        # Building Subjectivity score histogram
        fig = px.histogram(sub_list, nbins = 20, color_discrete_sequence=['green'])
        fig.update_layout(
            xaxis_title_text='Subjectivity Scores', # xaxis label
            yaxis_title_text='Tweet Count', # yaxis label
            bargap=0.2, # gap between bars of adjacent location coordinates
            bargroupgap=0.1 # gap between bars of the same location coordinates
        )
        st.plotly_chart(fig)
        return

    generateSubjectivityHistogram = st.checkbox("Display Subjectivity Score Histogram")
    if generateSubjectivityHistogram:
        subjectivityHistogram()