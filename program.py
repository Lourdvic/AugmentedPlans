from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile 

 

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("AP file Converter")
        self.minsize(640, 400)
 
        self.labelFrame = ttk.LabelFrame(self, text = "Open File")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
 
        self.button()
 
 
 
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A Plan",command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
 
 
    def fileDialog(self):
 
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select Your Plan", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.label = ttk.Label(self.labelFrame, text = "")
        self.label.grid(column = 1, row = 2)
        self.label.configure(text = self.filename)
        return self.filename