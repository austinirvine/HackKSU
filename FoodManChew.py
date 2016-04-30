import urllib2
from bs4 import BeautifulSoup

def remove_newlines(temp):
        if temp.find("u'\n'") == -1:
            return False
        else:
            return True

soup = BeautifulSoup(urllib2.urlopen('http://people.cis.ksu.edu/~hahnd11/First%20Site/').read())

page_title = soup.title.string

print(page_title)

fav_heroes = filter(remove_newlines, soup.body.ol.contents)

for x in range(0,len(fav_heroes)):
    print(fav_heroes[x])
