# Anna Finlay, matplotlib part
import csv
import matplotlib.pyplot as plt



def teacher_fixup(instructor_name: str) -> tuple: #the first is the fixed up name, the second is a bool, true if a discrepancy was caught / corrected
    """
    This auxillary function will help to format teacher names for use cases 0, 1, and 2. (All except class based x axis graphs.)
    This means that we will put a newline character and remove commas. This will prevent the X axis title from being pushed off of the page.
    It will also fix any discrepancies between teacher names, and return (in the 2nd tuple val,) wether a discrepancy was caught or not.

    teacher_fixup('Childs, Henry Roberts') returns -> ('Childs\nHenry', true)
    """
    return_string = ""
    for i in range(len(instructor_name)):
        if (instructor_name[i] != ","):
            return_string += instructor_name[i]
        else:
            return_string += '\n'
            i += 1
    booll = False
    if(len(return_string.split(" ")) != 2):
        booll = True
        return_string = str(return_string.split(" ")[0] + return_string.split(" ")[1])
    return (return_string, booll)
    

# Please Note: for simplicity's sake, we will be using identical parameters
# to those developed in query_handler.py.
#                                                    *********
#the only difference being that you must include the data dict retrieved from query_handler
#                                                    *********


"""
REMINDER: (from Nathan's query_handler.py:
    main_request (int): 0) specific class,
                        1) specific department, 
                        2) professors teaching at given level in department, 
                        3) all classes of a given level
    all_instructors
    percent As
    class_level [optional]
    dept
"""

def plotter(main_request: int, all_instructors: bool, easyA: bool, data_to_plot: dict, class_level=0, dept=""):
    """
    This will return a matplotlib plot of the requested graph. Here is a use case (using the query_handler file)
    
    Query1 = Query(0, True, True, class_level = 422, dept="CIS")
    Dict1 = Query1.database_search()

                            VVV
    plotter(0, True, True, Dict1, 400, "CIS")
                            ^^^
    """
    if(easyA):
        percent_condition = "got A's"
    else:
        percent_condition = "got D's / F's"
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

    else:#please go ahead and remove the below section in the case that
        # you indeed want to remove the teachers with 0s
        '''
        rem_list = [] #teachers with 0s
        for key in data_to_plot:
            if data_to_plot[key][0] == 0:
                rem_list.append(key)
        for rem in rem_list:
            del data_to_plot[rem]
        '''
        x_list = list(data_to_plot.keys())
        counter = 0
        for i in range(len(x_list)):
            (x_list[i], booll) = teacher_fixup(x_list[i])
            if (booll):
                counter += 1
        print("In this specific graph, we caught", str(counter), "discrepancies")
        font = {'size': 6, 'weight': 'bold', 'family': 'serif'}
        plt.rc('font', **font)

    y_axis = [stuff[0] for stuff in data_to_plot.values()]
        
    fig = plt.figure(figsize = (9, 6))
    plt.bar(x_list, y_axis, color ='green', width = 0.4,)
    #################################
    plt.xticks(rotation=90)
    fig.subplots_adjust(bottom=0.24)
    #################################
    plt.xlabel(x_axis, fontsize=18)
    plt.ylabel(f"Percent of students who {percent_condition}", fontsize=15)
    plt.title(title, fontsize=20, weight='bold')
    plt.ylim(0, 100)
    plt.show()

