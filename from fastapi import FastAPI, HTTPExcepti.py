import requests
from datetime import datetime

def get_weather(city):
    API_KEY = "e258412ed10f089fb116b2a5ee3913b8"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

        # Extract weather info
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        country = data['sys']['country']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')

        # Country flag emoji 🌍
        flag = chr(127397 + ord(country[0])) + chr(127397 + ord(country[1]))

        print(f"\n📍 Weather in {city.title()} {flag} ({country}):")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"🌤️ Conditions: {description.capitalize()}")
        print(f"💨 Wind Speed: {wind_speed} m/s")
        print(f"🌅 Sunrise: {sunrise}")
        print(f"🌇 Sunset: {sunset}")

    except requests.exceptions.HTTPError:
        print(f"❌ Error: City '{city}' not found.")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Network connection failed.")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    print("🌦️ Welcome to Riyad's Weather App!")
    print("👉 Type the city name to get weather info. Type 'exit' to quit.\n")

    while True:
        city = input("🌍 Enter city name: ").strip()
        if city.lower() == 'exit':
            print("👋 Bye! Stay sunny ☀️")
            break
        elif city == '':
            print("⚠️ Please enter a valid city name.")
        else:
            get_weather(city)
