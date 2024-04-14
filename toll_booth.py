# toll_booth.py

toll_booth_bounds = {
    'min_latitude': 19.123,
    'max_latitude': 19.124,
    'min_longitude': 72.849,
    'max_longitude': 72.851
}

def is_within_bounds(latitude, longitude):
    if (toll_booth_bounds['min_latitude'] <= latitude <= toll_booth_bounds['max_latitude']) and \
       (toll_booth_bounds['min_longitude'] <= longitude <= toll_booth_bounds['max_longitude']):
        return True
    else:
        return False
