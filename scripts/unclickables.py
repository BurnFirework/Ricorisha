import os
from tqdm import tqdm
import json
import matplotlib.pyplot as plt

from data_info import *

def is_clickable(cur_node):
    if cur_node is None:
        return False
    if cur_node.get('clickable', False):
        return True
    flag = False
    children = cur_node.get('children', [])
    for i in range(len(children)):
        flag = flag or is_clickable(children[i])
    return flag
        
unclickable_count = 0
for i in tqdm(range(DATA_SIZE)):
    path = f'{RELATIVE_LOCATION}/{i}.json'
    if os.path.isfile(path):
        with open(path) as json_file:
            data = json.load(json_file)
            if not is_clickable(data['activity']['root']):
                unclickable_count += 1

print('Количество неинтерактивных экранов:', unclickable_count)