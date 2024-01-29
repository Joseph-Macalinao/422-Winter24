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
    def __init__(self, req, instructor, easyA, class_level=0, dept=""):
        self.main_request = req
        self.class_input = class_level
        self.dept = dept
        self.all_instructors = instructor
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
            # error handling lol
            pass

        # TODO: define result in a meaningful way to be used for graphing.
 


    """
    TODO: need to figure out what the UI needs returned in order to make a graph
    idea:
        class GraphInformation:
        --> class object to be made in the UI.py file (and imported into this file)
        --> GraphInformation object returned to UI when a query is satified by handler
        --> then UI.py can take graph information and display 
    """