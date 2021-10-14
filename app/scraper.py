import requests
from bs4 import BeautifulSoup
from .myAPI.models import rssFeeds
from django.conf import settings
from django.db import IntegrityError

letters = settings.SCRAPER_ABC
urlStr = settings.SCRAPER_URL
headers = settings.SCRAPER_HEADERS

def insertFeed(feed, letter):
    try:
        rssFeeds(letter=letter, guid=feed.guid.text, link=feed.link.next_element.strip(),
                    pubDate=feed.pubdate.text, title=feed.title.text, description=feed.description.text).save()
            
    except IntegrityError as err:
        print('feed with guid: {} already exists; Skipping insert'.format(feed.guid.text))
    except Exception as err:
        print(repr(err))


def scraper():
    for letter in letters:
        url = urlStr.format(letter)
        try:
            response = requests.get(url, headers=headers)
            if int(response.status_code)>=200 and int(response.status_code)<300:
                feeds = BeautifulSoup(response.text, features='html.parser').find_all('item')
                print("I've got {} feeds for letter: {}".format(len(feeds), letter))
                [insertFeed(feed, letter) for feed in feeds]
            else:
                print('Web Server error: {}'.format(response.status_code))
        except Exception as err:
            print(err.args)