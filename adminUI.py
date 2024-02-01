"""
File is holding all the UI elements of the admin view.
Created to keep student/user UI and Admin UI separate
"""

import tkinter as tk
from tkinter import * # possibly change this because this is a big import!
import tkinter.font as tkFont
from tkinter import filedialog
import matplotlib.pyplot as plt

#from PIL import ImageTk, Image
#import os

#def closeAdmin():
#root.withdraw()

#function to allow admin to choose file to update grades
def openNewFile():
    file_path = filedialog.askopenfilename()

def adminView():
    root=tk.Tk()
    def closeAdmin():
        root.withdraw()
    root.title("Admin")
    root.geometry("700x700")
    adminButton = tk.Button(root, text="Student Mode", font=('Times', 15), command=closeAdmin)
    adminButton.place(x=20, y=20)
    #img = Image.open("fedor-PtW4RywQV4s-unsplash.jpg")
    #img = img.resize((34, 26))
    #bg = PhotoImage(file = "logo.png")
    #canvas1.create_image( 0, 0, image = bg,  anchor = "nw") 
    spase = tk.Text(root, height=14, width=0)
    spase.pack()
    editdata = tk.Button(root, text="Edit Data", font=('Times bold', 24), command=openNewFile)
    editdata.pack()
    spase1 = tk.Text(root, height=5, width=0)
    spase1.pack()
    comparedata = tk.Button(root, text="Compare Scraped Data", font=('Times bold', 24), command=0)
    comparedata.pack()
