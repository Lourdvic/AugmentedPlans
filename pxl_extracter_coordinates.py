import cv2
from PIL import ImageColor
import PIL.Image
import numpy as np
from program import Root
from save import save
from itertools import tee, islice, chain

def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)


file = Root()
path = file.fileDialog()
print("PATH = ", path)

img = PIL.Image.open(path)
size = w, h = img.size
data = img.load()

pxl_coords = []
apfile = ['W']
listX = []
im = PIL.Image.new('1', (w, h))
for x in range(w):
    for y in range(h):
        hex_color = '#' + \
        ''.join([ hex(it)[2:].zfill(2).upper() for it in data[x, y] ])
        #if the pxl is black append to its coordinates and draw it on a new image
        if hex_color == '#000000':
            pxl_coords.append((round(x * 0.02646), round(y * 0.02646), hex_color))
            im.putpixel((x, y), ImageColor.getcolor('white', '1')) #draw the pixels
            
            listX.append(x)
            prevX = (listX[len(listX) - 2])
            #print("prevX = ", prevX, "x= ", x)
            if int(prevX) + 1 < x:
                apfile.append('W')
  
            if x < 10:
                apfile.append('00000000' + str(round(x * 0.02646)))
            elif x >= 10 and x < 100:
                apfile.append('0000000' + str(round(x * 0.02646)))
            elif x >= 100 and x < 1000:
                apfile.append('000000' + str(round(x * 0.02646)))
            elif x >= 1000:
                apfile.append('00000' + str(round(y * 0.02646)))
            if y < 10:
                apfile.append('00000000' + str(round(y * 0.02646)))
            elif y >= 10 and x < 100:
                apfile.append('0000000' + str(round(y * 0.02646)))
            elif y >= 100 and x < 1000:
                apfile.append('000000' + str(round(y * 0.02646)))
            elif y >= 1000:
                apfile.append('00000' + str(round(y * 0.02646)))
            
#print(listX)
apstring = ''.join(apfile)
#print(apstring)
im.save(save())



with open('pxl_black-coords.txt', 'w') as handle:
    for pxl_coord in pxl_coords:
        handle.write(str(pxl_coord).replace("'", '') + '\n' )

with open('apfile.ap', 'w') as handle:
    handle.write(apstring)