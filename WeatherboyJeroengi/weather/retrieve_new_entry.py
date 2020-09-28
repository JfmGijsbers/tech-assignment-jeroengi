import requests
from bs4 import BeautifulSoup
import re
import datetime
from .models import Page

def main():
    P = Page()
    url = 'https://www.knmi.nl/nederland-nu/weer/waarnemingen'
    page = requests.get(url)

    soup = BeautifulSoup(page.text)

    # We want to take the temperature in "De Bilt", since this is the standard for weather measurements in the Netherlands
    temperature = float(soup.find('td', text='De Bilt').parent.findAll('td')[2].text)
    
    date = soup.findAll('h2', text=re.compile('Waarnemingen .+uur'))[0].text
    date = re.findall('Waarnemingen (.+) uur', date)[0]
    print(date)
    date_obj = datetime.datetime.strptime(date, '%d %B %Y %H:%M')

    P.date = date_obj
    P.temperature = temperature
    P.save()
