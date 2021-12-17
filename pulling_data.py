import networkx as nx
from networkx.classes.function import common_neighbors
from ebay_scraper_html import G
import json

def find_multiple_common_neighbors(category, condition, reputation):
    first_pair = list(nx.common_neighbors(G, category, condition))
    second_pair = list(nx.common_neighbors(G, category, reputation))
    common_set = set(first_pair).intersection(second_pair)
    return common_set

def convert_node_to_list_raw_data(raw_data, list):
    return_list = []
    for item in list:
        return_list.append(raw_data[item])
    return return_list


#a = list(nx.common_neighbors(G, 'pin', 'pre_owned'))
#b = list(nx.common_neighbors(G, 'pin', 'top_rated'))

def import_ebay_data():
    f = open('ebay_data_object.json')
    exported_dict = json.load(f)
    f.close()

    return exported_dict
#list = find_multiple_common_neighbors('hat', 'pre_owned', 'top_rated')
#print(list)
#exported_dict = import_ebay_data()
#print(len(exported_dict))
#print(convert_node_to_list_raw_data(exported_dict,list))