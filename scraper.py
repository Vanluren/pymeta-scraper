import validators
import urllib2
import csv
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def writeToCSV(data):
    with open('titler_metatitler.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file)

        for url, title in data:
            csv_writer.writerow([url, title])

def getTitleTags(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    data = []

    title = soup.title.string

    data.append((url, title))
    writeToCSV(data)

def getLinksFromSite(url):
    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')

    mailto = 'mailto'

    for link in soup.find_all('a', href=True):
        if validators.url(link['href']) and url in link['href']:
            getTitleTags(link['href'])
        else:
            pass

PAGE_URL = input('Which url would you like to scrape? \n')

getLinksFromSite(PAGE_URL)
