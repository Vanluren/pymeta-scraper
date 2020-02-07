import validators
import urlparse
import urllib2
import csv
import sys
#from urllib.parse import urlparse
from bs4 import BeautifulSoup


PAGE_URL = raw_input("Enter the base url: ")

def getLinksFromSite(url):

    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')

    allLinks = soup.find_all('a', href=True)

    for link in allLinks:
        if validators.url(link['href']) and url in link['href']:
            print(link['href'])
        else:
            pass

getLinksFromSite(PAGE_URL)
