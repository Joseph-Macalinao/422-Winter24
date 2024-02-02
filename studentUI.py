"""
File is holding all the UI elements of the student view.
Created to keep student/user UI and Admin UI separate
"""

import tkinter as tk
from tkinter import * 
import tkinter.font as tkFont
import matplotlib.pyplot as plt
from adminUI import adminView


def show_graph(some_list):
    ''' plot graph from inputted data from student page. 
    input: a list of [subject, crn, A/pass, level]
    '''
    dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

    ax = plt.plot(dev_x, dev_y)
    plt.xlabel('Ages')
    plt.ylabel('Median Salary (USD)')
    plt.title('Median Salary (USD) by Age')
    plt.show()

def admin():
    ''' show admin pop out page '''
    adminView()

def name_dropdown_input(curr_root, frame_name, var_name, input_text, option_menu):
    ''' average formatting for a *name* *dropdown menu* on one line type frame.
    input:
        curr_root, tk.TK() - the tk root.  
        frame_name, Frame(root) - the frame that the dropdown input will be on.
        var_name, tk.StringVar(root) - the variable that will store the output of the choice on screen.
        input_text, str - the text in the frame (*name* above). 
        option_menu, list - the tuple of menu options that the dropdown menu will have. 
    output:
        var_output, str - the variable choice from the menu.
    '''
    new_item = curr_root.Text(frame_name, height=0, width=35, font=('Times', 15)) 
    new_item.pack(side=LEFT)
    new_item.config(state="normal")
    new_item.insert(curr_root.END, input_text)
    new_item.config(state="disabled")
    input_enter = curr_root.OptionMenu(frame_name, var_name, *option_menu)
    input_enter.pack(side=LEFT) 
    var_output = var_name

    return var_output


def main():
    # initial page set up
    root = tk.Tk()
    root.title("EasyA")
    root.geometry("900x700")
    root.configure(bg="gray40")

    variable1 = tk.StringVar(root)
    variable1.set("None")
    variable2 = tk.StringVar(root)
    variable2.set("None")
    variable3 = tk.StringVar(root)
    variable3.set("None")
      
    # 'menu' buttons
    adminButton = tk.Button(root, text="Admin Mode", font=('Times', 15), command=admin)
    adminButton.place(x=20, y=20)

    # beginning space  
    spacer1 = tk.Text(root, height=11, width=0)
    #set bg to the same as root and change highlightthickness = 0, borderwidth=0 if dont want to visually see the spacer
    spacer1.config(state="disabled", bg='gray40', highlightthickness = 0, borderwidth=0)
    spacer1.pack()

    # title label 
    title = tk.Text(root, height=2, width=15, font=('Courier 16 bold', 30))
    title.pack()
    title.config(state="normal", highlightthickness = 0, borderwidth=0)
    title.tag_configure("center", justify='center')
    title.insert(tk.END, "EasyA")
    title.tag_add("center", "1.0", "end")
    title.config(state="disabled", bg="gray40")

    # dept type input
    deptframe = Frame(root) 
    deptframe.pack()
    tmp = name_dropdown_input(tk, deptframe, variable1, "Please Enter Department", ["Biochemistry", "Bioengineering", "Biology", "Chemistry", "CIT", "CS", "Data Science", "Environmental Studies", "Human Physiology", "Mathematics", "MACS", "Multidiscinary Science", "Neuroscience", "Physics", "Psychology"])
    variable1 = tmp

    # crn type input
    #crn = tk.Text(root, height=2, width=43, pady=15, font=('Times', 15))
    #crn.pack()
    #crn.insert(tk.END, "Please Enter Class Number")
    crn_enter = tk.Entry(root,width=42,font=('Times', 15))
    #lambda func to just get rid of text in class number when entering
    crn_enter.bind("<Button-1>",lambda e: crn_enter.delete(0,tk.END))
    crn_enter.insert(0, "Please Enter Class Number")
    crn_enter.pack()

    # type of grading input
    distframe = Frame(root) 
    distframe.pack()
    tmp = name_dropdown_input(tk, distframe, variable2, "A or Passing Distribution", ["A distribution", "Pass distribution"])
    variable2 = tmp

    # level input
    levelframe = Frame(root)
    levelframe.pack()
    tmp = name_dropdown_input(tk, levelframe, variable3, "Level", ["None", "100", "200", "300", "400"])
    variable3 = tmp

    # output of clicking button
    def output():
        output_list = []
        output_list.append(variable1.get())
        output_list.append((crn_enter.get()).replace(' ', ''))
        output_list.append(variable2.get())
        output_list.append(variable3.get())
        print(output_list) # has four variables
        show_graph(output_list)



    enterButton = tk.Button(root, text="Enter", font=('Times', 20), command=output)
    enterButton.pack(pady=28)

    #non tech requirement of us telling the user about the data
    acknowledgements = Label(root, text="All data coped directly from m https://emeraldmediagroup.github.io/grade-data/ in Janruary 2024.\
                                        \nIf you do not see your class in the listings, your \"class has been redacted\".\
                                        \nPlease refer to the UO class listing above for any discrepancies, from which we copied in Janruary 2024, so data may change.\
                                        \nThe years included in this system are from : 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023.\
                                        \nThank you", font=('Times, 10'))
    acknowledgements.config(bg='gray')
    acknowledgements.place(x=10,y=600)

    tk.mainloop()
    
    return 0


