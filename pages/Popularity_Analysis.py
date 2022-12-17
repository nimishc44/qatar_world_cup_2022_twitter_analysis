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

#st.set_page_config(layout="wide")

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.sidebar.success("This section helps to analyze the most popular keywords, hashtags, influential users and retweets")

st.header("Popularity Analysis")

# Creating a list to store the first column which contains the 5000 tweets that are related with Qatar Worldcup 2022.
tweet_list = list(data['tweet_text'])

# Creating an empty list to store all the words from the 5000 tweets
word_list_with_stopwords = []

# Running a loop to seperate every word whenever we encounter a space and changing everything to lowercase 
for t in tweet_list:
    word_list_with_stopwords.extend(t.lower().split())

# Now we have to extract the stopwords, but first we have to know the stopwords and state them in our code. In the beggining we downloaded from nltk the package with the stopwords and we'll reuse that
stop_words = nltk.corpus.stopwords.words('english')

# Extending the stopwords list to better fit our needs in this project
new_stopwords = ["rt", "rt,", "jt", "jt,", "amp", "&amp", "&amp;", "http", "https", "http:", "https:", "t", "co", "xt", "e.g.", "br", "sr", "idr", "quoted", "tweet", "click", "link"]
stop_words.extend(new_stopwords)
word_list_without_stopwords = []
for w in word_list_with_stopwords:
    if w not in stop_words and len(w) > 1:
        word_list_without_stopwords.append(w)

tab1, tab2, tab3 = st.tabs(["Words and Hashtags", "Users", "Retweets"])

with tab1:
    # In the beginning we imported all the packages needed for our project and the Counter package will help us to see how many times a word appears in our list.
    numberOfWordsToBeSelected = st.slider("Select the number of most popular words: ", min_value=1, max_value=100, value=3)
    st.write("The ", numberOfWordsToBeSelected, "most popular words are: ")
    st.table(Counter(word_list_without_stopwords).most_common(numberOfWordsToBeSelected))
    
    # Defining a new empty list to store all the hashtags from our tweets
    hashtags = []
    for w in word_list_without_stopwords:
        if w.startswith("#") and len(w)>1:
            #Using append to store the hashtags that specify the above condition into the hashtags list
            hashtags.append(w)

    # Using "Counter" and "most_common" to store the most common hashtags in new list with the name ten_most_popular_hashtags
    numberOfHashtagsToBeSelected = st.slider("Select the number of most popular hashtags: ", min_value=1, max_value=100, value=3)
    st.write("The ", numberOfHashtagsToBeSelected, "most popular hashtags are: ")
    st.table(Counter(hashtags).most_common(numberOfHashtagsToBeSelected))
    
with tab2:
    # Defining a new empty list to store all the usernames from our tweets
    # Rest of the process remains similar to what we did in the previous question
    usernames = []
    for u in word_list_without_stopwords:
        if u.startswith("@") and len(u) > 1:
            usernames.append(u)
    numberOfUsernamesToBeSelected = st.slider("Select the number of most popular usernames: ", min_value=1, max_value=100, value=3)
    st.write("The ", numberOfUsernamesToBeSelected, "most popular usernames are: ")
    st.table(Counter(usernames).most_common(numberOfUsernamesToBeSelected))
    
    # Simply creating a list which only contains the "user_screen_names" of the people who are tweeting, and then printing the most common user
    username_list = list(data["user_screen_name"])
    numberOfMostVocalUsers = st.slider("Select the number of most vocal users: ", min_value=1, max_value=100, value=3)
    st.write("The ", numberOfMostVocalUsers, "most frequently tweeting people is/are: ")
    st.table(Counter(username_list).most_common(numberOfMostVocalUsers))
    
    # Creating a new data frame which is based on our original data frame but only has rows and columns where the column value of "is_retweet" is true
    retweet_df = data[data["is_retweet"] == True]
    retweet_df["influence_score"] = retweet_df["source_user_followers_count"] + retweet_df["source_user_friends_count"] + retweet_df["source_user_listed_count"] + retweet_df["source_user_favourites_count"]
    numberOfInfluencersToBeSelected = st.slider("Select the number of influencers: ", min_value=1, max_value=100, value=3)
    most_influential_user = retweet_df.sort_values(["influence_score"], ascending = False).head(numberOfInfluencersToBeSelected)["user_name"]
    st.write("The ", numberOfInfluencersToBeSelected,"most influential user(s) is/are: ")
    st.table(most_influential_user)

with tab3:
    # This question also follows the similar approach as the last question
    retweet_df["retweet_influence_score"] = retweet_df["source_tweet_quote_count"] + retweet_df["source_tweet_reply_count"] + retweet_df["source_tweet_retweet_count"] + retweet_df["source_tweet_favorite_count"]
    numberOfRetweetsToBeSelected = st.slider("Select the number of popular retweets: ", min_value=1, max_value=100, value=3)
    most_influential_retweet = retweet_df.sort_values(["retweet_influence_score"], ascending = False).head(numberOfRetweetsToBeSelected)["tweet_text"]
    st.write("The ", numberOfRetweetsToBeSelected,"most influential retweet(s) is/are: ")
    st.table(most_influential_retweet)