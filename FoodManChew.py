import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://people.cis.ksu.edu/~hahnd11/First%20Site/').read())

page_title = soup.title.string

print(page_title)

fav_heroes = soup.body.ol.contents

for x in range(0,len(fav_heroes)):
    print(fav_heroes[x])
