#import requests
from urllib.request import urlopen

def weather(country, uk=""):
    country = country.title()
    print("Weather in " + country)
    country = country.lower()
    if len(uk)!=0:
        return "uk"
    else:
        if country=="usa" or country=="united states" or country == "united states of america":
            country = "united_states_of_america"
        url = "https://www.metoffice.gov.uk/weather/world/"+ country +"/list"
        print(url)
    return "passed"

def news(country):
    output1 = "Recent news in " + country

    return output1
weather("United States of America")
search="Weather in the New York"
URL ="https://openweathermap.org/city/5128581"