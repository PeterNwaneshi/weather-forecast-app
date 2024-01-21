# ---------- model.py -------------------
# Basic imports
import requests
import datetime

# Imports Within the App
from api_key import API_KEY # OpenWeatherMap API key

# Creating function to get relevant data
def get_weather_data(city):
    """Used to extract weather data from two openweathermap APIs
    
    Keyword arguments:
    Users are required to provide city name to enable extraction of weather information for the city location

    Return: 
    This function returns a dictionary of weather data
    """
    
    BASE_URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}&units=metric" # API String

    response = requests.get(BASE_URL) # connect to API
    
    
    ## if the response goes through with success extract weather information
    if response.status_code == 200: 
        response = requests.get(BASE_URL).json() # chosen json data type
        wind_speed = f"{response['wind']['speed']:.2f}m/s"
        wind_deg = f"{response['wind']['deg']:.2f}°"
        
        try:
            wind_gust = f"{response['wind']['gust']:.2f}m/s"
        except:
            wind_gust = "None"
        humidity = f"{response['main']['humidity']:.2f}%"
        search_area = f"{response['name']}, {response['sys']['country']}"
        description = response['weather'][0]['description']
        weather_icon = response['weather'][0]['icon']
        search_city = response['name']

        ### getting Latitude (lat) and Longitude (lon)
        lat = response['coord']['lat']
        lon = response['coord']['lon']

        ### Getting hourly forecast data through weathermap API
        HOURLY_URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&cnt=24&units=metric"
        response_hourly = requests.get(HOURLY_URL).json()


        ### First Forecast Data
        wind_speed_0 = f"{response_hourly['list'][0]['wind']['speed']:.2f}m/s"
        wind_deg_0 = f"{response_hourly['list'][0]['wind']['deg']:.2f}°"
        try:
            wind_gust_0 = f"{response_hourly['list'][0]['wind']['gust']:.2f}m/s"
        except:
            wind_gust_0 = "None"
        
        description_0 = response_hourly["list"][0]['weather'][0]['description']
        icon_0 = response_hourly["list"][0]['weather'][0]['icon']

        date_0 = datetime.datetime.strptime(response_hourly["list"][0]['dt_txt'],"%Y-%m-%d %H:%M:%S")
        now_0 = datetime.datetime.now().date()
        time_0 = date_0.strftime("%I:%M %p")
        time_t0 = date_0.strftime("%Y-%m-%d")
        next_t = now_0 + datetime.timedelta(days=1)
        
        if str(time_t0) == str(now_0):
            time_desc_0 = "Today"
        elif str(time_t0) == str(next_t):
            time_desc_0 = "Tomorrow"
        else:
            time_desc_0 = "Next"
        

        ### Second Forecast Data
        wind_speed_8 = f"{response_hourly['list'][8]['wind']['speed']:.2f}m/s"
        wind_deg_8 = f"{response_hourly['list'][8]['wind']['deg']:.2f}°"
        try:
            wind_gust_8 = f"{response_hourly['list'][8]['wind']['gust']:.2f}m/s"
        except:
            wind_gust_8 = "None"
        
        description_8 = response_hourly["list"][8]['weather'][0]['description']
        icon_8 = response_hourly["list"][8]['weather'][0]['icon']

        date_8 = datetime.datetime.strptime(response_hourly["list"][8]['dt_txt'],"%Y-%m-%d %H:%M:%S")
        now_8 = datetime.datetime.now().date()
        time_8 = date_8.strftime("%I:%M %p")
        time_t8 = date_8.strftime("%Y-%m-%d")
        
        if str(time_t8) == str(now_8):
            time_desc_8 = "Today"
        elif str(time_t8) == str(next_t):
            time_desc_8 = "Tomorrow"
        else:
            time_desc_8 = "Next"
        

        ### Third Forecast Data
        wind_speed_16 = f"{response_hourly['list'][16]['wind']['speed']:.2f}m/s"
        wind_deg_16 = f"{response_hourly['list'][16]['wind']['deg']:.2f}°"
        try:
            wind_gust_16 = f"{response_hourly['list'][16]['wind']['gust']:.2f}m/s"
        except:
            wind_gust_16 = "None"
        
        description_16 = response_hourly["list"][16]['weather'][0]['description']
        icon_16 = response_hourly["list"][16]['weather'][0]['icon']

        date_16 = datetime.datetime.strptime(response_hourly["list"][16]['dt_txt'],"%Y-%m-%d %H:%M:%S")
        now_16 = datetime.datetime.now().date()
        time_16 = date_16.strftime("%I:%M %p")
        time_t16 = date_16.strftime("%Y-%m-%d")

        if str(time_t16) == str(now_16):
            time_desc_16 = "Today"
        elif str(time_t16) == str(next_t):
            time_desc_16 = "Tomorrow"
        else:
            time_desc_16 = "Next"
        

        ### Storing all the data in a dictionary
        items = {
                 "speed":wind_speed,
                 "deg":wind_deg,
                 "gust":wind_gust,
                 "humidity":humidity,
                 "area":search_area,
                 "city":search_city,
                 "description":description,
                 "icon":weather_icon,
                 "forecasts":[{
                     "speed":wind_speed_0, 
                     "deg":wind_deg_0, 
                     "gust":wind_gust_0, 
                     "time":time_0, 
                     "description":description_0, 
                     "icon":icon_0, 
                     "day":time_desc_0
                 },
                 {
                     "speed":wind_speed_8, 
                     "deg":wind_deg_8, 
                     "gust":wind_gust_8, 
                     "time":time_8, 
                     "description":description_8, 
                     "icon":icon_8, 
                     "day":time_desc_8
                 },
                 {
                     "speed":wind_speed_16, 
                     "deg":wind_deg_16, 
                     "gust":wind_gust_16, 
                     "time":time_16, 
                     "description":description_16, 
                     "icon":icon_16, 
                     "day":time_desc_16
                 }],
                 
                }
        
        return items
    else:
        items = {
                 "speed":None,
                 "deg":None,
                 "gust":None,
                 "humidity":None,
                 "area":"City not available",
                 "city":"City not available",
                 "description":None,
                 "icon":None,
                 "forecasts":[{
                     "speed":None, 
                     "deg":None, 
                     "gust":None, 
                     "time":None, 
                     "description":None, 
                     "icon":None, 
                     "day":None
                 },
                 {
                     "speed":None, 
                     "deg":None, 
                     "gust":None, 
                     "time":None, 
                     "description":None, 
                     "icon":None, 
                     "day":None
                 },
                 {
                     "speed":None, 
                     "deg":None, 
                     "gust":None, 
                     "time":None, 
                     "description":None, 
                     "icon":None, 
                     "day":None
                 }],
                 
                }
        return items