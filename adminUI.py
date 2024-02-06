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


held_data = "./gradedata2.js" # holds input .js

# global booleans
alreadyin = False # whether a .js has been inputted in THIS run
if os.path.exists(held_data): # whether a .js has already been inputted in the past
    is_file = True
else:
    is_file = False

def update_js():
    win = tk.Toplevel()
    win.geometry("310x130")
    win.configure(bg="gray92")
    win.wm_title("Add/Replace Data")
    l = tk.Label(win, text="There is already a .js file. Do you wish\
    \n to replace it?", font=("Bold 16"))
    l.configure(bg="gray92")
    l.place(x=10, y=10)
    yes_b = tk.Button(win, text="Yes", command=openNewFile, font=("Bold 16"))
    yes_b.place(x=70, y=85)
    no_b = tk.Button(win, text="No", command=win.destroy, font=("Bold 16"))
    no_b.place(x=180, y=85)

def openNewFile():
    global alreadyin
    file_path = filedialog.askopenfilename()
    if file_path != '':
        if os.path.basename(file_path)[-2:] != 'js':
            err = tk.Toplevel()
            err.geometry("300x100")
            err.configure(bg="gray92")
            err.wm_title("Error!")
            l = tk.Label(err, text="File must be .js type", font=("Bold 16"))
            l.configure(bg="gray92")
            l.place(x=10, y=10)
        else:
            with open(file_path,'r') as firstfile, open(held_data,'w') as secondfile: 
                for line in firstfile: 
                    secondfile.write(line)
            err = tk.Toplevel()
            err.geometry("300x100")
            err.configure(bg="gray92")
            err.wm_title("Success")
            l = tk.Label(err, text="Inputted '" + os.path.basename(file_path)+"'", font=("Bold 16"))
            l.configure(bg="gray92")
            l.place(x=10, y=10)
            AdminMod.create_json_data("gradedata2.js")
            alreadyin = True
            
def add_button():
    # if there is a .js file already
    if (is_file == True or alreadyin == True) or (is_file == True and alreadyin == True):
        update_js()
    # if there isn't a .js file already
    else:
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
    some_button = tk.Button(root, text="Add/Replace.js file", font=("Bold 20"), command=add_button)
    some_button.pack()
    spase2 = tk.Text(root, bg='gray90', height=5, width=0, highlightthickness = 0, borderwidth=0)
    spase2.pack()
    preparedata = tk.Button(root, text="Run Scraper", font=('Bold 20'), command=scraperRun)
    preparedata.pack()
    
def main():
    adminView()   
    tk.mainloop()

if __name__ == "__main__":
    main()
