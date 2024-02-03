# Anna Finlay, matplotlib part
import csv
import matplotlib.pyplot as plt
from query_handler import * #take this line out later
#for now, we will be importing the file so that we can get the
#different lists of data



Query1 = Query(2, True, True, class_level = 400, dept="CIS")
"""
REMINDER: (from Nathan's query_handler.py:
Parameters:
    main_request (int): 0) specific class,
                        1) specific department, 
                        2) professors teaching at given level in department, 
                        3) all classes of a given level
    all_instructors
    percent As
    class_level [optional]
    dept
"""

Dict1 = Query1.database_search()
print(Dict1)


def teacher_fixup(instructor_name: str) -> str:
    return_string = ""
    for i in range(len(instructor_name)):
        if (instructor_name[i] != ","):
            return_string += instructor_name[i]
        else:
            return_string += '\n'
            i += 1
    return return_string
    

# Please Note: for simplicity's sake, we will be using identical parameters
# to those developed in query_handler.py. The difference

def plotter(main_request: int, all_instructors: bool, easyA: bool, data_to_plot: dict, class_level=0, dept=""):
    if(easyA):
        percent_condition = "got A's"
    else:
        percent_condition = "just passed"
    title = "Grade graph"
    x_axis = "Regular Faculty"
    if (all_instructors):
        x_axis = "Instructors"
    if (main_request == 0):
        title = class_level
    elif (main_request == 1):
        title = f"{dept} Department"
    elif (main_request == 2):
        title = f"{dept} Department -- {class_level} Level"
    elif (main_request == 3):
        title = f"{class_level} Level Classes"
        x_axis = "Classes Offered"
    
    if (main_request == 3): #3 is a unique case, where the keys of the dict are CLASSES not TEACHERS
        
        x_list = list(data_to_plot.keys())
        for i, a_class in enumerate(x_list):
            if (a_class[:len(dept)] == dept):
                x_list[i] = a_class[len(dept):] # this part just removes stuff like "CIS" if it's attatched

    else:
        x_list = list(data_to_plot.keys())
        for i in range(len(x_list)):
            x_list[i] = teacher_fixup(x_list[i])
        font = {'size': 6}
        plt.rc('font', **font)

    y_axis = [stuff[0] for stuff in data_to_plot.values()]
        
    fig = plt.figure(figsize = (9, 7))
    plt.bar(x_list, y_axis, color ='green', width = 0.4,)
    plt.xticks(rotation=90)
    plt.xlabel(x_axis, fontsize=18)
    plt.ylabel(f"Percent of students who {percent_condition}", fontsize=15)
    plt.title(title, fontsize=10)
    plt.show()
    print(x_list)
            
        
#                       VVV
plotter(2, True, True, Dict1, 400, "CIS")
#                       ^^^
