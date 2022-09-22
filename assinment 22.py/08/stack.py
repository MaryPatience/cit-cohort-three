from tkinter import *
import requests
import json
from datetime import datetime

#Display GUI window

interface =Tk()
#Setting GUI window size
interface.geometry("500x400")
interface.configure(bg="brown")
interface.resizable(0,0) #to make the window size fixed
#Displaying title
interface.title("-----NISAN GROUP PROJECT WEATHERAPP-----")


# creating functions to use in generating info via the open weather api
city_value = StringVar()


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


city_value = StringVar()

def weather_info():
    #API key from the OpenWeatherMap site
    #update this with your apikey
    api_key = "b6bf1ba66c65329ada34e9d32271fa30"
    
    # Getting data(city name) from the input field
    city_name=city_value.get()

    # open weathermap API
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    # Getting data(city name) from the input field
    response = requests.get(weather_url)

    #  converting open weathermap api url_response from json to python readable 
    weather_info = response.json()

    #Emptying textfield
    tfield.delete("1.0", "end")   

    #200 represents success
    #checking if there is a response

    if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin
        
        temp = int(weather_info['main']['temp'] - kelvin)      
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        
        #creating weather variable and passing values generated from the weather api
    try:  
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nDetails: {description}"
    except:
        weather = f"\nWeather for '{city_name}' not found!\nKindly Enter valid City Name !!"


    #Displaying output from the text input
    tfield.insert(INSERT, weather)


# GUI-side
city_head= Label(interface, text = 'City Name', font = 'Arial 12 bold').pack(pady=10)

inp_city = Entry(interface, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()


Button(interface, command = weather_info, text = "get weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
# Displaying output

weather_now = Label(interface, text = "Results:", font = 'arial 12 bold').pack(pady=10)

tfield = Text(interface, width=46, height=10)
tfield.pack()

interface.mainloop()