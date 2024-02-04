"""
File is holding all the UI elements of the student view.
Created to keep student/user UI and Admin UI separate
"""

import tkinter as tk
from tkinter import * 
import tkinter.font as tkFont
import matplotlib.pyplot as plt
from adminUI import adminView
from query_handler import *
from plot import *

root = tk.Tk()
def admin():
    ''' show admin pop out page '''
    adminView()

def name_dropdown_input(new_item, curr_root, frame_name, var_name, input_text, option_menu):
    ''' average formatting for a *name* *dropdown menu* on one line type frame.
    input:
        text_item, tk.Text() - a Text item with the appropriate width for the option menu.
        curr_root, tk.TK() - the tk root.  
        frame_name, Frame(root) - the frame that the dropdown input will be on.
        var_name, tk.StringVar(root) - the variable that will store the output of the choice on screen.
        input_text, str - the text in the frame (*name* above). 
        option_menu, list - the tuple of menu options that the dropdown menu will have. 
    output:
        var_output, str - the variable choice from the menu.
    ''' 
    new_item.pack(side=LEFT)
    new_item.config(state="normal")
    new_item.insert(curr_root.END, input_text)
    new_item.config(state="disabled")
    menu_width = len(max(option_menu, key=len))
    input_enter = curr_root.OptionMenu(frame_name, var_name, *option_menu)
    input_enter.config(font=("Bold", 17), fg='black', width=menu_width)#, bg="gray92")
    input_enter.pack(side=LEFT) 
    var_output = var_name

    return var_output

def query_selected_option(query):
    print(query)

    variable1 = tk.StringVar(root)
    variable1.set("None")
    variable2 = tk.StringVar(root)
    variable2.set("None")
    variable3 = tk.StringVar(root)
    variable3.set("None")
    variable4 = tk.StringVar(root)
    variable4.set("None")
    
    deptframe = Frame(root) 
    deptframe.place(x=360, y=250)
    deptframe.configure(bg="gray92")
    tmp_item = tk.Text(deptframe, height=0, width=21, font=('Bold', 17))
    tmp_item.configure(bg="gray92", fg='black',highlightthickness = 0, borderwidth=0)
    tmp = name_dropdown_input(tmp_item, tk, deptframe, variable1, "Please Enter Department", ["Biochemistry", "Bioengineering", "Biology", "Chemistry", "CIT", "CIS", "Data Science", "Environmental Studies", "Human Physiology", "Mathematics", "MACS", "Multidiscinary Science", "Neuroscience", "Physics", "Psychology"])
    variable1 = tmp

    # crn type input
    crnframe = Frame(root)
    crnframe.place(x=360, y=288)
    crnframe.configure(bg="gray92")
    new_item = tk.Text(crnframe, height=0, width=34, font=('Bold', 17)) 
    new_item.pack(side=LEFT)
    new_item.config(state="normal")
    new_item.insert(tk.END, "Class Number")
    new_item.config(state="disabled", bg="gray92", fg='black', highlightthickness = 0, borderwidth=0)
    crn_enter = tk.Entry(crnframe,width=12,font=("Helvetica 17 italic"), fg='grey60')
    #lambda func to just get rid of text in class number when entering
    crn_check = ["Department", "Department Level by Teacher", "Department Level by Class"]

    if query in crn_check:
        crn_enter.bind("<Button-1>",lambda e: crn_enter.delete(0,tk.END))
        crn_enter.insert(0, "Class Number")
        crn_enter.configure(state="disabled")
    elif query not in crn_check:
        crn_enter.bind("<Button-1>",lambda e: crn_enter.delete(0,tk.END))
        crn_enter.insert(0, "Class Number")
    #crn_enter.configure(bg="gray92", highlightthickness = 1, borderwidth=0)
    crn_enter.pack(side=RIGHT)

    # type of grading input
    distframe = Frame(root) 
    distframe.place(x=360, y=328)
    distframe.config(bg="gray92")
    tmp_item = tk.Text(distframe, height=0, width=26, font=('Bold', 17), bg="gray92", fg='black',highlightthickness = 0, borderwidth=0)
    tmp = name_dropdown_input(tmp_item, tk, distframe, variable2, "A or Passing Distribution", ["A distribution", "Pass distribution"])
    variable2 = tmp

    # level input
    
    levelframe = Frame(root)
    levelframe.place(x=360, y=366)
    levelframe.configure(bg="gray92")
    tmp_item = tk.Text(levelframe, height=0, width=39, font=('Bold', 17), bg="gray92", fg='black', highlightthickness = 0, borderwidth=0)
    if query == "Specific Class" or query == "Department":
        tmp = name_dropdown_input(tmp_item, tk, levelframe, variable3, "Level", ["None"])
        tmp_item.configure(state="disabled")
    
    elif query != "Specific Class" or query == "Department":
        tmp = name_dropdown_input(tmp_item, tk, levelframe, variable3, "Level", ["100", "200", "300", "400"])
    variable3 = tmp

    # level input
    allframe = Frame(root)
    allframe.place(x=360, y=410)
    allframe.configure(bg="gray92")
    tmp_item = tk.Text(allframe, height=0, width=28, font=('Bold', 17), bg="gray92", fg='black', highlightthickness = 0, borderwidth=0)
    tmp = name_dropdown_input(tmp_item, tk, allframe, variable4, "All Instructors/Regular Faculty", ["All Instructors", "Regular Faculty"])
    variable4 = tmp




