# importing all files  from tkinter 
from tkinter import * 
from tkinter import ttk 
  
# import only asksaveasfile from filedialog 
# which is used to save file in any extension 
from tkinter.filedialog import asksaveasfile 
  
#root = Tk() 
#root.geometry('200x150') 
  
# function to call when user press 
# the save button, a filedialog will 
# open and ask to save file 
def save(): 
    files = [('Png Files', '*.png'), 
             ('Jpg Files', '*.jpg')] 
    file = asksaveasfile(filetypes = files, defaultextension = files)
    return file.name
  
#btn = ttk.Button(root, text = 'Save', command = lambda : save()) 
#btn.pack(side = TOP, pady = 20) 