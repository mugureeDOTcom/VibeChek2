import streamlit as st

st.set_page_config(page_title="Customer Review Sentiment Analyzer", layout="wide")

st.title("📊 Customer Review Sentiment Analyzer")
st.write("Welcome! This tool helps you analyze customer feedback using AI-driven sentiment analysis.")

st.markdown("### How It Works")
st.write("""
1. **Find a Business**: Enter the business name to get the Place ID.
2. **Load Reviews**: Fetch, clean, and download reviews.
3. **Analyze Reviews**: Get insights with dashboards, heatmaps, and word clouds.
4. **AI Recommendations**: Receive business improvement suggestions.
5. **Exit or Restart**: Wrap up or start over.
""")

st.sidebar.success("Use the sidebar to navigate between pages.")