def main():
    # initial page set up
    
    root.title("easyA")
    root.geometry("1200x750")
    root.resizable(False,False)

    #query type selection
    variable5 = tk.StringVar(root)
    variable5.set("None")

    # lists of optionmenus
    level_list = ["None", "100", "200", "300", "400"]
    

    # background :3
    root.backGroundImage=PhotoImage(file="background.png")
    root.backGroundImageLabel=Label(root, image=root.backGroundImage)
    root.backGroundImageLabel.place(x=0, y=0)
    root.canvas=Canvas(root, width=750, height=450) # was width=650, height=450
    root.canvas.configure(bg="gray92")
    root.canvas.place(x=275, y=120)

    # 'menu' buttons
    adminButton = tk.Button(root, text="Admin Mode", font=('Bold 30', 20), fg='black', command=admin)
    adminButton.place(x=40, y=40)

    # title label 
    title = tk.Label(root, text="easyA", font=("Bold 40"), bg="gray92", fg='black')
    title.place(x=550, y=160)


    #query selection
    query_selection = Frame(root)
    query_selection.place(x=360,y=220)
    query_selection.configure(bg="gray92")
    now_item = tk.Text(query_selection, height=0, width=21, font=('Bold', 17))
    now_item.configure(bg="gray92", fg="black", highlightthickness=0, borderwidth=0)
    selected = name_dropdown_input(now_item, tk, query_selection, variable5, "Enter Query Type", ["Specific Class", "Department", "Department Level by Teacher", "Department Level by Class"])
    def selection():
        x = variable5.get()
        query_selected_option(x)
        
    #query_decide = tk.Button(command=lambda: query_selected_option(variable5))
    query_decide = tk.Button(command=selection)
    query_decide.place(x=900, y=220)

    # dept type input
    """ deptframe = Frame(root) 
    deptframe.place(x=360, y=250)
    deptframe.configure(bg="gray92")
    tmp_item = tk.Text(deptframe, height=0, width=21, font=('Bold', 17))
    tmp_item.configure(bg="gray92", fg='black',highlightthickness = 0, borderwidth=0)
    tmp = name_dropdown_input(tmp_item, tk, deptframe, variable1, "Please Enter Department", ["Biochemistry", "Bioengineering", "Biology", "Chemistry", "CIT", "CIS", "Data Science", "Environmental Studies", "Human Physiology", "Mathematics", "MACS", "Multidiscinary Science", "Neuroscience", "Physics", "Psychology"])
    variable1 = tmp

    # crn type input
    crnframe = Frame(root)
    crnframe.place(x=360, y=288)
    crnframe.configure(bg="gray92")
    new_item = tk.Text(crnframe, height=0, width=34, font=('Bold', 17)) 
    new_item.pack(side=LEFT)
    new_item.config(state="normal")
    new_item.insert(tk.END, "Class Number")
    new_item.config(state="disabled", bg="gray92", fg='black', highlightthickness = 0, borderwidth=0)
    crn_enter = tk.Entry(crnframe,width=12,font=("Helvetica 17 italic"), fg='grey60')
    #lambda func to just get rid of text in class number when entering
    crn_enter.bind("<Button-1>",lambda e: crn_enter.delete(0,tk.END))
    crn_enter.insert(0, "Class Number")
    #crn_enter.configure(bg="gray92", highlightthickness = 1, borderwidth=0)
    crn_enter.pack(side=RIGHT)

    # type of grading input
    distframe = Frame(root) 
    distframe.place(x=360, y=328)
    distframe.config(bg="gray92")
    tmp_item = tk.Text(distframe, height=0, width=26, font=('Bold', 17), bg="gray92", fg='black',highlightthickness = 0, borderwidth=0)
    tmp = name_dropdown_input(tmp_item, tk, distframe, variable2, "A or Passing Distribution", ["A distribution", "Pass distribution"])
    variable2 = tmp

    # level input
    levelframe = Frame(root)
    levelframe.place(x=360, y=366)
    levelframe.configure(bg="gray92")
    tmp_item = tk.Text(levelframe, height=0, width=39, font=('Bold', 17), bg="gray92", fg='black', highlightthickness = 0, borderwidth=0)
    tmp = name_dropdown_input(tmp_item, tk, levelframe, variable3, "Level", level_list)
    #if variable5 == "Specific Class":
    #    tmp_item.configure(state="disabled")
    variable3 = tmp

    # level input
    allframe = Frame(root)
    allframe.place(x=360, y=410)
    allframe.configure(bg="gray92")
    tmp_item = tk.Text(allframe, height=0, width=28, font=('Bold', 17), bg="gray92", fg='black', highlightthickness = 0, borderwidth=0)
    tmp = name_dropdown_input(tmp_item, tk, allframe, variable4, "All Instructors/Regular Faculty", ["All Instructors", "Regular Faculty"])
    variable4 = tmp """
    

    # output of clicking button
    def output():
        output_list = []
        output_list.append(variable1.get())
        output_list.append((crn_enter.get()).replace(' ', ''))
        output_list.append(variable2.get())
        output_list.append(variable3.get())
        output_list.append(variable4.get())
        print(output_list) # has four variables
        a_vs_justpass = (output_list[2] == 'A distribution')
        if (output_list[2] == ""):
            a_vs_justpass = True
        if (output_list[1] == ""):
            output_list[1] = 0
        else:
            while(True):
                try:
                    output_list[1] = int(output_list[1])
                    output_list[3] = int(output_list[3])
                    break
                except:
                    pass
        
        my_query = Query(2, a_vs_justpass, True, class_level = output_list[1], dept=output_list[0])
        Dict1 = my_query.database_search()
        print(Dict1)
        plotter(2, a_vs_justpass, True, Dict1, output_list[1], output_list[0])
        print(output_list)

    enterButton = tk.Button(root, bg='light blue', fg='black', text="Enter", font=('Bold 24'), command=output)
    #enterButton.configure(bg="blue")
    enterButton.place(x=586, y=470)

    #non tech requirement of us telling the user about the data
    acknowledgements = Label(root, text="All data coped directly from m https://emeraldmediagroup.github.io/grade-data/ in January 2024. If you do not see your class in the listings, your \"class has been redacted\". Please refer to the UO class\
                                        \n listing above for any discrepancies, from which we copied in January 2024, so data may change. The years included in this system are from : 2013, 2014, 2015, 2016. The scraped data is from 2014\
                                        \nThank you", font=('Times, 10'))
    acknowledgements.config(bg='gray40')
    acknowledgements.place(x=55,y=650)

    tk.mainloop()
    
    return 0

