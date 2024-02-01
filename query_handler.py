"""
Module containing functions for handling and resolving queries.
Primarily used by the standard UI:
    UI gathers information necessary and creates a Query object
"""

from database import *

class Query:
    """
    Query objects contain all specifications required to fully identify a query.

    Parameters:
        main_request (int): Enumerated identifier for (0) specific class, (1) specific department, 
                                            (2) professors teaching at given level in department, 
                                            and (3) all classes of a given level                                  
        
        class_input (int): Data specifying class level/ class number
        dept (str): Data specifying department 
        
        all_instructors (bool): Boolean identifying "all instructors" vs "regular faculty"
        easy_a (bool): Boolean identifying % of A's vs % of D/F's

    Returns:
        something 
    """
    def __init__(self, req, all_instructors, easyA, class_level=0, dept=""):
        self.main_request = req
        self.class_input = class_level
        self.dept = dept
        self.all_instructors = all_instructors
        self.easy_a = easyA


    def database_search(self):
        """
        High level function: 
            Calls specific database searches (as defined in database.py)
        
        """

        if self.main_request == 0:
            result = class_search(self.class_input, self.dept ,self.all_instructors, self.easy_a) 

        elif self.main_request == 1:
            result = department_search(self.dept, self.all_instructors, self.easy_a) 

        elif self.main_request == 2:
            result = level_department_search(self.class_input, self.dept, self.all_instructors, self.easy_a) 

        elif self.main_request == 3:
            result = class_level_search(self.class_input, self.dept, self.all_instructors, self.easy_a) 

        else:
            # error handling if needed
            pass

        # temorary return
        return result

        # TODO: define result in a meaningful way to be used for graphing.

        # returned result is a dict that takes the following format:
        #   Each key corresponds to a professor name (for queries 0~2) or class name (for query 3)
        #   Each value corresponds to a list of 2 elements with the following format: 
        #       [A% / D&F% Average (float), number of entries (int)]
        #   
        #   number of entries is relevant for Part (e) of functional requirements
        #       --> An option to show class count (number of classes represented by each bar in graph)
 


    """
    TODO: need to figure out what the UI needs returned in order to make a graph
    idea:
        class GraphInformation:
        --> class object to be made in the UI.py file (and imported into this file)
        --> GraphInformation object returned to UI when a query is satified by handler
        --> then UI.py can take graph information and display 
    """


if __name__ == "__main__":
    
    # Running example queries of each type
    # class search for "CIS 122" professors, with easyA and all_instructors enabled
    # input_query = Query(0, True, True, class_level=122, dept="CIS")
    
    # CIS department search for professors, with easyA and all_instructors enabled
    # input_query = Query(1, True, True, dept="CIS")

    # CIS department search for all professors of 400 level, with easyA and all_instructors enabled
    # input_query = Query(2, True, True, class_level=400, dept="CIS")

    # CIS department search for all 600 level classes, with easyA and all_instructors enabled
    input_query = Query(3, True, True, class_level=600, dept="CIS")
    
    res = input_query.database_search()
    print(res)