if __name__ == "__main__":
    main()



# old code without formatting -- for reference
'''
root = tk.Tk()
root.title("Grade Analysis")

root.geometry("700x700")
root.configure(bg="gray")
variable1 = tk.StringVar(root)

#spacer2 = tk.Text(root, height=4, width=0)
#spacer2.pack()

# beginning space @_@
#spacer1 = tk.Text(root, height=1, width=0)
#spacer1.pack()

# 'menu' buttons
adminButton = tk.Button(root, text="Admin Mode", font=('Times', 15), command=admin)
adminButton.place(x=20, y=20)

#spacer2 = tk.Text(root, height=3.5, width=0)
#spacer2.pack()

# title label 
title = tk.Text(root, height=2, width=15, font=('Times bold', 24))
title.pack()
title.config(state="normal")
title.insert(tk.END, "Grade Analysis")
title.config(state="disabled")

deptframe = Frame(root)
deptframe.pack()

# form text
depart = tk.Text(deptframe, height=0, width=35, font=('Times', 15)) 
depart.pack(side=LEFT)
depart.config(state="normal")
depart.insert(tk.END, "Please Enter Department")
depart.config(state="disabled")
variable1.set("None")
#var_1 = StringVar()
depart_enter = tk.OptionMenu(deptframe, variable1, "Physics", "Biology", "Chemistry", "Earth Science", "Human Physiology")
#depart_enter = tk.OptionMenu(root, var_1, "Physics", "Biology", "Chemistry", "Earth Science", "Human Physiology")
#depart_enter.place(x=380, y=144)
depart_enter.pack(side=LEFT)
#d = depart_enter.get()

crn = tk.Text(root, height=2, width=43, pady=15, font=('Times', 15))
crn.pack()

crn.insert(tk.END, "Please Enter CRN")
crn_enter = tk.Entry(root)
crn_enter.pack()
#crn_enter.get()

#spacer3 = tk.Text(root, height=0.5, width=0)
##spacer3.pack()

distframe = Frame(root)
distframe.pack()

variable2 = tk.StringVar(root)
variable2.set("None")
choice = tk.Text(distframe, height=0, width=35, font=('Times', 15))
choice.pack(side=LEFT)
choice.config(state="normal")
choice.insert(tk.END, "A or Passing Distribution")
choice.config(state="disabled")
w = tk.OptionMenu(distframe, variable2, "A distribution", "Pass distribution")
#w.place(x=380, y=280)
w.pack(side=LEFT)

#spacer4 = tk.Text(root, height=0.5, width=0)
#spacer4.pack()

levelframe = Frame(root)
levelframe.pack()

variable3 = tk.StringVar(root)
variable3.set("None")
level = tk.Text(levelframe, height=0, width=35, font=('Times', 15))
level.pack(side=LEFT)
level.config(state="normal")
level.insert(tk.END, "Level")
level.config(state="disabled")
z = tk.OptionMenu(levelframe, variable3, "None", "100", "200", "300", "400")
#w.place(x=380, y=280)
z.pack(side=LEFT)

#spacer5 = tk.Text(root, height=0.5, width=0)
#spacer5.pack()

enterButton = tk.Button(root, text="Enter", font=('Times', 20), command=show_graph)
enterButton.pack(pady=28)

tk.mainloop()
'''