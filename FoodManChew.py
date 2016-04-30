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
    temp = temp.split(">")[len(temp.split(">")) - 1]
    return temp

soup = BeautifulSoup(urllib2.urlopen('').read())
