import random as ra
import requests
import time

API_KEY = "f29586250bdc9e2a16f46b19c26931a3"
#nombre_ciudad = input("Ingresar ciudad: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q=Temuco&APPID={API_KEY}&units=metric"

while True:
  response = requests.get(url).json()


  temperatura_actual = int(response['main']['temp'])

  print(str(temperatura_actual))

  payload = {"Temperatura-Temuco": temperatura_actual}
  r = requests.get("https://node-red-frivera.mybluemix.net/nodo-http-temps", params=payload)
  time.sleep(3)
