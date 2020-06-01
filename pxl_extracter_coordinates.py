import cv2
from PIL import ImageColor
import PIL.Image
import numpy as np
from program import Root
 
file = Root()
path = file.fileDialog()
print("PATH = ", path)

img = PIL.Image.open(path)
size = w, h = img.size
data = img.load()

pxl_coords = []
im = PIL.Image.new('1', (1200, 1055)) # create the Image of size 1 pixel
for x in range(w):
    for y in range(h):
        hex_color = '#' + \
        ''.join([ hex(it)[2:].zfill(2).upper() for it in data[x, y] ])
        #if the pxl is black append to its coordinates and draw it on a new image
        if hex_color == '#000000':
            pxl_coords.append((x, y, hex_color))
            im.putpixel((x, y), ImageColor.getcolor('white', '1')) #draw the pixel

im.save('newplan1.png')



with open('pxl_black-coords.txt', 'w') as handle:
    for pxl_coord in pxl_coords:
        handle.write(str(pxl_coord).replace("'", '') + '\n' )
