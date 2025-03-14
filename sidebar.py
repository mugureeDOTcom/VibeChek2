import streamlit as st

def sidebar():
    st.sidebar.title("📌 Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["🏠 Welcome", "🔍 Find Business", "📥 Load & Clean Reviews", "📊 Sentiment Analysis", "🤖 AI Recommendations", "✅ Exit"]
    )

    return page  # This will be used to navigate between pages
