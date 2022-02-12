from urllib.request import urlopen, Request
from country_list import countries_for_language
import mechanicalsoup as ms
import pycountry

# sets up browser to use to access the html of the website
browser = ms.Browser()

# takes country name and city and returns url for weather via weather-forecast.com
def weather(country, city):
    if type(country) != str or type(city) != str or len(country)==0 or len(city)==0:
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
    
    #finds url that contains the weather information
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
    
    #finds info about the weather given the url
    def get_info(url):
        inform = []
        inform2 = []
        print("Getting info...")
        req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
        info_page = browser.get(url)
        info_html = info_page.soup
        infos = info_html.select('span')
        for info in infos:
            text = info.text
            if len(text)!=0:
                text = text.replace("\n", '')
                if text != '-' or text != '|':
                    if '\u2009' in text:
                        text = text.replace('\u2009', '')
                    inform += [text]
        infos = info_html.select('div')
        weather_types = ['cloudy', 'some clouds', 'rain shwrs', 'light rain', 'clear', 'mod. rain']
        weth_types = []
        for info in infos:
            text = info.text
            text = text.replace("\n", '')
            if len(text)!=0 or text != '-':
                if text in weather_types:
                    weth_types += [text]
                inform2 += [text]
        index = inform.index('Temp')
        temps = inform[index+3:index+8]
        weather = weth_types[36:41]
        times=[]
        for info in inform:
            if info.endswith('AM') or info.endswith('PM'):
                if len(info)>2:
                    times += [info]
                    if len(times)==5:
                        break
        output = {}
        for i in range(len(times)):
            output[times[i]] = [temps[i]+"°C", weather[i]]
        return output
        
    
    address = find_link(url, city)
    if address is None:
        url = url + "/locations/" + city[0].upper()
        address = find_link(url, city)
        if address is None:
            return ""
        result = get_info(address)
        return result
    else:
        result = get_info(address)
        return result

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

#s = weather("uk", "london")
#print(s)