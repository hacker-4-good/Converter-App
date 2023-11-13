import streamlit as st
import pymongo 

@st.cache_resource
def init_connection():
    return pymongo.MongoClient("mongodb://localhost:27017/")

client = init_connection()

@st.cache_data(ttl=600)
def get_data():
    db = client.mydb 
    items = db.mycollection.find()
    items = list(items)
    return items

items = get_data()

for item in items:
    st.write(f"{item['name']} has a: {item['pet']}")