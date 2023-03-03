import sys
from tqdm import tqdm
import json
import matplotlib.pyplot as plt

from data_info import *

def is_clickable(root_node):
    if root_node.get('clickable', False):
        return True
    nodes = [root_node]
    children_index = [0]
    while len(nodes) > 0:
        cur_node = nodes[-1]
        children = cur_node.get('children', [])

        if children_index[-1] >= len(children):
            nodes.pop()
            children_index.pop()
            continue
        
        child_index = children_index[-1]
        child = children[child_index]
        children_index[-1] += 1
        if child is not None:
            if child.get('clickable', False):
                return True
            nodes.append(child)
            children_index.append(0)
    return False

def main():
    data_location = DEFAULT_DATA_LOCATION
    args = sys.argv[1:]
    if (len(args) > 0):
        data_location = args[0]

    unclickable_count = 0
    json_files = get_all_json_files(data_location)
    for file in tqdm(json_files):
        with file.open() as json_file:
            data = json.load(json_file)
            if not is_clickable(data['activity']['root']):
                unclickable_count += 1
    
    print('Количество неинтерактивных экранов:', unclickable_count)

if __name__ == "__main__":
    main()