import requests
from bs4 import BeautifulSoup
import re
import datetime

class Page():
    def __init__(self, url):
        self.page = requests.get(url)
        self.text = self.page.text
        self.soup = BeautifulSoup(self.text, features="html.parser")
        self.deBilt = self.soup.find('td', text='De Bilt').parent

    def get_current_temp(self):
        temperature = float(self.deBilt.findAll('td')[2].text)
        ## Now, check whether or not the found value COULD actually be valid
        if temperature < -30 or temperature > 50:
            return "INCORRECT TEMPERATURE FOUND"
        else:
            return temperature

    def get_date(self):
        date = self.soup.findAll('h2', text=re.compile('Waarnemingen .+uur'))[0].text
        date = re.findall('Waarnemingen (.+) uur', date)[0]
        date_obj = datetime.datetime.strptime(date, '%d %B %Y %H:%M')
        return date_obj

    def get_wind(self):
        wind = self.deBilt.findAll('td')[5].text
        return wind


    def refresh(self, url):
        self.page = requests.get(url)
        self.text = self.page.text
        self.soup = BeautifulSoup(self.text, features="html.parser")
        return self.get_current_temp()

def main():
    if __name__ == "__main__":
        url = 'https://www.knmi.nl/nederland-nu/weer/waarnemingen'
        page = requests.get(url)
        page = Page(url)
        print(page.get_current_temp())
        print(page.get_date())
        print(page.get_wind())

main()

#url = 'https://forecast.buienradar.nl/2.0/forecast/2746301?ak=3c4a3037-85e6-4d1e-ad6c-f3f6e4b75f2f'



