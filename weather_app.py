import requests
from colorama import Fore, Style

API_KEY = "6747167c49c7aa2006c04722512dfec2"

try:
    Choose = int(input(Fore.CYAN + "Enter number of cities: "))
except ValueError:
    print(Fore.RED + "Please enter a valid number!")
    exit()

print(Style.RESET_ALL)

for i in range(Choose):
    city = input(Fore.GREEN + "Enter city name: ")
    print(Style.RESET_ALL)

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print(Fore.RED + "Network Error!")
        continue

    if response.status_code == 200:
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"]
            feels_like = data["main"]["feels_like"]
            wind_speed = data["wind"]["speed"]
            country = data["sys"]["country"]

            print(Fore.BLUE + f"\n🌤️ Weather in {city}, {country}:")
            print(Style.RESET_ALL)

            print(Fore.GREEN + f"🌡️ Temperature: {temp}°C")
            print(Fore.YELLOW + f"🤒 Feels like: {feels_like}°C")
            print(Fore.LIGHTBLUE_EX + f"💧 Humidity: {humidity}%")
            print(Fore.CYAN + f"🌬️ Wind Speed: {wind_speed} m/s")
            print(Fore.LIGHTYELLOW_EX + f"☁️ Condition: {weather}")
            print(Style.RESET_ALL)

        else:
            print(Fore.RED + "City Not Found")
            print(Style.RESET_ALL)

    else:
        print(Fore.RED + "Network Error")
        print(Style.RESET_ALL)