if __name__ == "__main__":
    main()


'''
# dept type input
    deptframe = Frame(root) 
    deptframe.place(x=360, y=250)
    deptframe.configure(bg="gray92")
    tmp_item = tk.Text(deptframe, height=0, width=21, font=('Bold', 17))
    tmp_item.configure(bg="gray92", fg='black',highlightthickness = 0, borderwidth=0)
    tmp = name_dropdown_input(tmp_item, tk, deptframe, variable1, "Please Enter Department", ["Biochemistry", "Bioengineering", "Biology", "Chemistry", "CIT", "CIS", "Data Science", "Environmental Studies", "Human Physiology", "Mathematics", "MACS", "Multidiscinary Science", "Neuroscience", "Physics", "Psychology"])
    variable1 = tmp

    # crn type input
    crnframe = Frame(root)
    crnframe.place(x=360, y=288)
    crnframe.configure(bg="gray92")
    new_item = tk.Text(crnframe, height=0, width=34, font=('Bold', 17)) 
    new_item.pack(side=LEFT)
    new_item.config(state="normal")
    new_item.insert(tk.END, "Class Number")
    new_item.config(state="disabled", bg="gray92", fg='black', highlightthickness = 0, borderwidth=0)
    crn_enter = tk.Entry(crnframe,width=12,font=("Helvetica 17 italic"), fg='grey60')
    #lambda func to just get rid of text in class number when entering
    crn_enter.bind("<Button-1>",lambda e: crn_enter.delete(0,tk.END))
    crn_enter.insert(0, "Class Number")
    #crn_enter.configure(bg="gray92", highlightthickness = 1, borderwidth=0)
    crn_enter.pack(side=RIGHT)

    # type of grading input
    distframe = Frame(root) 
    distframe.place(x=360, y=328)
    distframe.config(bg="gray92")
    tmp_item = tk.Text(distframe, height=0, width=26, font=('Bold', 17), bg="gray92", fg='black',highlightthickness = 0, borderwidth=0)
    tmp = name_dropdown_input(tmp_item, tk, distframe, variable2, "A or Passing Distribution", ["A distribution", "Pass distribution"])
    variable2 = tmp

    # level input
    levelframe = Frame(root)
    levelframe.place(x=360, y=366)
    levelframe.configure(bg="gray92")
    tmp_item = tk.Text(levelframe, height=0, width=39, font=('Bold', 17), bg="gray92", fg='black', highlightthickness = 0, borderwidth=0)
    tmp = name_dropdown_input(tmp_item, tk, levelframe, variable3, "Level", ["None", "100", "200", "300", "400"])
    #if variable5 == "Specific Class":
    #    tmp_item.configure(state="disabled")
    variable3 = tmp

    # level input
    allframe = Frame(root)
    allframe.place(x=360, y=410)
    allframe.configure(bg="gray92")
    tmp_item = tk.Text(allframe, height=0, width=28, font=('Bold', 17), bg="gray92", fg='black', highlightthickness = 0, borderwidth=0)
    tmp = name_dropdown_input(tmp_item, tk, allframe, variable4, "All Instructors/Regular Faculty", ["All Instructors", "Regular Faculty"])
    variable4 = tmp'''