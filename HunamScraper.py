import urllib2
from bs4 import BeautifulSoup
import random

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

def prices_to_float(prices):
    fprices = [float(prices[0].split("$")[1])]
    for x in range(1, len(prices)):
        fprices = fprices + [float(prices[x].split("$")[1])]
    return(fprices)

def sort_menu_costs(items, prices):
    done = False
    while(done == False):
        done = True
        for x in range(1, len(prices)):
            if prices[x - 1] > prices[x]:
                done = False
                temp = prices[x]
                prices[x] = prices[x-1]
                prices[x-1] = temp
                temp = items[x]
                items[x] = items[x-1]
                items[x-1] = temp
    return items

def choose_foods(cash, prices, items):
    random.seed()
    selections = []
    while cash > prices[0]:
        for x in range(0, len(prices)):
            if prices[x] > cash:
                temp1 = x - 1
                break
            elif x == len(prices) - 1:
                temp1 = x

        temp2 = random.randint(0, temp1)
        cash -= prices[temp2]
        selections.append(str(items[temp2]))

    return selections

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

#chef's specialties
menu_section = return_menu_section("category21963")
complete_menu_items.extend(return_menu_items(menu_section))
complete_menu_prices.extend(return_prices(menu_section))

del complete_menu_prices[len(complete_menu_prices) - 1]
del complete_menu_items[len(complete_menu_items) - 1]

#diet dishes
menu_section = return_menu_section("category21971")
complete_menu_items.extend(return_menu_items(menu_section))
complete_menu_prices.extend(return_prices(menu_section))

spending_cash = float(input("Input cash to spend: $"))

complete_menu_items = sort_menu_costs(complete_menu_items, complete_menu_prices)
complete_menu_prices.sort()

new_complete_menu_prices = prices_to_float(complete_menu_prices)

print("\n")

for x in range(0, len(complete_menu_items)):
    print(str(new_complete_menu_prices[x]) + "\t" + complete_menu_items[x])

print("\n")

for x in choose_foods(spending_cash, new_complete_menu_prices, complete_menu_items):
    print(x)

print("\n")
