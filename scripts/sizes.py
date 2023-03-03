import sys
import imagesize
from tqdm import tqdm

from data_info import *

def main():
    data_location = DEFAULT_DATA_LOCATION
    args = sys.argv[1:]
    if (len(args) > 0):
        data_location = args[0]

    sizes = set()
    ratios = set()
    image_files = get_all_image_files(data_location)
    for file in tqdm(image_files):
        height, width = imagesize.get(file)
        sizes.add((height, width))
        ratios.add(height / width)

    print('Размеры изображений:', sizes)
    print('Соотношения сторон:', ratios)

if __name__ == "__main__":
    main()