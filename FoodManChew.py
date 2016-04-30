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

def return_menu_section(cat):
    return(soup.body.find_all(id=cat))

def return_menu_items(temp):
    temp = str(temp)
    arr = temp.split("\"menu-item-name\">")
    return arr

def return_prices(temp):
    temp = str(temp)
    arr = temp.split("\"menu-item-price\">")
    return arr

soup = BeautifulSoup(urllib2.urlopen('http://www.hunamexpress.com/#/').read())

page_title = soup.title.string

print("Web page title: " + page_title)


menu_section = return_menu_section("category21972")
#menu_section = soup.body.find_all(id="category21972")

menu_items = return_menu_items(menu_section)

menu_prices = return_prices(menu_section)

del menu_items[0]
del menu_prices[0]

for x in range(0, len(menu_items)):
    menu_items[x] = remove_tags(menu_items[x])
    menu_prices[x] = remove_tags(menu_prices[x])

print("\n")

for x in range(0, len(menu_items)):
    print(menu_prices[x] + "\t" + menu_items[x])
