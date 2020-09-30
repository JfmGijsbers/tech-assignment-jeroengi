from django.core.management.base import BaseCommand, CommandError

import requests
import datetime
from weather.models import Page
import json

def main():
    url = 'https://jeroengijsbers.nl/weatherboyJeroengi/get_data.php'
    page_text = requests.get(url).text
    page_json = json.loads(page_text)
    for page in page_json:
        date = datetime.datetime.strptime(page['date'], '%Y-%m-%dT%H:%M')
        if Page.objects.filter(date=date).count() > 0:
            pass
        else:
            P = Page(temperature=page['temperature'], date=date)
            P.save()
    
        
