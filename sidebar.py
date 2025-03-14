import streamlit as st

def sidebar():
    st.sidebar.title("📌 Navigation")

    # Sidebar Navigation
    page = st.sidebar.radio(
        "Go to:",
        ["🏠 Welcome", "🔍 Find Business", "📥 Load & Clean Reviews",
         "📊 Sentiment Analysis", "🤖 AI Recommendations", "✅ Exit"]
    )

    # Update query parameters based on selection
    st.query_params["page"] = page
    st.rerun()

    return page
