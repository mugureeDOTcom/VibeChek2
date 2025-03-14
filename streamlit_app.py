import streamlit as st
from sidebar import sidebar  # Import sidebar function

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 Welcome"

# Set up sidebar
page = sidebar()

# Welcome Page Content
if page == "🏠 Welcome":
    st.title("🎉 Welcome to Customer Review Sentiment Analyzer")
    st.write("Easily analyze customer feedback and gain insights!")

    st.image("media/welcome.webp", use_container_width=True)  # Add a nice banner image
    st.write("Click on **Find Business** in the sidebar or use the button below to get started.")

    # Add a "Find Business" button
    if st.button("🔍 Find Business"):
        st.session_state.current_page = "🔍 Find Business"

# Page Routing Based on Session State
if st.session_state.current_page == "🔍 Find Business":
    st.experimental_set_query_params(page="find_business")  # Preserves page state
    st.switch_page("pages/1_Find_Business.py")
elif st.session_state.current_page == "📥 Load & Clean Reviews":
    st.experimental_set_query_params(page="load_clean_reviews")
    st.switch_page("pages/2_Load_Clean_Reviews.py")
elif st.session_state.current_page == "📊 Sentiment Analysis":
    st.experimental_set_query_params(page="sentiment_analysis")
    st.switch_page("pages/3_Sentiment_Analysis.py")
elif st.session_state.current_page == "🤖 AI Recommendations":
    st.experimental_set_query_params(page="ai_recommendations")
    st.switch_page("pages/4_AI_Recommendations.py")
elif st.session_state.current_page == "✅ Exit":
    st.experimental_set_query_params(page="exit")
    st.switch_page("pages/5_Exit.py")
