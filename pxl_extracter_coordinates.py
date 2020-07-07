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
listY = []
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
            listY.append(y)
            prevX = (listX[len(listX) - 2])
            prevY = (listY[len(listY) - 2])
            
            if round(int(prevX) * 0.02646) + 1 == round(x * 0.02646):
                apfile.append('W')

            if x != int(prevX) and y != int(prevY):
                if round(x * 0.02646) < 10:
                    apfile.append('0000000' + str(round(x * 0.02646)))
                elif round(x * 0.02646) >= 10 and round(x * 0.02646) < 100:
                    apfile.append('000000' + str(round(x * 0.02646)))
                elif round(x * 0.02646) >= 100 and round(x * 0.02646) < 1000:
                    apfile.append('00000' + str(round(x * 0.02646)))
                elif round(x * 0.02646) >= 1000:
                    apfile.append('0000' + str(round(y * 0.02646)))
                if round(y * 0.02646) < 10:
                    apfile.append('0000000' + str(round(y * 0.02646)))
                elif round(y * 0.02646) >= 10 and round(y * 0.02646) < 100:
                    apfile.append('000000' + str(round(y * 0.02646)))
                elif round(y * 0.02646) >= 100 and round(y * 0.02646) < 1000:
                    apfile.append('00000' + str(round(y * 0.02646)))
                elif round(y * 0.02646) >= 1000:
                    apfile.append('0000' + str(round(y * 0.02646)))
      
apstring = ''.join(apfile)
im.save(save())

with open('./coord/pxl_black-coords1.txt', 'w') as handle:
    for pxl_coord in pxl_coords:
        handle.write(str(pxl_coord).replace("'", '') + '\n' )

with open('./ap/apfile2.txt', 'w') as handle:
    handle.write(apstring)