import validators
import urllib2
import csv
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

def writeToCSV(data):
    with open('titler_metatitler.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file)

        for url, title, desc in data:
            csv_writer.writerow([url, title, desc])

def getTitleTags(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')

    data = []

    title = soup.title.string
    desc = soup.find_all('meta', attrs={'name':'description'})['content'].get('content') or soup.find('meta',  attrs={'property':'Description'}).get('content')

    print desc
    # data.append((url, title, desc))
    #
    # writeToCSV(data)

def getLinksFromSite(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')

    allLinks = soup.find_all('a', href=True)

    for link in allLinks:
        if validators.url(link['href']) and url in link['href']:
            getTitleTags(link['href'])
        else:
            pass

PAGE_URL = raw_input('Which url would you like to scrape? \n')

getLinksFromSite(PAGE_URL)
