'''
Program with a function that requests the current weather in Belfast
from OpenWeatherMap.
'''
import json
from urllib import request

def getCurrentWeatherInBelfast(weatherType):
   weatherUrl = "http://api.openweathermap.org/data/2.5/weather?q=Belfast,UK&appid=3d8843f54f13271dc1eaacdb467e9cd6"
   weatherRequest = request.Request(weatherUrl)
   httpResponse = request.urlopen(weatherRequest)
   currentWeather = json.load(httpResponse)

   weatherInfo = ""

   if weatherType == "temperature":
       weatherInfo = str(currentWeather.get("main").get("temp"))
   elif weatherType == "pressure":
       weatherInfo = str(currentWeather.get("main").get("pressure"))
   elif weatherType == "description":
       weatherInfo = currentWeather.get("weather")[0].get("description")
   elif weatherType == "wind":
       weatherInfo = str(currentWeather.get("wind").get("deg")) + " degrees, " + str(currentWeather.get("wind").get("speed"))  + "mph"
   return(weatherInfo)

print(getCurrentWeatherInBelfast('temperature'))
print(getCurrentWeatherInBelfast('pressure'))
print(getCurrentWeatherInBelfast('description'))
print(getCurrentWeatherInBelfast('wind'))