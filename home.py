import streamlit as st
from PIL import Image

def home_page():
    st.title("Welcome to Toll Tax Tracker")

    # Add images from local gallery
    image1 = Image.open(r"C:\Users\Malay Chandan Ghosh\Desktop\Mini Project Sem 4\Screenshot (437).png") 
    # Use raw string (r"") or replace backslashes with forward slashes
    # Add more images as needed
    # image2 = Image.open(r"path/to/your/image2.jpg")

    st.image(image1, caption="Toll System Of India")

    st.write(
        """
        ## Importance of Toll Tax

        Toll taxes play a crucial role in financing the maintenance and construction of roads and highways. 
        Here are some reasons why toll taxes are important:

        ### 1. Infrastructure Development
        Toll taxes help fund the construction and maintenance of highways, bridges, and other critical infrastructure. 
        These projects improve transportation efficiency and safety, leading to economic growth and development.

        ### 2. Revenue Generation
        Toll collection provides a significant source of revenue for government agencies responsible for road maintenance and upgrades. 
        This revenue can be used to cover operating costs, repay loans, and fund future infrastructure projects.

        ### 3. Traffic Management
        By imposing tolls on certain roads or lanes, authorities can manage traffic flow and reduce congestion. 
        Variable tolling strategies, such as congestion pricing, can incentivize drivers to use less congested routes or travel during off-peak hours.

        ### 4. User Pays Principle
        Toll taxes adhere to the "user pays" principle, where those who benefit from using the road infrastructure contribute to its upkeep. 
        This ensures that the burden of maintaining roads is distributed among road users rather than borne entirely by taxpayers.

        """
    )


if __name__ == "__main__":
    home_page()
