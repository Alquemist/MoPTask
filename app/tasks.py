from app.celeryApp import app
from celery import shared_task
from time import sleep
from .scraper import scraper

@app.task(name='test')
def debug_task():
    sleep(2)
    print('working!')
    #print(f'Request: {self.request!r}')
    return 'Excellent'

@app.task(name='scraper')
def startScraper():
    scraper()