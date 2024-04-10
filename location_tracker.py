import streamlit as st
from streamlit_folium import folium_static
import folium

def location_tracker_page():
    st.title("Location Tracker Page")
    st.write("This is the location tracker page.")

import streamlit as st
from streamlit_folium import folium_static
import folium

def location_tracker_page():
    st.title("Vehicle Location Tracker")

    # Set initial coordinates to Andheri, Mumbai, India
    andheri_lat = 19.1197
    andheri_lon = 72.8464

    # Create a folium map centered around Andheri, Mumbai, India
    vehicle_map = folium.Map(location=[andheri_lat, andheri_lon], zoom_start=12)

    # Add marker for Andheri
    folium.Marker(location=[andheri_lat, andheri_lon], popup="Andheri, Mumbai").add_to(vehicle_map)

    st.write("### Vehicle Location Input Received From GPS Module.")
    st.write("Click On Update Location To See Map")
    # Input fields for latitude and longitude
    latitude = st.number_input("Latitude", min_value=-90.0, max_value=90.0, step=0.0001, format="%.4f", help="Enter latitude")
    longitude = st.number_input("Longitude", min_value=-180.0, max_value=180.0, step=0.0001, format="%.4f", help="Enter longitude")

    # Button to update vehicle's location on the map
    if st.button("Update Location"):
        # Remove previous marker
        vehicle_map = folium.Map(location=[andheri_lat, andheri_lon], zoom_start=12)
        folium.Marker(location=[andheri_lat, andheri_lon], popup="Andheri, Mumbai").add_to(vehicle_map)

        # Add marker for updated location
        folium.Marker(location=[latitude, longitude], popup="Vehicle Location").add_to(vehicle_map)

        # Display the updated map
        folium_static(vehicle_map)

if __name__ == "__main__":
    location_tracker_page()

