import os
from tqdm import tqdm
import json
import matplotlib.pyplot as plt

from data_info import *

def get_depth(cur_node):
    if cur_node is None:
        return 0
    max_size = 0
    children = cur_node.get('children', [])
    for i in range(len(children)):
        max_size = max(max_size, get_depth(children[i]))
    return max_size + 1
        
depth_count = dict()
for i in tqdm(range(DATA_SIZE)):
    path = f'{RELATIVE_LOCATION}/{i}.json'
    if os.path.isfile(path):
        with open(path) as json_file:
            data = json.load(json_file)
            depth = get_depth(data['activity']['root'])
            if depth in depth_count:
                depth_count[depth] += 1
            else:
                depth_count[depth] = 1

depth_count = dict(sorted(depth_count.items()))
keys = list(depth_count.keys())
values = list(depth_count.values())

print(depth_count)
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