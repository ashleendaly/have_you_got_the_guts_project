from urllib.request import urlopen, Request
from country_list import countries_for_language
import mechanicalsoup as ms

lwrcase_countries = []
for i in range(len(countries_for_language('en'))):
    lwrcase_countries += [countries_for_language('en')[i][1]]

browser = ms.Browser()

def weather(country, location):
    if type(country) != str or type(location) != str or len(country)==0 or len(location)==0:
        return "Invalid parameter(s) for program. Please enter valid parameters"
    country = country.title()
    string = "Weather in " + country
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
                    address = "https://www.bbc.co.uk/"+address
                    return address

#print(news('australia'))

#s = weather("usa", "detroit")
#print(s)