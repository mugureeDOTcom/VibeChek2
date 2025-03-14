import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim

st.title("🔍 Find Business & Copy Place ID")

# Initialize session state variables if they don't exist
if "place_id" not in st.session_state:
    st.session_state["place_id"] = ""

if "business_name" not in st.session_state:
    st.session_state["business_name"] = ""

# User input for business search
business_name = st.text_input("Enter Business Name:", "")

if st.button("Search"):
    if business_name:
        geolocator = Nominatim(user_agent="business_locator")
        location = geolocator.geocode(business_name)

        if location:
            st.success(f"📍 Found: {location.address}")
            st.write(f"**Latitude:** {location.latitude}")
            st.write(f"**Longitude:** {location.longitude}")

            # ✅ Store values in session state before switching pages
            st.session_state["place_id"] = f"{location.latitude},{location.longitude}"
            st.session_state["business_name"] = location.address

        else:
            st.error("❌ Business not found. Try a different name.")
    else:
        st.warning("⚠ Please enter a business name to search.")

# Display Place ID
st.text_input("📌 Place ID:", st.session_state["place_id"], key="place_id", disabled=True)

# Display map if location exists
if st.session_state["place_id"]:
    m = folium.Map(location=[float(coord) for coord in st.session_state["place_id"].split(",")], zoom_start=15)
    folium.Marker([float(coord) for coord in st.session_state["place_id"].split(",")], popup=st.session_state["business_name"]).add_to(m)
    folium_static(m)

    # ✅ FIX: Ensure session state is set before navigation
    if st.button("➡ Load Reviews"):
        st.switch_page("pages/2_Load_Clean_Reviews.py")
