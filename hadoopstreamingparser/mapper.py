#!/usr/bin/python

import sys
import json
from bs4 import BeautifulSoup

def myfunction(line):
    record = json.load(line)
    soup = BeautifulSoup(record['html'])
    articles = soup.find_all('article')
    for article in articles:
        header = article.find('header', {'class':'entry-header'}).text.encode('utf-8').translate(None, '\n')
        content = article.find('div', {'class':'entry-content'}).text.encode('utf-8').translate(None, '\n')
        print chr(1).join([header,content,record['url']])

for line in sys.stdin:
    try:
        myfunction(line)
    except:
        pass
