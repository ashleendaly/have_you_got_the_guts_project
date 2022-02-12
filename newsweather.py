from urllib.request import urlopen, Request
from country_list import countries_for_language
import mechanicalsoup as ms

print(countries_for_language('en')[0][1])

lwrcase_countries = []
for i in range(len(countries_for_language('en'))):
    lwrcase_countries += [countries_for_language('en')[i][1]]

def weather(country, location):
    browser = ms.Browser()
    if type(country) != str or type(location) != str or len(country)==0 or len(location)==0:
        return "Invalid parameter(s) for program. Please enter a string"
    country = country.title()
    string = "Weather in " + country
    if len(location)!=0:
        location = location.title()
        string += ", "+location
    print(string)
    country = country.lower()
    if country=="uk" or country=="united kingdom":
        country = "uk"
    elif country=="usa" or country=="united states" or country == "united states of america":
        country = "united_states_of_america"
    
    if country=="uk":
        url = "https://www.metoffice.gov.uk/weather/forecast/uk"
    else:
        url = "https://www.metoffice.gov.uk/weather/world/"+ country +"/list"
        location = location.lower()
    req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    print(url)
    log_page = browser.get(url)
    log_html = log_page.soup
    links = log_html.select('a')
    for link in links:
        address = link['href']
        text = link.text
        text = text.strip().lower()
        if text == location:
            address = "https://www.metoffice.gov.uk" + address
            return address

def news(country):
    if type(country) != str or len(country)==0:
        return "Parameter entered is not a string. Please enter a string"
    country = country.title()
    print("Recent news in " + country)
    country = country.lower()
    if country=="uk" or country=="united kingdom":
        url = "https://www.bbc.co.uk/news/uk"
    elif country=="scotland" or country=="england" or country=="wales":
        url = "https://www.bbc.co.uk/news/"+country
    elif country == "northern ireland":
        url = "https://www.bbc.co.uk/news/northern_ireland"
    return

weather("usa", "detroit")