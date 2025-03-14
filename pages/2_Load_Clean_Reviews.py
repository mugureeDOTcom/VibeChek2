import streamlit as st
import pandas as pd
import requests

# Load API key securely from Streamlit secrets
SERP_API_KEY = st.secrets["serpapi"]["api_key"]


st.title("📂 Load & Clean Reviews")

# Check if Place ID is available
if "place_id" not in st.session_state:
    st.error("❌ No Place ID found! Please go back and search for a business first.")
    st.stop()

place_id = st.session_state["place_id"]
business_name = st.session_state["business_name"]

st.write(f"📍 **Business Name:** {business_name}")
st.write(f"📌 **Place ID:** {place_id}")

# Function to fetch reviews from Serp API
def fetch_reviews(place_id):
    url = f"https://serpapi.com/search.json?engine=google_maps_reviews&place_id={place_id}&api_key={SERP_API_KEY}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "reviews" in data:
            reviews = data["reviews"]
            df = pd.DataFrame(reviews)[["date", "rating", "snippet"]]
            return df
        else:
            return None
    else:
        return None

# Fetch reviews when button is clicked
if st.button("📥 Fetch Reviews"):
    reviews_df = fetch_reviews(place_id)

    if reviews_df is not None:
        st.success("✅ Reviews Loaded Successfully!")
        st.dataframe(reviews_df)

        # Download raw reviews
        csv_raw = reviews_df.to_csv(index=False).encode("utf-8")
        st.download_button("📩 Download Raw Reviews", data=csv_raw, file_name="raw_reviews.csv", mime="text/csv")

        # Data Cleaning
        reviews_df.drop_duplicates(inplace=True)  # Remove duplicates
        reviews_df.dropna(inplace=True)  # Remove missing values
        reviews_df["snippet"] = reviews_df["snippet"].str.replace(r'[^\w\s]', '', regex=True)  # Remove special characters

        # Display cleaned reviews
        st.subheader("🧼 Cleaned Reviews")
        st.dataframe(reviews_df)

        # Download cleaned reviews
        csv_clean = reviews_df.to_csv(index=False).encode("utf-8")
        st.download_button("📩 Download Cleaned Reviews", data=csv_clean, file_name="cleaned_reviews.csv", mime="text/csv")

        # Button to move to Sentiment Analysis
        if st.button("📊 Sentiment Analysis"):
            st.session_state["cleaned_reviews"] = reviews_df
            st.switch_page("sentiment_analysis.py")

    else:
        st.error("❌ Failed to fetch reviews. Try again later or check the Place ID.")

