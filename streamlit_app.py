import streamlit as st
from sidebar import sidebar  # Import sidebar function

# Set up sidebar
page = sidebar()

# Welcome Page Content
if page == "🏠 Welcome":
    st.title("🎉 Welcome to Customer Review Sentiment Analyzer")
    st.write("Easily analyze customer feedback and gain insights!")

    st.image("media/welcome.webp", use_container_width=True)
    st.write("Click on **Find Business** in the sidebar or use the button below to get started.")

    # Add a "Find Business" button
if st.button("🔍 Find Business"):
    st.query_params.clear()  # Clear existing params to avoid conflicts
    st.query_params["page"] = "Find Business"
    st.rerun()  # Refresh the app with new parameters


# Navigation Based on Query Parameters
if "page" in st.query_params:
    if st.query_params["page"] == "Find Business":
        st.experimental_set_query_params(page="Find Business")
        st.experimental_rerun()
    elif st.query_params["page"] == "Load & Clean Reviews":
        st.experimental_set_query_params(page="Load & Clean Reviews")
        st.experimental_rerun()
    elif st.query_params["page"] == "Sentiment Analysis":
        st.experimental_set_query_params(page="Sentiment Analysis")
        st.experimental_rerun()
    elif st.query_params["page"] == "AI Recommendations":
        st.experimental_set_query_params(page="AI Recommendations")
        st.experimental_rerun()
    elif st.query_params["page"] == "Exit":
        st.experimental_set_query_params(page="Exit")
        st.experimental_rerun()
