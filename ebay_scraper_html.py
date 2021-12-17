import json
import urllib.request
from bs4 import BeautifulSoup
from bs4.element import Script
import requests
from lxml import html
import networkx as nx
from network_setup import G
from re import sub
from decimal import Decimal

category = []
name = []
price = []
reputation = []
condition = []
image = []
root_list = {}
node_dict = {}


def create_code(condition, reputation, category, counter):
    code = category + ";" + condition + ";" + reputation + \
        ";" + str(counter)
    return code

root = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=michigan+wolverines"
ending = "&_sacat=0&_pgn="
items = [
    "hat",
    "sweatshirt",
    "mug",
    "t+shirt",
    "pin",
    "pennant"
]

for item in items:
    print("Scraping " + item + " listings")
    counter = 1
    for i in range(1, 3):
        url = root + "+" + item + ending + str(i)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        listings = soup.find_all(
            'li', class_='s-item s-item__pl-on-bottom s-item--watch-at-corner')

        for index, listing in enumerate(listings):
            # each listing is scraped and converted into a dict
            if item:
                item_category = item
            else:
                #print(str(index) + "no item category; skipped")
                continue
            if listing.find('span', class_='SECONDARY_INFO'):
                item_condition = listing.find(
                    'span', class_='SECONDARY_INFO').text
            else:
                #print(str(index) + "no condition; skipped")
                continue
            if listing.find('img', class_='s-item__image-img'):
                item_image = listing.find(
                    'img', class_='s-item__image-img')['src']
            else:
                #print(str(index) + "no image; skipped")
                continue
            if listing.find('a', class_='s-item__link'):
                item_link = listing.find('a', class_='s-item__link')['href']
            else:
                #print(str(index) + "no link; skipped")
                continue
            if listing.find('span', class_="s-item__hotness"):
                item_hotness = listing.find(
                    'span', class_="s-item__hotness").text
            else:
                item_hotness = None
            if listing.find('span', class_="s-item__etrs-text"):
                item_reputation = 'Top'
            else:
                item_reputation = "Not"
            # Above are more if/else statements that determine what data should be in the listing's dict
            # s-item__hotness
            if listing.find('h3', class_='s-item__title'):
                item_name = listing.find('h3', class_='s-item__title').text
            else:
                #print(str(index) + "no name; skipped")
                continue
            if listing.find('span', class_='s-item__price'):
                raw_price = listing.find('span', class_='s-item__price').text
                item_price = round(float(sub(r'[^\d.]', '', raw_price)), 2)
            else:
                #print(index + "no price; skipped")
                continue
            # def __init__(self, name, link, image, price, condition, reputation, category, i)
            current_code = create_code(
                item_condition, item_reputation, item_category, counter)

            root_list[current_code] = {
                "name": item_name,
                "link": item_link,
                "image": item_image,
                "price": item_price,
                "hotness": item_hotness,
                "condition": item_condition,
                "reputation": item_reputation,
                "category": item_category
            }
            G.add_node(current_code)
            G.nodes[current_code]['type'] = 'listing'

            G.add_edge(item_category, current_code)

            if (item_reputation == 'Top'):
                G.add_edge("top_rated", current_code)
            else:
                G.add_edge("not_top_rated", current_code)

            if (item_condition == 'Pre-Owned'):
                G.add_edge("pre_owned", current_code)
            else:
                G.add_edge("new", current_code)

            #G.nodes[current_code]['condition'] = item_condition
            #G.nodes[current_code]['reputation'] = item_reputation
            #G.nodes[current_code]['category'] = item_category
            counter += 1
print("Scraping complete")

# root_list_json = json.dump(root_list, 'ebay_data_object.json')
# for nbr in G.adj['hat;Brand New;Top;1']:
#    print(nbr)

temp = nx.Graph()
temp.add_nodes_from(G.adj['hat;Brand New;Top;1'])
#print(nx.get_node_attributes(temp, 'type'))


f = open("ebay_data_object.json", "w")
json.dump(root_list, f)
f.close()
# RenderTree(A).by_attr()
# How to create a walker
# w = Walker()
# w.walk(A, F)
# temp_list = course_listing_parent.find_all('h3')
# print(len(course_listing_parent))
# out_list.append(res.text)
# print("App loaded % s " % (item))
# text_file.write(res.text)
# text_file.close()
'''
listOfLists = []
listOfLists.append(category)
listOfLists.append(name)
listOfLists.append(price)
listOfLists.append(reputation)
listOfLists.append(condition)
listOfLists.append(image)
jsonListOfLists = json.dumps(listOfLists)

jsonFile = open('ebay_data_object.json', 'w')
jsonFile.write(root_list_json)
jsonFile.close()


with open('ebay_data.json', 'w') as f:
    json.dumps("[", f)
    json.dumps(category, f)
    json.dumps(name, f)
    json.dumps(price, f)
    json.dumps(reputation, f)
    json.dumps(condition, f)
    json.dumps(image, f)
    json.dumps("]", f)
'''


# userPick = input(
#    "Enter the number for the category to search: \n 1. Hats \n 2. Jackets \n 3. Sweatshirt \n 4. Mugs \nYour Pick: ")
# print("% s picked!" % (userPick))
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())

# course_urls_list[0]
# course_urls_list[0]['href']
