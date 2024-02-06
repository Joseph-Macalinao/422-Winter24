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

depts = {
"AA" : "Allied Arts", 
"AAA": "Architecture and Allied Arts",
"AAAP": "Historic Preservation",
"AAD": "Arts and Administration",
"ACTG": "Accounting",
"AEIS": "Academic Eng for Intl Students",
"AFR": "African Studies",
"AIM": "Applied Information Management",
"ANTH": "Anthropology",
"ARB": "Arabic",
"ARCH": "Architecture",
"ARH": "Art History", 
"ART": "Art",
"ARTC": "Ceramics",
"ARTD":  "Art & Technology",
"ARTF": "Fibers",
"ARTM": "Metalsmithing & Jewelry",
"ARTO": "Photography",
"ARTP": "Painting",
"ARTR": "Printmaking", 
"ARTS": "Sculpture",
"ASIA": "Asian Studies",
"ASL": "American Sign Language",
"ASTR": "Astronomy",
"BA": "Business Administration",
"BE": "Business Environment", 
"BI": "Biology",
"CAS": "College of Arts & Sciences",
"CDS": "Communication Disorders & Sci",
"CFT": "Couples & Family Therapy", 
"CH": "Chemistry",
"CHN": "Chinese",
"CINE": "Cinema Studies",
"CIS": "Computer & Information Science",
"CIT": "Computer Information Technology",
"CLAS":  "Classics",
"COLT": "Comparative Literature",
"CPSY": "Counseling Psychology",
"CRES": "Conflict & Dispute Resolution",
"CRWR": "Creative Writing",
"DAN": "Dance Professional",
"DANC": "Dance Activity",
"DSC": "Data Science",
"EALL": "East Asian Lang & Literature",
"EC": "Economics",
"EDLD": "Educational Leadership",
"EDST": "Educational Studies",
"EDUC": "Education",
"ENG": "English",
"ENVS": "Environmental Studies",
"ES": "Ethnic Studies",
"FHS": "Family & Human Services",
"FIN": "Finance",
"FLR": "Folklore",
"FR":  "French",
"GEOG": "Geography",
"GEOL":  "Geology",
"GER": "German",
"GRK": "Greek",
"HBRW": "Hebrew",
"HC": "Honors College", 
"HIST": "History",
"HPHY": "Human Physiology",
"HUM": "Humanities",
"IARC": "Interior Architecture",
"INTL": "International Studies",
"ITAL": "Italian",
"J": "Journalism",
"JDST": "Judaic Studies", 
"JPN": "Japanese",
"KRN": "Korean",
"LA": "Landscape Architecture",
"LAS": "Latin American Studies",
"LAT": "Latin",
"LAW": "Law",
"LIB": "Library",
"LING": "Linguistics",
"LT": "Language Teaching",
"MATH": "Mathematics",
"MDVL": "Medieval Studies",
"MGMT": "Management",
"MIL": "Military Science",
"MKTG": "Marketing",
"MUE": "Music :Education",
"MUJ": "Music Jazz Studies",
"MUP": "Music Performance",
"MUS": "Music",
"PD": "Production Design",
"PEF": "PE Fitness",
"PEL": "PE Leadership",
"PEO": "PE Outdoor Pursuits",
"PHIL": "Philosophy",
"PHYS": "Physics",
"PORT": "Portuguese",
"PPPM": "Planning Public Policy Mgmt",
"PS": "Political Science",
"PSY": "Psychology",
"REL": "Religious Studies",
"RL": "Romance Languages",
"RUSS": "Russian",
"SBUS": "Sports Business",
"SCAN": "Scandinavian",
"SOC": "Sociology",
"SPAN": "Spanish",
"SPD": "Sports Product Design",
"SPED": "Special Education",
"SPSY": "School Psychology",
"SWAH": "Swahili",
"SWED": "Swedish",
"TA": "Theater Arts",
"WGS": "Women’s & Gender Studies",
"WR": "Writing"
}



root = tk.Tk()
global variable1
variable1 = tk.StringVar(root)
variable1.set("None")
global variable2 
variable2 = tk.StringVar(root)
variable2.set("None")
global variable3 
variable3 = tk.StringVar(root)
variable3.set("None")
global variable4 
variable4 = tk.StringVar(root)
variable4.set("None")
global crnEnter
crnEnter = tk.StringVar(root)
crnEnter.set("None")
global selected
selected = tk.StringVar(root)
selected.set("None")


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
    input_enter.config(font=("Bold", 17), fg='black', bg="white" ,width=menu_width)
    input_enter.pack(side=LEFT) 
    var_output = var_name

    return var_output

