import streamlit as st
from scraper import scraper

st.title("Welcome, please enter the url")

URL = st.text_input("url", label_visibility = "hidden")

if st.button("Get Data"):
    if URL:
        d = scraper(URL)
        print(d)
        st.text("Product Name : {}".format("Scraped Product Name"))
        st.text("ASIN : {}".format("Scraped ASIN"))
        st.text("Price : {}".format("Scraped Price"))
    else:
        st.error("Please enter a valid URL.")