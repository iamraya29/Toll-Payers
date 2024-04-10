import streamlit as st

def signup_page():
    st.title("Sign Up")

    # Input fields for user registration
    username = st.text_input("Username", placeholder="Enter your username")
    email = st.text_input("Email", placeholder="Enter your email")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")

    # Center align the input fields and the button
    st.markdown(
        """
        <style>
        .stTextInput {
            text-align: center;
        }
        .stButton>button {
            width: 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sign up button
    if st.button("Sign Up"):
        if password == confirm_password:
            # You can perform signup logic here, such as adding the user to a database
            st.success("Sign up successful!")
        else:
            st.error("Passwords do not match.")

if __name__ == "__main__":
    signup_page()

