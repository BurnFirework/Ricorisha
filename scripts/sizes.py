import os
import imagesize
from tqdm import tqdm

from data_info import *

sizes = set()
ratios = set()

for i in tqdm(range(DATA_SIZE)):
    path = f'{RELATIVE_LOCATION}/{i}.jpg'
    if os.path.isfile(path):
        height, width = imagesize.get(path)
        sizes.add((height, width))
        ratios.add(height / width)

print('Размеры изображений:', sizes)
print('Соотношения сторон:', ratios)