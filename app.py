# app.py

import streamlit as st
from streamlit_folium import folium_static
import folium
from gps_receiver import receive_gps_coordinates
from toll_booth import is_within_bounds

def main():
    st.title("Real-Time Location Tracker")

    # Create a Folium map
    m = folium.Map(location=[19.1197, 72.8464], zoom_start=12)

    # Add a marker for a toll booth location
    toll_booth_location = [19.1234, 72.8500]
    folium.Marker(location=toll_booth_location, popup="Toll Booth").add_to(m)

    # Create a marker for the vehicle's current location
    vehicle_marker = folium.Marker(location=[0, 0], popup="Vehicle Location", icon=folium.Icon(color='blue'))
    vehicle_marker.add_to(m)

    # Update the vehicle marker with real-time GPS coordinates
    for latitude, longitude in receive_gps_coordinates():
        vehicle_marker.location = [latitude, longitude]

        # Check if the vehicle is within the toll booth bounds
        if is_within_bounds(latitude, longitude):
            st.write("Vehicle entered the toll booth area!")

        # Render the updated Folium map using Streamlit
        folium_static(m)

if __name__ == "__main__":
    main()
