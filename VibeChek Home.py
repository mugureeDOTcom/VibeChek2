import streamlit as st

# Set full-width layout
st.set_page_config(layout="wide")  

# Function to navigate between pages
def navigate_to(page):
    st.session_state.page = page
    st.rerun()

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "🏠 Welcome"

# --- Page Routing ---
if st.session_state.page == "🏠 Welcome":
    st.title("🎉 Welcome to Customer Review Sentiment Analyzer")
    st.write("Easily analyze customer feedback and gain insights!")

    st.image("media/welcome.webp", use_container_width=True)
    st.write("Click below to start finding businesses.")

    if st.button("🔍 Find Business"):
        navigate_to("🔍 Find Business")

elif st.session_state.page == "🔍 Find Business":
    st.title("🔍 Find a Business")
    st.write("Search for a business and copy its Place ID.")

    if st.button("➡ Load & Clean Reviews"):
        navigate_to("Load & Clean Reviews")

elif st.session_state.page == "Load & Clean Reviews":
    st.title("📂 Load & Clean Reviews")
    st.write("Upload a file or fetch reviews automatically.")

    if st.button("📊 Sentiment Analysis"):
        navigate_to("Sentiment Analysis")

elif st.session_state.page == "Sentiment Analysis":
    st.title("📊 Sentiment Analysis")
    st.write("Analyze customer sentiment and generate insights.")

    if st.button("🤖 AI Recommendations"):
        navigate_to("AI Recommendations")

elif st.session_state.page == "AI Recommendations":
    st.title("🤖 AI Recommendations")
    st.write("Get AI-powered suggestions based on reviews.")

    if st.button("🏁 Exit / Start Over"):
        navigate_to("🏠 Welcome")
