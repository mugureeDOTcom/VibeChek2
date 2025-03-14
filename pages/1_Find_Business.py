import streamlit as st

st.title("🔍 Find Business")
st.write("Search for a business, get its Place ID, and analyze its customer reviews.")

# Ensure the page is correctly set via query parameters
if st.query_params.get("page") != "Find Business":
    st.query_params["page"] = "Find Business"
    st.rerun()

# Embedded Google Place ID Finder (iframe)
st.write("Use the embedded map below to find your business and copy its Place ID.")
st.markdown("""
    <iframe src="https://developers-dot-devsite-v2-prod.appspot.com/maps/documentation/utils/geocoder" 
    width="100%" height="450"></iframe>
""", unsafe_allow_html=True)

# Input for Place ID
place_id = st.text_input("📍 Enter or Paste Place ID here:")

if place_id:
    st.success(f"✅ Place ID copied: `{place_id}`")
else:
    st.warning("⚠️ No Place ID entered yet.")

# Navigation Buttons
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("⬅ Back to Home"):
        st.query_params["page"] = "🏠 Welcome"
        st.rerun()

with col2:
    if st.button("➡ Proceed to Load Reviews"):
        st.query_params["page"] = "Load & Clean Reviews"
        st.rerun()
