import requests
from bs4 import BeautifulSoup

letters = ['AAPL', 'TWTR', 'GC=F', 'INTC']
urlStr = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s={}&region=US&lang=en-US'
headers = {'User-Agent': 'Mozilla/5.0'}

def scraper():
    for letter in letters:
        url = urlStr.format(letter)
        try:
            response = requests.get(url, headers=headers)
            if int(response.status_code)>=200 and int(response.status_code)<300:
                feeds = BeautifulSoup(response.text, features='html.parser').find_all('item')
                print("I've got {} feeds for letter: {}".format(len(feeds), letter))
                [print('feed link: ',(feed.link.next_element.strip())) for feed in feeds]
            else:
                print('Web Server error: {}'.format(response.status_code))
        except Exception as err:
            print(err.args)

scraper()

# from app.myAPI.models import rssFeeds
# rssFeeds.objects.all().delete()