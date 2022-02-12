from urllib.request import urlopen, Request
from country_list import countries_for_language
import string
import mechanicalsoup as ms
import pycountry

upr_alpha = list(string.ascii_uppercase)

lwrcase_countries = []
for i in range(len(countries_for_language('en'))):
    lwrcase_countries += [countries_for_language('en')[i][1]]

# sets up browser to use to access the html of the website
browser = ms.Browser()

# takes country name and city and returns url for weather via weather-forecast.com
def weather(country, city):
    if type(country) != str or type(city) != str or len(country)==0 or len(city)==0 or (country not in lwrcase_countries):
        return "Invalid parameter(s) for program. Please enter valid parameters"
    country = country.title()
    string = "Weather in " + country
    city = city.title()
    string += ", "+city
    print(string)
    country = country.lower()
    url = 'https://www.weather-forecast.com/'
    if country=="uk" or country=="united kingdom":
        country = "united kingdom"
    elif country=="usa" or country=="united states" or country == "united states of america":
        country = "united states"
    country_url = country.replace(" ", "-")
    country_url = "countries/"+country_url
    url = url+country_url
    def find_link(url, city):
        city = city.lower()
        req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
        log_page = browser.get(url)
        log_html = log_page.soup
        links = log_html.select('a')
        for link in links:
            address = link['href']
            text = link.text
            text = text.strip().lower()
            if text == city:
                address = "https://www.weather-forecast.com/" + address
                return address
    address = find_link(url, city)
    if address is None:
        url = url + "/locations/" + city[0].upper()
        address = find_link(url, city)
        if address is None:
            return ""
        return address
    else:
        return address

# takes country and returns link from bbc which contains data on the recent news
def news(country):
    if type(country) != str or len(country)==0 or (country not in lwrcase_countries):
        return "Invalid parameter for program. Please enter valid parameters"
    country = country.title()
    print("Recent news in " + country)
    country = country.lower()
    home_headers = ['england', 'n. ireland', 'scotland', 'wales']
    if country in home_headers:
        url = "https://www.bbc.co.uk/news"
        req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
        log_page = browser.get(url)
        log_html = log_page.soup
        links = log_html.select('a')
        for link in links:
            address = link['href']
            text = link.text
            text = text.strip().lower()
            if text in country:
                print(text+" "+address)
    else:
        if country == 'usa':
            country = 'us '
        world_headers = ['africa', 'asia', 'australia', 'europe', 'latin america', 'middle east', 'us & canada']
        url = "https://www.bbc.co.uk/news/world"
        req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
        log_page = browser.get(url)
        log_html = log_page.soup
        links = log_html.select('a')
        for link in links:
            address = link['href']
            text = link.text
            text = text.strip().lower()
            if text in world_headers:
                if country in text:
                    address = "https://www.bbc.co.uk"+address
                    return address

#print(news('asia'))

#s = weather("afghanistan", "fayzabad")
#print(s)