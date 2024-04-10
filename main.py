import streamlit as st
from home import home_page
from signup import signup_page
from location_tracker import location_tracker_page
from payment_options import payment_options_page

# Define the layout of the sidebar navigation
def navigation():
    st.sidebar.title("Navigation Bar")
    option = st.sidebar.radio("Go to", ["Home Page", "Sign Up", "Location Tracker", "Payment Options"])
    return option

# Main function to control navigation
def main():
    st.set_page_config(page_title="Toll Payers", page_icon=":car:")
    #st.title("Streamlit Navigation Example")
    option = navigation()

    # Render corresponding page based on selected option
    if option == "Home Page":
        home_page()
    elif option == "Sign Up":
        signup_page()
    elif option == "Location Tracker":
        location_tracker_page()
    elif option == "Payment Options":
        payment_options_page()

if __name__ == "__main__":
    main()

