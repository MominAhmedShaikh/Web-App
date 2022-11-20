import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()


st.title('Real Time Sentiment Analysis')

string2 = st.text_input('Enter your text')
score2 = sentiment.polarity_scores(string2)

s = score2['compound']


if s < 0:
    st.text("Negative")
elif s == 0:
    st.text("Neutral")
else:
    st.text("Positive")


