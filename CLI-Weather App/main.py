# Imports
import requests
from colorama import Fore, Style


# API Key
api_key = 'cd8fe19c915f562bbede37b1ed3469e1'

city = input(Fore.CYAN + 'Enter city name: ')

# API docs - https://openweathermap.org/current
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

# Conditions
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    desc = data['weather'][0]['main']
    hum = data['main']['humidity']

    # Divider
    print(Fore.BLACK, '============================')
    
    print(Fore.GREEN + Style.BRIGHT + f"City: {data['name']}")
    print(f'Description: {desc}')
    print(f'Temperature: {round(temp - 273.15, 2)}°C / {temp}°K')
    print(f'Feels like: {round(feels_like - 273.15, 2)}°C / {feels_like}°K')
    print(f'Humidity: {hum}%')

    
elif response.status_code == 404:
    # Divider
    print(Fore.BLACK, '============================')

    print(Fore.RED + Style.BRIGHT + 'Error! City not found.')

else:
    data = response.json()
    # Divider
    print(Fore.BLACK, '============================')
    
    print(Fore.RED + Style.BRIGHT + f"Error!\n{data['message']}")