def class_input(var_name, new):
    '''
    aux function to help set StringVar with the .Entry widget from Tkinter
    var_name - String Var - holder for "new" text
    new - str - text for StringVar to be .set() with

    uses Tkinter .set() function to provide text to StringVar provided
    '''
    var_name.set(new)

def error_msg(msg):
    '''
    pop out for bad class request 
    
    msg - str - Message for the error window to show
    '''
    err = tk.Toplevel()
    err.geometry("500x250")
    err.backGroundImage=PhotoImage(file="backgroundcopy.png")
    err.backGroundImageLabel=Label(err, image=err.backGroundImage)
    err.backGroundImageLabel.place(x=0, y=0)
    err.wm_title("Error Msg")
    l = tk.Label(err, text=msg, font=("Bold 16"), fg="black")
    l.configure(bg="gray92")
    l.place(x=100, y=100)

def graph_my_output_list(output_list: list)-> None: #graphs the output list
    '''
    Graphs data from output_list using Matplotlib

    '''
    class_conversion = {}

    for key in depts.keys():
        class_conversion[f'{key} : {depts[key]}'] = key
    class_conversion['None'] = 'None'
    output_list[0] = class_conversion[output_list[0]]

    #NOTE - have most of the classes but need to check environmental science and the rest of them. also find how to do "MACS"
    my_int = ["Specific Class", "Department", "Department Level by Teacher", "Department Level by Class"].index(output_list[5])
    a_vs_justpass = bool(output_list[2] == 'A distribution')
    all_inst_vs_reg_fac = bool(output_list[4] == 'All Instructors')

    if(my_int != 0):
        if (output_list[3] == 'None'):
            output_list[3] = 0
            
        my_query = Query(my_int, all_inst_vs_reg_fac, a_vs_justpass, class_level = int(output_list[3]), dept=output_list[0])
        Dict1 = my_query.database_search()
        plotter(my_int, all_inst_vs_reg_fac, a_vs_justpass, Dict1, int(output_list[3]), output_list[0])
    else:
        try: 
            output_list[1] = int(output_list[1])
        except:
            error_msg("Can't search for this class,\nas it is not an integer!")
            print("Cannot search for this class, as it is not an integer!")
            return
        my_query = Query(my_int, a_vs_justpass, all_inst_vs_reg_fac, class_level = int(output_list[1]), dept=output_list[0])
        Dict1 = my_query.database_search()
        if Dict1 != {}:
            plotter(my_int, a_vs_justpass, all_inst_vs_reg_fac, Dict1, int(output_list[1]), output_list[0])
        if Dict1 == {}:
            error_msg("ERROR: Class not found.\n Check class input and try again.")


