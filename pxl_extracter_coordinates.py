import cv2
from PIL import Image
import numpy as np



img = Image.open('plan.png')

size = w, h = img.size
data = img.load()

pxl_coords = []
for x in range(w):
    for y in range(h):
        hex_color = '#' + \
        ''.join([ hex(it)[2:].zfill(2).upper() for it in data[x, y] ])
        #print(hex_color) print the pixel color in hexa
        #if the pxl is black append to its coordinates
        if hex_color == '#000000':
            pxl_coords.append((x, y, hex_color))
#print(pxl_coords)

with open('pxl_black-coords.txt', 'w') as handle:
    for pxl_coord in pxl_coords:
        handle.write(str(pxl_coord).replace("'", '') + '\n' )



#redraw the image

max_x = max_y = 0
pxl = []
with open('pxl_coords.txt') as handle:
    for line in handle.readlines():
       x, y, hex_color = line.strip().split()
       x = int(x[1:-1])
       y = int(y[:-1])

       r = int(hex_color[1:3], 16)
       g = int(hex_color[3:5], 16)
       b = int(hex_color[5:7], 16)

       #print(r, g, b)

       pxl_coords.append([x, y, r, g, b])
       #print(pxl_coords)
       #pxl.append([r, g, b])
       #print(pxl_coords)
       #array = np.array(pxl, dtype=np.uint8)
       #new_image = Image.fromarray(array)
       #new_image.save('new.png')
       max_x = max([x, max_x])
       max_y = max([y, max_y])

wid = max_x + 1
hei = max_y + 1
size = wid, hei

img = Image.new('RGB', size)

data2 = img.load()
#for pxl_coord in pxl_coords:
    #print(pxl_coord[2])
    #x, y, r, g, b = pxl_coord
    #data2[x, y] = pxl_coord[2]
    #print(x, y, r, g, b)

#data2 = np.zeros([600,600,3],dtype=np.uint8)
#data2.fill(200) # or img[:] = 255
#data2[x, y] = [r, g , b]
#img2 = Image.fromarray(data2, 'RGB')
#img2.show()

#img.show()
#img.save('recreated.jpg')

