import streamlit as st
from sidebar import sidebar  # Import sidebar function

# Set up sidebar
page = sidebar()

# Welcome Page Content
if page == "🏠 Welcome":
    st.title("🎉 Welcome to Customer Review Sentiment Analyzer")
    st.write("Easily analyze customer feedback and gain insights!")

    st.image("media/welcome.webp", use_container_width=True)
  # Add a nice banner image
    st.write("Click on **Find Business** in the sidebar to get started.")

elif page == "🔍 Find Business":
    st.switch_page("pages/1_Find_Business.py")
elif page == "📥 Load & Clean Reviews":
    st.switch_page("pages/2_Load_Clean_Reviews.py")
elif page == "📊 Sentiment Analysis":
    st.switch_page("pages/3_Sentiment_Analysis.py")
elif page == "🤖 AI Recommendations":
    st.switch_page("pages/4_AI_Recommendations.py")
elif page == "✅ Exit":
    st.switch_page("pages/5_Exit.py")
