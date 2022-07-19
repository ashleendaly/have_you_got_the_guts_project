from email.headerregistry import Address
from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
import mechanicalsoup as ms
from countrygroups import EUROPEAN_UNION

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
    
    #finds info about the weather given the url, returns dictionary containing time, temperature and weather
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
    
    # returns url address for the respected webpage to get info from
    def get_url(url, worldH=None):
        req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
        log_page = browser.get(url)
        log_html = log_page.soup
        links = log_html.select('a')
        for link in links:
            address = link['href']
            text = link.text
            text = text.strip().lower()
            if worldH is not None:
                if text in worldH:
                    if country in text:
                        address = "https://www.bbc.co.uk"+address
                        return address
            if text in country:
                address = "https://www.bbc.co.uk"+address
                return address
    
    # returns a dictionary containing the news headline adn link to the news
    def get_news(url):
        output = {}
        links = []
        titles = []
        str_covers = []
        r1 = requests.get(url)
        coverpage = r1.content
        
        soup1 = BeautifulSoup(coverpage, 'html5lib')
        coverpage_news = soup1.find_all('a', class_='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor')
        for cover in coverpage_news:
            str_covers.append(str(cover))
            if "https://www.bbc.co.uk" in str(cover['href']) or "https://www.bbc.com" in str(cover['href']):
                links += [str(cover['href'])]
            else:
                links += [str("https://www.bbc.co.uk"+cover['href'])]
        for cover in str_covers:
            tofind = '<h3 class="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text">'
            start = cover.find('<h3 class="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text">')
            start += len(tofind)
            end = cover.find('</h3>')
            titles += [cover[start:end]]
        if len(links)==0 or len(titles)==0:
            return None
        for i in range(5):
            output[titles[i]] = links[i]
        return output
    
    if country == 'northern ireland':
        country = 'n. ireland'
    home_headers = ['england', 'n. ireland', 'scotland', 'wales']
    if country in home_headers or (country=='uk' or country=='united kingdom'):
        if country == 'n. ireland':
            country = 'northern_ireland'
        url = "https://www.bbc.co.uk/news"
        address = get_url(url)
        if country == 'northern_ireland':
            address = 'https://www.bbc.co.uk/news/northern_ireland'
        output = get_news(address)
        return output
    else:
        if country == 'usa':
            country = 'us '
        world_headers = ['africa', 'asia', 'australia', 'europe', 'latin america', 'middle east', 'us & canada']
        url = "https://www.bbc.co.uk/news/world"
        address = get_url(url, world_headers)
        if country == 'us ':
            country = 'us'
        output = get_news(address)
        return output