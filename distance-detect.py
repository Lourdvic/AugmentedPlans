from tkinter import *
from PIL import ImageTk, Image
import math
import cv2


root = Tk()
imgpath = "plan\white plan\plan-maison-traditionnelle-maison-gallegos-ebe25052a-775x450.jpeg"
img = ImageTk.PhotoImage(Image.open(imgpath))
dimg = cv2.imread(imgpath)
window_name = "plan image"
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
counter = 0
x0 = 0
x1 = 0
y0 = 0
y1 = 0


def getDistance(event):
    global counter, x0, y0, x1, y1
    if counter == 0:
        x0 = event.x
        y0 = event.y
        counter += 1
    elif counter == 1:
        x1 = event.x
        y1 = event.y
        counter += 1
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
        print(reeldim)
        counter = 0


panel.bind("<Button-1>", getDistance)
root.mainloop()