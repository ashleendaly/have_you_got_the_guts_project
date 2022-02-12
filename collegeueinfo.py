
from tkinter import *
from urllib.request import urlopen
from country_list import countries_for_language
from newsweather import news, weather
import requests




x = requests.get(f'https://guts22.dukedan.uk/api/weather?city={city}') # 'city' contains city name, e.g. Glasgow
print(x.status_code) # will be 200 if request was successful. If code starts with 5 or 4 an error has occurred.
weather_data = x.json()
if weather_data'success'] == True:
  print(weather_data['data'])
else:
  print(weather_data['reason'])

url= ’api.openweathermap.org/data/2.5/weather?lat={l}&lon={lon}&appid={ 31b68aa2df700b29c325496f14e75f06}’






def weather(country, location):
    if type(country) != str or type(city) != str or len(country)==0 or len(city)==0:
        return "Invalid city(s) for program. Please enter a city of your collegaue
    country = country.title()
    string = "Weather in " + country
    city = city.title()
    string += ", "+city
    print(string)
    country = country.lower()
    if country=="France" or country==“France:"
        country = “France”
    elif country=="usa" or country=="united states" or country == "united states of america":
        country = "united_states_of_america"


# ---- Add Colleague
//we add extending paddy from right to left frame, which is why I am using padx
add_colleague_label = Label(left_frame, text="Add Colleague").grid(row=0, column=0, padx=5, pady=5, columnspan=2)

// name of your colleague
 - Name Label and Entry
name_label = Label(left_frame, text="Name:")
name_label.grid(row=1, column=0, padx=5, pady=5)

name_entry = Entry(left_frame)
name_entry.focus_set()
name_entry.grid(row=1, column=1, padx=5, pady=5)


 // country of your colleague 
countrylabel = Label(left_frame, text="Country:")
country_label.grid(row=1, column=0, padx=5, pady=5)

country_text = StringVar()
country_entry = Entry(left_frame, textvariable=country_text)
country_entry.grid(row=1, column=1, padx=5, pady=5)












add_colleague_button = Button(left_frame, text="Add", command=add_colleague_to_dict)
add_colleague_button.grid(row=3, column=0, padx=5, pady=5, columnspan=2)


 root.mainloop()


