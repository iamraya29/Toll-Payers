# gps_receiver.py

import time

def receive_gps_coordinates():
    while True:
        # Simulated GPS coordinates (replace with actual implementation)
        latitude = 19.1200
        longitude = 72.8464
        yield latitude, longitude
        time.sleep(5)  # Simulate a delay of 5 seconds
