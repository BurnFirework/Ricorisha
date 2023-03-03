import sys
from tqdm import tqdm
import json
import matplotlib.pyplot as plt
from collections import defaultdict
import pprint

from data_info import *

def get_depth(root_node):
    max_depth = 1
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
            nodes.append(child)
            children_index.append(0)
            max_depth = max(max_depth, len(nodes))
    return max_depth
        
def main():
    data_location = DEFAULT_DATA_LOCATION
    args = sys.argv[1:]
    if (len(args) > 0):
        data_location = args[0]
        
    depth_count = defaultdict(int)
    json_files = get_all_json_files(data_location)
    for file in tqdm(json_files):
        with file.open() as json_file:
            data = json.load(json_file)
            depth = get_depth(data['activity']['root'])
            depth_count[depth] += 1

    depth_count = dict(sorted(depth_count.items()))
    keys = list(depth_count.keys())
    values = list(depth_count.values())

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(depth_count)

    fig, ax = plt.subplots()
    plt.bar(keys, values, width=1)
    ax.set_title('Распределение глубин UI-деревьев')
    ax.set_xlabel('Глубина')
    ax.set_ylabel('Количество деревьев')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)
    fig.set_figheight(8)
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(keys, values,
            linestyle = '-',
            linewidth = 2,
            color = 'crimson')
    ax.set_title('Распределение глубин UI-деревьев')
    ax.set_xlabel('Глубина')
    ax.set_ylabel('Количество деревьев')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)
    fig.set_figheight(8)
    plt.show()

if __name__ == "__main__":
    main()