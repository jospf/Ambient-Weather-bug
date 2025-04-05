import requests
from config import API_KEY, APP_KEY, MAC_ADDRESS  # Import keys and MAC address from config.py

# Construct the API URL with the provided credentials
url = f'https://api.ambientweather.net/v1/devices/{MAC_ADDRESS}?apiKey={API_KEY}&applicationKey={APP_KEY}'

try:
    # Make a GET request to the API
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the HTTP response code indicates an error (4xx or 5xx)
    data = response.json()

    if isinstance(data, list) and len(data) > 0:
        latest = data[0]
        temp = latest.get('tempf', 'N/A')
        humidity = latest.get('humidity', 'N/A')
        windspeed = latest.get('windspeedmph', 'N/A')

        print(f"🌡️ {temp}°F  💧 {humidity}%  💨 {windspeed} mph")
    else:
        print("No valid data available from the API.")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from Ambient Weather API: {e}")
except KeyError as e:
    print(f"Unexpected data format: Missing key {e}")
