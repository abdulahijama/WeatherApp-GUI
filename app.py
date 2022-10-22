
from tkinter import *

from tkinter import messagebox
import requests

url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

api_key = '535aebdbbdc6a208e03a6f213adba4de'



def get_weather(city):
  result = requests.get(url.format(city, api_key))
  if result: 
   json = result.json()
   #(City,Country, temp_celsius, temp_fahrenheit, icon, weather )
   city = json['name']
   country = json['sys']['country']
   temp_kelvin = json['main']['temp']
   temp_celsius = temp_kelvin - 273.15
   temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
   icon = json['weather'][0]['main']
   weather = json['weather'][0]['main']
   final = (city, country, temp_celsius, temp_fahrenheit, icon, weather)
   return final
  else:
    return None

def search():
  city = city_text.get()
  weather = get_weather(city)
  if weather:
    location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
    temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
    weather_lbl['text'] = weather[5]
  else:
    messagebox.showerror('Error', 'Cannot find city {}'.format(city))
  

root = Tk()
root.title("Weather app")
root.geometry('700x400')


city_text = StringVar()
city_entry = Entry(root, textvariable=city_text)
city_entry.pack()

search_btn = Button(root, text='Search weather!', width=15, command=search)
search_btn.pack()

location_lbl = Label(root, text='', font=('bold', 20))
location_lbl.pack()


image = Label(root, image='')
image.pack()

temp_lbl = Label(root, text='')
temp_lbl.pack()

weather_lbl = Label(root, text='')
weather_lbl.pack()

root.mainloop()
