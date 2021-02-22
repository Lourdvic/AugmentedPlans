import cv2
import numpy as np  
import sys

# to upload and save files
from tkinter import filedialog
from tkinter import *
from program import Root

root = Tk()
file = Root()
imgpath = file.fileDialog()

#load image and convert to hsv
img = cv2.imread(imgpath)

#turn black into white and white into black
lower_black = np.array([0,0,0], dtype = "uint16")
upper_black = np.array([70,70,70], dtype = "uint16")
black_mask = cv2.inRange(img, lower_black, upper_black)

# findcontours
contours, hier = cv2.findContours(black_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#draw contours
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

#display result
cv2.imshow("Result", img)

x_coord = []
y_coord = []
i = 0
apfile = []
for coord in range(len(contours)):
  for coord2 in range(len(contours[coord])):
    x_coord.append(contours[coord][coord2][0][0])
    y_coord.append(contours[coord][coord2][0][1])

#write AP FILE
for i in range(len(x_coord) -1):
  x1 = x_coord[i]
  y1 = y_coord[i]
  print("x1: ", x1, " y1: ", y1)
  if i == len(x_coord) -1 and j == len(y_coord) -1:
    #if it's the last wall the next wall point is the first one
    #get the coordinate of the distance wall
    x2 = x_coord[0]
    y2 = y_coord[0]
    
    #convert the pixel coord to mm at scale
    originX = int(round(x1 / 40 * 100 * 10))
    originY = int(round(y1 / 40 * 100 * 10))
    sizeX = int(round(x2 / 40 * 100 * 10) + round(x1 / 40 * 100 * 10))
    sizeY = int(round(y2 / 40 * 100 * 10) + round(y1 / 40 * 100 * 10))
    
    #compute the distance
    if sizeX < 0:
      originX += int(sizeX)
      sizeX = int(abs(sizeX))
    if sizeY < 0:
      originY += int(sizeY)
      sizeY = int(abs(sizeY))

  else:
    #get the next point of the wall
    idx = x_coord.index(x1) + 1
    idx2 = y_coord.index(y1) + 1
    x2 = x_coord[idx]
    y2 = y_coord[idx2]

  originX = int(round(x1 / 40 * 100 * 10))
  originY = int(round(y1 / 40 * 100 * 10))

  sizeX = int(round(x2 / 40 * 100 * 10) - round(x1 / 40 * 100 * 10))
  sizeY = int(round(y2 / 40 * 100 * 10) - round(y1 / 40 * 100 * 10))
  if sizeX < 0:
    originX += int(sizeX)
    sizeX = int(abs(sizeX))
  if sizeY < 0:
    originY += int(sizeY)
    sizeY = int(abs(sizeY))

  # ID type and group id of the object 
  apfile.append('W00000001')

  # origin X
  if originX == 0:
    apfile.append('000000000')
  elif originX <= 9 and originX > 0:
    apfile.append('00000000' + str(originX))
  elif originX >= 10 and originX <= 99:
    apfile.append('0000000' + str(originX))
  elif originX >= 100 and originX <= 999:
    apfile.append('000000' + str(originX))
  elif originX >= 1000 and originX <= 9999:
    apfile.append('00000' + str(originX))
  elif originX >= 10000 and originX <= 99999:
    apfile.append('0000' + str(originX))

  # origin Y
  if originY == 0:
    apfile.append('000000000')
  elif originY <= 9 and originY > 0:
    apfile.append('00000000' + str(originY))
  elif originY >= 10 and originY <= 99:
    apfile.append('0000000' + str(originY))
  elif originY >= 100 and originY <= 999:
    apfile.append('000000' + str(originY))
  elif originY >= 1000 and originY <= 9999:
    apfile.append('00000' + str(originY))
  elif originY >= 10000 and originY <= 99999:
    apfile.append('0000' + str(originY))

  # origin z
  apfile.append('000000000')
        
  # angle X, Y, Z
  apfile.append('000000000')
  apfile.append('000000000')
  apfile.append('000000000')

  # size X
  if sizeX == 0:
    apfile.append('000000000')
  elif sizeX <= 9 and sizeX > 0:
      apfile.append('00000000' + str(sizeX))
  elif sizeX >= 10 and sizeX <= 99:
    apfile.append('0000000' + str(sizeX))
  elif sizeX >= 100 and sizeX <= 999:
    apfile.append('000000' + str(sizeX))
  elif sizeX >= 1000 and sizeX <= 9999:
    apfile.append('00000' + str(sizeX))
  elif sizeX >= 10000 and sizeX <= 99999:
    apfile.append('0000' + str(sizeX))

  # sizeY 
  if sizeY == 0:
    apfile.append('000000000')
  elif sizeY <= 9 and sizeY > 0:
    apfile.append('00000000' + str(sizeY))
  elif sizeY >= 10 and sizeY <= 99:
    apfile.append('0000000' + str(sizeY))
  elif sizeY >= 100 and sizeY <= 999:
    apfile.append('000000' + str(sizeY))
  elif sizeY >= 1000 and sizeY <= 9999:
    apfile.append('00000' + str(sizeY))
  elif sizeY >= 10000 and sizeY <= 99999:
    apfile.append('0000' + str(sizeY))
  
  # size Z
  apfile.append('000000000')

  # pipe
  apfile.append('000000000')

# convert the apfile list to a str
apstring = ''.join(apfile)


# write & save apfile on file 
win = Tk()
filename = filedialog.asksaveasfilename(initialdir='/', title='Save File', filetypes=(('AP Files', '.ap*'), ('All Files', '*.*')))
myfile = open(filename, "w+")
myfile.write(apstring)
print("File saved as ", filename)