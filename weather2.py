import requests

# Load API keys from ~/.ambient_api_keys
def load_keys(filepath):
    keys = {}
    with open(filepath, 'r') as f:
        for line in f:
            if '=' in line:
                k, v = line.strip().split('=', 1)
                keys[k.strip()] = v.strip()
    return keys

# Load keys
keys = load_keys('/home/jospf/.ambient_api_keys')  # use absolute path

API_KEY = keys.get('API_KEY')
APP_KEY = keys.get('APP_KEY')
MAC_ADDRESS = keys.get('MAC_ADDRESS')

url = f'https://api.ambientweather.net/v1/devices/{MAC_ADDRESS}?apiKey={API_KEY}&applicationKey={APP_KEY}'

response = requests.get(url)
data = response.json()

latest = data[0]  # already a dict with what we need

temp = latest.get('tempf', 'N/A')
humidity = latest.get('humidity', 'N/A')
wind = latest.get('windspeedmph', 'N/A')
feels_like = latest.get('feelsLike', 'N/A')
rain_today = latest.get('dailyrainin', 'N/A')

print(f"🌡️  Temp: {temp}°F (Feels like {feels_like}°F)")
print(f"💧 Humidity: {humidity}%")
print(f"💨 Wind: {wind} mph")
print(f"🌧️  Rain Today: {rain_today} in")