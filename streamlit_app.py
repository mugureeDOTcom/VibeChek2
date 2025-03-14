import streamlit as st

# Page Title
st.set_page_config(page_title="Customer Review Sentiment Analyzer", page_icon="📝")

# Welcome Section
st.title("📊 Customer Review Sentiment Analyzer")
st.subheader("Turn customer feedback into meaningful insights.")

st.write("""
Welcome to the **Customer Review Sentiment Analyzer**!  
This tool helps you analyze customer reviews from different businesses  
to extract insights and improve decision-making.
""")

# How It Works (Optional)
with st.expander("🔎 How It Works"):
    st.write("""
    1. **Find a Business** – Search for a business and get its Place ID.
    2. **Load & Clean Reviews** – Fetch and preprocess customer reviews.
    3. **Analyze Sentiment** – Visualize trends, word clouds, and key insights.
    4. **AI Recommendations** – Get suggestions to improve based on customer feedback.
    5. **Download Reports** – Export raw reviews, cleaned data, and recommendations.
    """)

# Get Started Button
if st.button("🚀 Get Started"):
    st.switch_page("pages/1_Find_Business.py")  # Redirect to the next page

