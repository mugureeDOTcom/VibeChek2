import streamlit as st

def under_construction(page_name):
    st.title(f"🚧 {page_name} - Under Construction 🚧")
    st.write("We're working hard to bring this feature to life. Stay tuned!")
    
    st.image("media/under_construction.webp", use_container_width=True)  # Add an image if available
    
    st.info("🔙 Use the sidebar to navigate to another page.")
