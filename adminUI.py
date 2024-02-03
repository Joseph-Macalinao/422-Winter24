"""
File is holding all the UI elements of the admin view.
Created to keep student/user UI and Admin UI separate
"""

import tkinter as tk
from tkinter import * # possibly change this because this is a big import!
import tkinter.font as tkFont
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import messagebox

import os as os

import admin as AdminMod

#from PIL import ImageTk, Image
#import os

#def closeAdmin():
#root.withdraw()

alreadyin = False
held_data = "./gradedata2.js"

# if there is not already a .js file
if not os.path.exists(held_data):
    is_file = False
# if there is a .js file already
else:
    is_file = True

#function to allow admin to choose file to update grades
def openNewFile():
    global alreadyin
    # if there is no .js file yet
    if is_file == False and alreadyin != True:
        file_path = filedialog.askopenfilename()
        # copy contents to gradedata.js
        with open(file_path,'r') as firstfile, open(held_data,'w') as secondfile: 
            for line in firstfile: 
                    secondfile.write(line)
        alreadyin = True

    # if there is one already
    else:
        messagebox.showerror('easyA Error', 'There is already a .js file!')
        # what should we do here? be able to replace or what

def editData():
    # file to edit data with
    if is_file == True:
        # make a form so you can see what is there? (sounds like alot of work .. lol)
        pass
    # no file to edit data with
    else:
        pass

    
def adminView():
    root=tk.Tk()
    def closeAdmin():
        root.withdraw()
    def scraperRun():
        AdminMod.scraper()
    root.title("Admin")
    root.geometry("350x600")
    root.configure(bg='gray40')
    adminButton = tk.Button(root, text="Student Mode", font=('Bold 20'), command=closeAdmin)
    adminButton.place(x=20, y=20)
    spase = tk.Text(root, height=12, width=0)
    spase.configure(bg='gray40', highlightthickness = 0, borderwidth=0)
    spase.pack()
    addnew = tk.Button(root, text="Add new .js file", font=("Bold 20"), command=openNewFile)
    addnew.pack()
    spase3 = tk.Text(root, bg='gray40', height=5, width=0, highlightthickness = 0, borderwidth=0)
    spase3.pack()
    editdata = tk.Button(root, text="Edit Data", font=('Bold 20'), command=editData)
    editdata.pack()
    spase2 = tk.Text(root, bg='gray40', height=5, width=0, highlightthickness = 0, borderwidth=0)
    spase2.pack()
    preparedata = tk.Button(root, text="Run Scraper", font=('Bold 20'), command=scraperRun)
    preparedata.pack()
    spase1 = tk.Text(root, bg='gray40', height=5, width=0, highlightthickness = 0, borderwidth=0)
    spase1.pack()
    comparedata = tk.Button(root, text="Compare Scraped Data", font=('Bold 20'), command=0)
    comparedata.pack()
