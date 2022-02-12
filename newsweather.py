from urllib.request import urlopen, Request
from country_list import countries_for_language
import string
import mechanicalsoup as ms

upr_alpha = list(string.ascii_uppercase)

lwrcase_countries = []
for i in range(len(countries_for_language('en'))):
    lwrcase_countries += [countries_for_language('en')[i][1]]

browser = ms.Browser()

# takes country name and exact location and returns links for weather via metoffice
def weather(country, location):
    if type(country) != str or type(location) != str or len(country)==0 or len(location)==0:
        return "Invalid parameter(s) for program. Please enter valid parameters"
    country = country.title()
    string = "Weather in " + country
    location = location.title()
    string += ", "+location
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
    def find_link(url, location):
        location = location.lower()
        req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
        log_page = browser.get(url)
        log_html = log_page.soup
        links = log_html.select('a')
        for link in links:
            address = link['href']
            text = link.text
            text = text.strip().lower()
            if text == location:
                address = "https://www.weather-forecast.com/" + address
                return address
    address = find_link(url, location)
    if address is None:
        url = url + "/locations/" + location[0].upper()
        address = find_link(url, location)
        return address
    else:
        return address

# takes country and returns link from bbc which contains data on the recent news
def news(country):
    if type(country) != str or len(country)==0:
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

s = weather("uk", "wrexham")
print(s)