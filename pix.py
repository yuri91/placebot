from PIL import Image
import sys
import json
import sys

import argparse

parser = argparse.ArgumentParser(description='Bot for r/place.')
parser.add_argument('image',
                    help='png image to convert')
parser.add_argument('--location', required=True, type=int, nargs=2,
                    help='top left corner position of your image in the canvas')
parser.add_argument('-o',
                    help='output file')

args = parser.parse_args()
if args.o:
    out = open(args.o, 'w')
else:
    out = sys.stdout

img = Image.open(sys.argv[1])
pixels = img.load()
color_map = {
    (255, 255, 255, 255): 0,
    (228, 228, 228, 255): 1,
    (136, 136, 136, 255): 2,
    (34, 34, 34, 255): 3,
    (255, 167, 209, 255): 4,
    (229, 0, 0, 255): 5,
    (229, 149, 0, 255): 6,
    (160, 106, 66, 255): 7,
    (229, 217, 0, 255): 8,
    (148, 224, 68, 255): 9,
    (2, 190, 1, 255): 10,
    (0, 211, 221, 255): 11,
    (0, 131, 199, 255): 12,
    (0, 0, 234, 255): 13,
    (207, 110, 228, 255): 14,
    (130, 0, 128, 255): 15,
    (0, 0, 0, 0): -1,
}

arr = []
for y in range(0,img.size[1]):
    for x in range(0,img.size[0]):
        arr.append(color_map.get(pixels[(x,y)],-1))

data = {'pixels':arr,'size':img.size, 'location': args.location}
json.dump(data,out)

