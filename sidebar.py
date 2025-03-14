import streamlit as st

def sidebar():
    pages = {
        "🏠 Welcome": "streamlit_app.py",
        "🔍 Find Business": "pages/1_Find_Business.py",
        "📥 Load & Clean Reviews": "pages/2_Load_Clean_Reviews.py",
        "📊 Sentiment Analysis": "pages/3_Sentiment_Analysis.py",
        "🤖 AI Recommendations": "pages/4_AI_Recommendations.py",
        "✅ Exit": "pages/5_Exit.py"
    }

    # Read query parameter to set active page
    query_params = st.query_params
    current_page = query_params.get("page", "🏠 Welcome")  # Default to Welcome Page

    # Sidebar Navigation
    selected_page = st.sidebar.radio("Navigation", list(pages.keys()), index=list(pages.keys()).index(current_page))

    # Update query params only if user selects a new page
    if selected_page != current_page:
        st.query_params["page"] = selected_page
        st.rerun()

    return selected_page
