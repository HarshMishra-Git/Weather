import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=4c076610766f4ba294b93609241401&q={city}"

r = requests.get(url)

# print(r.text)

weatherapi = json.loads(r.text)

temperature = weatherapi["current"]["temp_c"]

voice = f"the current weather of the {city} is {temperature} degree celcius"

print(voice)

speak.Speak(voice)