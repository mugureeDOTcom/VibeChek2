import streamlit as st

# Set full-width layout
st.set_page_config(layout="wide")

st.title("🎉 Welcome to Customer Review Sentiment Analyzer")
st.write("Easily analyze customer feedback and gain insights!")

st.image("media/welcome.webp", use_container_width=True)
st.write("Click below to start finding businesses.")

if st.button("🔍 Find Business & Get Place ID"):
    st.switch_page("pages/1_Find_Business.py")  # Redirects to the first page
