import streamlit as st
import joblib
import pandas as pd
import re
import warnings

warnings.simplefilter("ignore")

data = pd.read_csv("Streamlit/LanguageDetection/Language_Detection.csv")


X = data["Text"]
y = data["Language"]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

data_list = []

for text in X:
    
    text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
    text = re.sub(r'[[]]', ' ', text)
    
    text = text.lower()
    
    data_list.append(text)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(data_list).toarray()

model = joblib.load('Streamlit/LanguageDetection/Language_Detection.pkl')

def predict(text):
    x = cv.transform([text]).toarray()
    lang = model.predict(x)
    lang = le.inverse_transform(lang)
    return lang[0]

st.title("Language Detection 🗨️🧔🏻")

text = st.text_input("Enter the text")

if st.button('Find'):
    ans = predict(text)
    st.text(ans)