"""
File is holding all the UI elements of the admin view.
Created to keep student/user UI and Admin UI separate
"""

import tkinter as tk
from tkinter import * # possibly change this because this is a big import!
import tkinter.font as tkFont
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter.messagebox import showinfo

import os 

import admin as AdminMod

#from PIL import ImageTk, Image
#import os

##root = None
#held_data = "./gradedata2.js"

def make_new():
    root = tk.Tk()
#root = tk.Tk()
#global alreadyin
#alreadyin = tk.StringVar(root)
#alreadyin.set("False")
#global is_file
#is_file = tk.StringVar(root)
#if os.path.exists(held_data):
#    is_file.set("True")
#else:
#    is_file.set("False")
is_file = False
alreadyin = False

# if there is not already a .js file
#if os.path.exists(held_data):
#    is_file = True

def openNewFile():
    #global alreadyin
    file_path = filedialog.askopenfilename()
    if file_path != '':
        print(file_path, held_data)
        # copy contents to gradedata.js
        with open(file_path,'r') as firstfile, open(held_data,'w') as secondfile: 
            for line in firstfile: 
                secondfile.write(line)
        alreadyin = ("True")   

def new_js():
    win = tk.Toplevel()
    win.geometry("310x100")
    win.configure(bg="gray92")
    win.wm_title("Add/Replace Data")
    l = tk.Label(win, text="There is already a .js file. Do you wish\
    \n to replace it?", font=("Bold 16"))
    l.place(x=10, y=10)
    yes_b = tk.Button(win, text="Yes", command=openNewFile, font=("Bold 16"))
    yes_b.place(x=70, y=65)
    no_b = tk.Button(win, text="No", command=win.destroy, font=("Bold 16"))
    no_b.place(x=180, y=65)

def add_button():
    #global is_file
    #global alreadyin
    # if there is already a .js file
    if is_file == False and alreadyin != True:
        new_js()
        #addnew = tk.Button(root, text="Add/Replace.js file", font=("Bold 20"), command=new_js)
        #addnew.pack()

    else:
    # if there isn't a file already:
        #addnew = tk.Button(root, text="Add/Replace.js file", font=("Bold 20"), command=openNewFile)
        #addnew.pack()
        openNewFile()


def adminView():
    global is_file
    global alreadyin
    root=tk.Tk()
    def closeAdmin():
        root.withdraw()
    def scraperRun():
        AdminMod.scraper()
    root.title("Admin")
    root.geometry("350x600")
    root.configure(bg='gray90')
    adminButton = tk.Button(root, text="Student Mode", font=('Bold 20'), command=closeAdmin)
    adminButton.place(x=20, y=20)
    spase = tk.Text(root, height=12, width=0)
    spase.configure(bg='gray90', highlightthickness = 0, borderwidth=0)
    spase.pack()
    #function to allow admin to choose file to update grades
    '''
    def openNewFile():
        global alreadyin
        file_path = filedialog.askopenfilename()
        if file_path != '':
            print(file_path, held_data)
            # copy contents to gradedata.js
            with open(file_path,'r') as firstfile, open(held_data,'w') as secondfile: 
                for line in firstfile: 
                    secondfile.write(line)
            alreadyin = True    
    
    def new_js():
        win = tk.Toplevel()
        win.geometry("310x100")
        win.configure(bg="gray92")
        win.wm_title("Add/Replace Data")
        l = tk.Label(win, text="There is already a .js file. Do you wish\
        \n to replace it?", font=("Bold 16"))
        l.place(x=10, y=10)
        yes_b = tk.Button(win, text="Yes", command=openNewFile, font=("Bold 16"))
        yes_b.place(x=70, y=65)
        no_b = tk.Button(win, text="No", command=win.destroy, font=("Bold 16"))
        no_b.place(x=180, y=65)

    def add_button():
        # if there is already a .js file
        if is_file == False and alreadyin != True:
            print("hi")
            new_js()
            #addnew = tk.Button(root, text="Add/Replace.js file", font=("Bold 20"), command=new_js)
            #addnew.pack()

        else:
        # if there isn't a file already:
            #addnew = tk.Button(root, text="Add/Replace.js file", font=("Bold 20"), command=openNewFile)
            #addnew.pack()
            openNewFile()
    '''
    #print(is_file.get(), alreadyin.get())
    if is_file == False and alreadyin != True:
        print("hi")
    some_button = tk.Button(root, text="Add/Replace.js file", font=("Bold 20"), command=new_js)#add_button)
    some_button.pack()
    spase2 = tk.Text(root, bg='gray90', height=5, width=0, highlightthickness = 0, borderwidth=0)
    spase2.pack()
    preparedata = tk.Button(root, text="Run Scraper", font=('Bold 20'), command=scraperRun)
    preparedata.pack()
    tk.mainloop()
    #spase1 = tk.Text(root, bg='gray40', height=5, width=0, highlightthickness = 0, borderwidth=0)
    #spase1.pack()
    #comparedata = tk.Button(root, text="Compare Scraped Data", font=('Bold 20'), command=0)
    #comparedata.pack()
