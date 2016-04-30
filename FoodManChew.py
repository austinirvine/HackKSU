import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://people.cis.ksu.edu/~hahnd11/First%20Site/').read())

page_title = soup.title.string

print(page_title)

paragraph = soup.p

print(paragraph)
