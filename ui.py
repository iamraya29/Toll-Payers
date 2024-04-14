import streamlit as st

def update_ui(is_within_bounds):
    if is_within_bounds:
        st.write("Your vehicle is within the toll booth area. Please proceed to make a payment.")
    else:
        st.write("Your vehicle is outside the toll booth area.")
