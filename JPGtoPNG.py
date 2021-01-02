import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output = sys.argv[2]


if not os.path.exists(output):
    os.makedirs(output)

for filename in os.listdir(image_folder):
    print (filename)
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)  # to remove the extension
    img.save(f'{output}{clean_name}.png', 'png')
    print('ALL DONE!')