def query_selected_option(query, v1, v2, v3, v4, entry):
    '''
    Aux function to enter filtered data for classes
    lower function chosen to be .set() values for v1-v4

    v1-v4 - StringVar - holders for StringVar from Tkinter library dropdowns
    entry - StringVar - holder for .Entry widget from Tkinter

    output - after class filter has been entered, informatin is ".set()" for 
    graphical representation
    '''
    # canvas
    root.canvas=Canvas(root, width=580, height=210)
    root.canvas.configure(bg="white")
    root.canvas.place(x=340, y=270)
    # dept frame input
    deptframe = Frame(root) 
    deptframe.place(x=360, y=288)
    deptframe.configure(bg="white")
    tmp_item = tk.Text(deptframe, height=0, width=21, font=('Bold', 17))
    tmp_item.configure(bg="white", fg='black',highlightthickness = 0, borderwidth=0)

    a_list = []
    for key in depts.keys():
        a_list.append(f'{key} : {depts[key]}')
    tmp1 = name_dropdown_input(tmp_item, tk, deptframe, v1, "Please Enter Department", a_list)

    # crn type input
    crnframe = Frame(root)
    crnframe.place(x=360, y=328)
    crnframe.configure(bg="white")
    new_item = tk.Text(crnframe, height=0, width=34, font=('Bold', 17)) 
    new_item.pack(side=LEFT)
    new_item.config(state="normal")
    new_item.insert(tk.END, "Class Number")
    new_item.config(state="disabled", bg="white", fg='black', highlightthickness = 0, borderwidth=0)
    tmp_item2 = tk.Text(crnframe, height=0, width=26, font=('Bold', 17), bg="white", fg='black',highlightthickness = 0, borderwidth=0)
    crn_entry = tk.Entry(root, width=12,font=("Helvetica 17 italic"), fg='grey60')
    crn_entry.place(x=700, y=314)
    crn_check = ["Department", "Department Level by Teacher", "Department Level by Class"]

    if query in crn_check:
        crn_entry.configure(state="disabled")

    # type of grading input
    distframe = Frame(root) 
    distframe.place(x=360, y=366)
    distframe.config(bg="white")
    tmp_item = tk.Text(distframe, height=0, width=26, font=('Bold', 17), bg="white", fg='black',highlightthickness = 0, borderwidth=0)
    tmp2 = name_dropdown_input(tmp_item, tk, distframe, v2, "A or Passing Distribution", ["A distribution", "Pass distribution"])

    # level input  
    levelframe = Frame(root)
    levelframe.place(x=360, y=400)
    levelframe.configure(bg="white")
    tmp_item = tk.Text(levelframe, height=0, width=39, font=('Bold', 17), bg="white", fg='black', highlightthickness = 0, borderwidth=0)
    if query == "Specific Class" or query == "Department":
        tmp3 = name_dropdown_input(tmp_item, tk, levelframe, v3, "Level", ["None"])
        tmp_item.configure(state="disabled")
    
    elif query != "Specific Class" or query == "Department":
        tmp3 = name_dropdown_input(tmp_item, tk, levelframe, v3, "Level", ["100", "200", "300", "400", "500", "600"])


    # level input
    allframe = Frame(root)
    allframe.place(x=360, y=435)
    allframe.configure(bg="white")
    tmp_item = tk.Text(allframe, height=0, width=28, font=('Bold', 17), bg="white", fg='black', highlightthickness = 0, borderwidth=0)
    tmp4 = name_dropdown_input(tmp_item, tk, allframe, v4, "All Instructors/Regular Faculty", ["All Instructors", "Regular Faculty"])

    #setting globals to be able to .get() later on
    def selectQuery():
        '''
        aux function to .set() variable1-variable4 with dropdown and Entry filters
        for classes
        '''
        class_input(entry, crn_entry.get())
        #print(crnEnter)
        variable1.set(tmp1)
        variable2.set(tmp2)
        variable3.set(tmp3)
        variable4.set(tmp4)
    selection = Frame(root)
    selection.place(x=360, y=450)
    selection.configure(bg="white")
    final = tk.Button(root, text="Use Filters", font=('Bold 30', 20), fg='black', command=selectQuery)
    final.place(x=500, y=500)


def main():
    # initial page set up
    
    root.title("easyA")
    root.geometry("1200x750")
    root.resizable(False,False)

    variable1 = tk.StringVar(root)
    variable1.set("None")
    variable2 = tk.StringVar(root)
    variable2.set("None")
    variable3 = tk.StringVar(root)
    variable3.set("None")
    variable4 = tk.StringVar(root)
    variable4.set("None")
    crnEnter = tk.StringVar(root)
    crnEnter.set("None")

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
    title = tk.Label(root, text="EasyA", font=("Bold 40"), bg="gray92", fg='black')
    title.place(x=550, y=160)

    #query selection
    query_selection = Frame(root)
    query_selection.place(x=360,y=232)
    query_selection.configure(bg="gray92")
    now_item = tk.Text(query_selection, height=0, width=21, font=('Bold', 17))
    now_item.configure(bg="gray92", fg="black", highlightthickness=0, borderwidth=0)
    selected = name_dropdown_input(now_item, tk, query_selection, variable5, "Enter Query Type", ["Specific Class", "Department", "Department Level by Teacher", "Department Level by Class"])
    def selection():
        selected_query = selected.get()
        x = variable5.get()
        query_selected_option(x, variable1, variable2, variable3, variable4, crnEnter)
    
    #button to "lock in" class filters
    query_decide = tk.Button(root, bg='green', text="✅", command=selection)
    query_decide.place(x=895, y=230)
 
    # output of clicking button ~ leading to a graphical repr of cladd data
    def output():
        output_list = []
        output_list.append(variable1.get())
        output_list.append(crnEnter.get())
        output_list.append(variable2.get())
        output_list.append(variable3.get())
        output_list.append(variable4.get())
        output_list.append(selected.get())
        graph_my_output_list(output_list)
        
    enterButton = tk.Button(root, bg='light blue', fg='black', text="Enter", font=('Bold 24'), command=output)
    enterButton.place(x=650, y=500)
    
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
