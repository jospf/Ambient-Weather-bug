import requests
import subprocess
from config import API_KEY, APP_KEY, MAC_ADDRESS

url = f"https://api.ambientweather.net/v1/devices/{MAC_ADDRESS}?apiKey={API_KEY}&applicationKey={APP_KEY}"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, list) and len(data) > 0:
        latest = data[0]
        temp = latest.get("tempf", "N/A")
        humidity = latest.get("humidity", "N/A")
        wind = latest.get("windspeedmph", "N/A")
        rain = latest.get("dailyrainin", "N/A")

        message = f"🌡 {temp}°F | 💧 {humidity}% | 💨 {wind}mph | 🌧 {rain}in"
        subprocess.run(
            ["notify-send", "--app-name=Weather", "🌤️ Local Weather", message]
        )
    else:
        subprocess.run(["notify-send", "Weather Error", "No valid data received."])

except requests.exceptions.Timeout:
    print("Request timed out.")
except Exception as e:
    subprocess.run(["notify-send", "Weather Error", str(e)])
