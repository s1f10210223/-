import csv
import os
import sys
import requests

from bs4 import BeautifulSoup

def scraping():
    url = 'https://news.yahoo.co.jp/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = []
    for top_news in soup.find_all(class_='sc-ccXozh'):
        result.append([
            top_news.text,
            top_news.get('href')
        ])   
    return result