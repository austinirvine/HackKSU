import urllib2
from bs4 import BeautifulSoup

def remove_newlines(temp):
    if temp.find("u'\n'") == -1:
        return False
    else:
        return True

def remove_tags(temp):
    temp = str(temp)
    temp = temp.split("</", 2)[0]
    temp = temp.split("g>",2)[1]
    return temp

soup = BeautifulSoup(urllib2.urlopen('http://people.cis.ksu.edu/~hahnd11/First%20Site/').read())

page_title = soup.title.string

print("Web page title: " + page_title)

fav_heroes = filter(remove_newlines, soup.body.ol.contents)

for x in range(0,len(fav_heroes)):
    fav_heroes[x] = remove_tags(fav_heroes[x])

print("\nDalton's Favorite Heroes:")

for x in range(0,len(fav_heroes)):
    print(fav_heroes[x])
