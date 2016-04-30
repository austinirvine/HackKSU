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
    del arr[0]
    for x in range(0, len(arr)):
        arr[x] = remove_tags(arr[x])
    return arr

def return_prices(temp):
    temp = str(temp)
    arr = temp.split("\"menu-item-price\">")
    del arr[0]
    for x in range(0, len(arr)):
        arr[x] = remove_tags(arr[x])
    return arr

soup = BeautifulSoup(urllib2.urlopen('http://www.hunamexpress.com/#/').read())

page_title = soup.title.string

print("Web page title: " + page_title)

#appetizers
menu_section = return_menu_section("category21972")
complete_menu_items = return_menu_items(menu_section)
complete_menu_prices = return_prices(menu_section)

#soups
menu_section = return_menu_section("category21973")
complete_menu_items.extend(return_menu_items(menu_section))
complete_menu_prices.extend(return_prices(menu_section))

print("\n")

for x in range(0, len(complete_menu_items)):
    print(complete_menu_prices[x] + "\t" + complete_menu_items[x])
