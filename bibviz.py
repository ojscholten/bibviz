'''
Ollie's basic bib file visualizer.

What it does: makes a picture (bar chart-esque) where the top bar is the year of the most recent citation, and the bottom is the earliest

How to use it: put this file in the same directory as a bib file called 'test.bib' call 'python this_script.py'
'''
from pybtex.database import parse_file
from PIL import Image, ImageFont, ImageDraw 
import matplotlib.pyplot as plt
import sys

tile_size = 40 # size of squares in output image (in pixels)
tile_sep = 5 # separation between squares (in pixels)
font = ImageFont.truetype("saxmono.ttf", 38)

bib_data = parse_file(str(sys.argv[1]))

years = []
for entry in bib_data.entries:
    year = bib_data.entries[entry].fields['year']
    years.append(year)
    
year_set = set(years)
year_set = sorted(year_set, reverse=True)

max_occurances = 0
for year in year_set:
    occurances = years.count(year)
    if occurances > max_occurances:
        max_occurances = occurances

im_w = max_occurances*tile_size + max_occurances*tile_sep
im_h = (len(year_set)-1)*tile_size + (len(year_set))*tile_sep
im = Image.new("RGB", (im_w + 100, im_h), '#fff')
draw = ImageDraw.Draw(im)

cy = 1
for year in year_set:
    occurances = years.count(year)
    cx = 0
    draw.text((tile_sep, tile_sep + cy*tile_size + (cy*tile_sep) - tile_size), year, font=font, fill=(0,0,0,255))
    for x in range(occurances):
        coords = ((100+cx*tile_size + tile_sep*cx, cy*tile_sep + cy*tile_size),
                  (100+cx*tile_size+tile_size + tile_sep*cx, cy*tile_sep + cy*tile_size-tile_size))
        cx += 1
        draw.rectangle(coords, fill='blue')
    cy += 1

plt.figure()
plt.axis('off')
im.save('output.png', scale=1)

