import requests
import tkinter as tk
from tkinter import ttk

api_key = 'd87e59989f539349fd02e6ed76cfe56e'

def get_weather(city, units):
    # Set units for API call
    if units == 'C':
        units = 'metric'
    elif units == 'F':
        units = 'imperial'
    else:
        units = 'standard'  # Default API unit if neither C nor F is chosen

    # Create the URL with the correct units
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"

    # Make the API request
    response = requests.get(url)
    data = response.json()
    # Get the temperature
    temp = data['main']['temp']
    return temp

def update_weather():
    city = city_entry.get()
    units = units_entry.get().upper()
    temperature = get_weather(city, units)
    result_label.config(text=f'Temperature in {city} is {temperature}°{units}')

root = tk.Tk()
root.title('Weather Report')

frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

city_label = ttk.Label(frame, text='Enter city: ')
city_label.grid(column=0, row=0, sticky=tk.W)
city_entry = ttk.Entry(frame, width=30)
city_entry.grid(column=0, row=1, sticky=tk.W)
city_entry.focus()

units_label = ttk.Label(frame, text='Enter C for Celsius: ')
units_label.grid(column=0, row=2, sticky=tk.W)
units_entry = ttk.Entry(frame, width=30)
units_entry.grid(column=0, row=3, sticky=tk.W)

result_button = ttk.Button(frame, text='Get Weather', command=update_weather)
result_button.grid(column=0, row=4, columnspan=2)

result_label = ttk.Label(frame)
result_label.grid(column=0, row=5, columnspan=2)

root.mainloop()