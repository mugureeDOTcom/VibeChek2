import streamlit as st

# Set up sidebar navigation
def sidebar():
    page = st.sidebar.radio(
        "Navigation",
        ["🏠 Welcome", "🔍 Find Business", "📥 Load & Clean Reviews", 
         "📊 Sentiment Analysis", "🤖 AI Recommendations", "✅ Exit"]
    )

    if page == "🏠 Welcome":
        st.switch_page("streamlit_app.py")  
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

    return page
