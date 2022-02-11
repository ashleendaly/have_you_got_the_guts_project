from urllib.request import urlopen, Request

def weather(country, location=""):
    if type(country) != str or type(location) != str:
        return "Parameter(s) entered is not a string. Please enter a string"
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
    elif len(location)!=0:
        url = "https://www.metoffice.gov.uk/weather/world/"+ country +"/list"
    else:
        url = "https://www.metoffice.gov.uk/weather/world/"+ country
    req = Request(url, headers={'User-Agent':'Mozilla/5.0'})
    print(url)
    page = urlopen(req).read().decode("utf-8")
    if len(location)!= 0:
        location_index = page.find(location)
        print(location_index)
        loc_start_index = location_index + len(location)
        print(loc_start_index)
    return "passed"

def news(country):
    if type(country) != str:
        return "Parameter entered is not a string. Please enter a string"
    country = country.title()
    print("Recent news in " + country)

    return

weather("usa", "detroit")