import requests
import time

def get_iss_data():
    iss_api = 'https://api.wheretheiss.at/v1/satellites/25544'
    request = requests.get(iss_api).json()
    iss_latitude = request['latitude']
    iss_longitude = request['longitude']
    iss_altitude = request['altitude']
    iss_velocity = request['velocity']

    print(f'''
---------------------------
Real-time ISS Location:
---------------------------
Altitude: {iss_altitude}
Latitude: {iss_latitude}
Longitude: {iss_longitude}
Velocity km/h: {iss_velocity}
---------------------------
    ''')

def iss_current_data():
    i = 1
    while i <= 5:
        get_iss_data()
        time.sleep(3)
        i += 1

iss_current_data()