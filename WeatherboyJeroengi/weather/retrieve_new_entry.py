import requests
from bs4 import BeautifulSoup
import re
import datetime
from .models import Page

class WeatherEntry():
    def __init__(self, url):
        self.url = url
        self.text = requests.get(url).text
        self.soup = BeautifulSoup(self.text)
        self.deBilt = self.soup.find('td', text='De Bilt').parent

    def retrieve_temperature(self):
        try:
            return float(self.soup.find('td', text='De Bilt').parent.findAll('td')[2].text)
        except:
            return "Fatal error retrieving temperature"
    
    def retrieve_date(self):
        try:
            date = self.soup.findAll('h2', text=re.compile('Waarnemingen .+uur'))[0].text
            date = re.findall('Waarnemingen (.+) uur', date)[0]
            date_obj = datetime.datetime.strptime(date, '%d %B %Y %H:%M')
            return date_obj
        except:
            return "Fatal error retrieving date"
    
    def retrieve_wind(self):
        try:
            # Gather wind direction (4) and speed (5)
            return [self.deBilt.findAll('td')[4].text, self.deBilt.findAll('td')[5].text]
        except:
            return "Fatal error retrieving wind"



def main():
    url = 'https://www.knmi.nl/nederland-nu/weer/waarnemingen'
    weather_entry = WeatherEntry(url)
    db_entry = Page(temperature=weather_entry.retrieve_temperature(), date=weather_entry.retrieve_date())
    db_entry.save()
