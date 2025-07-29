import requests

def get_weather(city):
    API_KEY = "e258412ed10f089fb116b2a5ee3913b8" 
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Get temperature in Celsius
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        data = response.json()
        
        # Extract relevant information
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}F")
        print(f"Conditions: {description.capitalize()}")
        print(f"Wind Speed: {wind_speed} km\hr")
        
    except requests.exceptions.HTTPError:
        print(f"Error: City '{city}' not found. Please check the spelling.")
    except requests.exceptions.ConnectionError:
        print("Error: Network connection failed.")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)