import tkinter as tk
from tkinter import * # possibly change this because this is a big import!
import tkinter.font as tkFont
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Grade Analysis")

root.geometry("700x700")
variable1 = tk.StringVar(root)

def show_graph():
    dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

    ax = plt.plot(dev_x, dev_y)
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')
    plt.title('Median Salary (USD) by Age')
    plt.show()

def admin():
    adminRoot = tk.Tk()
    adminRoot.geometry("700x700")
    adminRoot.title("Admin")

# beginning space @_@
spacer1 = tk.Text(root, height=1, width=0)
spacer1.pack()

# 'menu' buttons
userButton = tk.Button(root, text="User", font=('Times', 15))
userButton.place(x=15, y=10)
adminButton = tk.Button(root, text="Admin", font=('Times', 15), command=admin)
adminButton.place(x=70, y=10)

spacer2 = tk.Text(root, height=4, width=0)
spacer2.pack()

# title label 
title = tk.Text(root, height=2, width=17, font=('Times bold', 24))
title.pack()
title.insert(tk.END, "Grade Analysis")

# form text
depart = tk.Text(root, height=2, width=35, font=('Times', 15))
depart.pack()
depart.insert(tk.END, "Please Enter Department")
variable1.set("None")
#var_1 = StringVar()
depart_enter = tk.OptionMenu(root, variable1, "Physics", "Biology", "Chemistry", "Earth Science", "Human Physiology")#, command=func)
#depart_enter = tk.OptionMenu(root, var_1, "Physics", "Biology", "Chemistry", "Earth Science", "Human Physiology")
depart_enter.place(x=380, y=144)
#depart_enter.pack()
#d = depart_enter.get()

crn = tk.Text(root, height=2, width=35, font=('Times', 15))
crn.pack()
crn.insert(tk.END, "Please Enter CRN")
crn_enter = tk.Entry(root)
crn_enter.pack()
#crn_enter.get()

spacer3 = tk.Text(root, height=0.5, width=0)
spacer3.pack()

variable2 = tk.StringVar(root)
variable2.set("None")
choice = tk.Text(root, height=2, width=35, font=('Times', 15))
choice.pack()
choice.insert(tk.END, "A or Passing Distribution")
w = tk.OptionMenu(root, variable2, "A distribution", "Pass distribution")
w.place(x=380, y=280)
#w.pack()

spacer4 = tk.Text(root, height=0.5, width=0)
spacer4.pack()

enterButton = tk.Button(root, text="Enter", font=('Times', 20), command=show_graph)
enterButton.pack()

#adminButton = tk.Button(root, text="Admin", command=admin)
#adminButton.pack()

tk.mainloop()