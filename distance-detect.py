# import required libs 

# to get the mouse event coord from an image
from tkinter import *
from PIL import ImageTk, Image

# to compute the scale
import math

# to draw the lines
import cv2

# to upload files
from program import Root

root = Tk()

file = Root()
path = file.fileDialog()
print("PATH = ", path)

imgpath = path
img = ImageTk.PhotoImage(Image.open(imgpath))

# load the clone image to draw on it
dimg = cv2.imread(path)
window_name = "plan image"

panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

# initiate the values
counter = 0
x0 = 0
x1 = 0
y0 = 0
y1 = 0

# function to compute distance between mouse event
def getDistance(event):
    global counter, x0, y0, x1, y1
    getDistance.apfile = []
    getDistance.nbwalls = 0

    # when we click the counter is incremented to recognize the different phase
    # 1st click -> get the x0 & y0 coord
    if counter == 0:
        x0 = event.x
        y0 = event.y
        print('x0 : ', x0, ' y0: ', y0)
        counter += 1
    # 2nd click get the x1 and y1 coord
    elif counter == 1:
        x1 = event.x
        y1 = event.y
        print('x1 : ', x1, ' y1: ', y1)

        counter += 1
    # 3rd click draw the line on the clone image and compute the distance then give the size of the wall
    elif counter == 2:

        #get info to draw on image 
        start_point = (x0, y0)
        end_point = (x1, y1)
        color = (0, 255, 0)
        thickness = 9
        cv2.line(dimg, start_point, end_point, color, thickness=9)
        cv2.imshow(window_name, dimg)  

        #calculate the distance
        distance = math.sqrt(((x0 - x1)**2)+((y0 - y1)**2))
        cm = distance / 40
        echelle = 100
        reeldim = cm * echelle
        mm = round(reeldim * 10)
        print(mm)

        #write AP FILE
        # ID type and group id of the object 
        getDistance.apfile.append('W00000001')
        # origin X
        if x0 == 0:
            getDistance.apfile.append('000000000')
        elif x0 <= 9 and x0 > 0:
            getDistance.apfile.append('00000000' + str(x0))
        elif x0 >= 10 and x0 <= 99:
            getDistance.apfile.append('0000050' + str(x0))
        elif x0 >= 100 and x0 <= 999:
            getDistance.apfile.append('000005' + str(x0))
        elif x0 >= 1000 and x0 <= 9999:
            getDistance.apfile.append('00000' + str(x0))
        elif x0 >= 10000 and x0 <= 99999:
            getDistance.apfile.append('0000' + str(x0)) 

        # origin y
        if y0 == 0:
            getDistance.apfile.append('000000000')
        elif y0 < 10 and y0 >  0:
            getDistance.apfile.append('00000000' + str(y0))
        elif y0 > 10 and y0 < 100:
            getDistance.apfile.append('0000050' + str(y0))
        elif y0 > 100 and y0 < 1000:
            getDistance.apfile.append('000005' + str(y0))
        elif y0 > 1000 and y0 < 10000:
            getDistance.apfile.append('00000' + str(y0))
        elif y0 > 10000 and y0 < 100000:
            getDistance.apfile.append('0000' + str(y0))
        
        # origin z
        getDistance.apfile.append('000000000')
        
        # angle X, Y, Z
        getDistance.apfile.append('000000000')
        getDistance.apfile.append('000000000')
        getDistance.apfile.append('000000000')

        # size X
        getDistance.apfile.append('000001000')
        # if mm == 0:
        #     getDistance.apfile.append('000000000')
        # elif mm < 10 and mm > 0:
        #     getDistance.apfile.append('00000000' + str(mm))
        # elif mm > 10 and mm < 100:
        #     getDistance.apfile.append('0000000' + str(mm))
        # elif mm > 100 and mm < 1000:
        #     getDistance.apfile.append('000000' + str(mm))
        # elif mm > 1000 and mm < 10000:
        #     getDistance.apfile.append('00000' + str(mm))
        # elif mm > 10000 and mm < 100000:
        #     getDistance.apfile.append('0000' + str(mm))
        
        # size Y
        getDistance.apfile.append('000002000')
        # if mm == 0:
        #     getDistance.apfile.append('000000000')
        # elif mm < 10 and mm > 0:
        #     getDistance.apfile.append('00000000' + str(mm))
        # elif mm > 10 and mm < 100:
        #     getDistance.apfile.append('0000000' + str(mm))
        # elif mm > 100 and mm < 1000:
        #     getDistance.apfile.append('00000' + str(mm))
        # elif mm > 1000 and mm < 10000:
        #     getDistance.apfile.append('00000' + str(mm))
        # elif mm > 10000 and mm < 100000:
        #     getDistance.apfile.append('0000' + str(mm))
        
         # size Z
        getDistance.apfile.append('000000000')

        # pipe
        getDistance.apfile.append('000000000')

        # convert the apfile list to a str
        apstring = ''.join(getDistance.apfile)

        # write & save apfile on file 
        with open('./NEWAP/NEWAPfile.txt', 'a') as handle:
            handle.write(apstring)


        
        counter = 0
        getDistance.nbwalls += 1
        

# button 1 get the mouse event info
panel.bind("<Button-1>", getDistance)
# run the app till we close it 
root.mainloop()

# check the nb of walls
print(getDistance.nbwalls)

