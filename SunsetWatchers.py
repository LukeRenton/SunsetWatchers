import requests
import pywhatkit
import datetime

API_KEY = "49e7578d1823d8de2fb067c8934bfadb"
lat = -26.205
long = 28.049722
API_ENDPOINT_WEATHER = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={API_KEY}&units=metric"
GROUP_ID = "Fi6VgN9hqOa78ttiVVyrPq"

def get_weather_results():
    weather_data = requests.get(API_ENDPOINT_WEATHER)
    weather_data = weather_data.json()
    return format_forecast(weather_data)

def format_forecast(forecast):
    time = datetime.datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d %I:%M %p')
    temp = forecast['main']['temp']
    feels_like = forecast['main']['feels_like']
    temp_min = forecast['main']['temp_min']
    temp_max = forecast['main']['temp_max']
    pressure = forecast['main']['pressure']
    humidity = forecast['main']['humidity']
    description = forecast['weather'][0]['description']
    wind_speed = forecast['wind']['speed']
    sunrise = forecast['sys']['sunrise']
    sunset = forecast['sys']['sunset']
    sunrise_time = datetime.datetime.fromtimestamp(sunrise).strftime('%I:%M %p')
    sunset_time = datetime.datetime.fromtimestamp(sunset).strftime('%I:%M %p')
    
    return f"Time: {time}\nTemperature: {temp}°C\nFeels Like: {feels_like}°C\nMin Temperature: {temp_min}°C\nMax Temperature: {temp_max}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {description}\nWind Speed: {wind_speed} m/s\nSunrise: {sunrise_time}\nSunset: {sunset_time}"


def send_whatsapp_message(message):
    pywhatkit.sendwhatmsg_instantly(f"+27607289497", message)
    
    

def lambda_handler(event, context):
    print(temp := get_weather_results())
    send_whatsapp_message(temp)

lambda_handler(None, None)