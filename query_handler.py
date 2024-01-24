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
        
        meta_data (list[mixed]): Data to satisfy actual query, such as CRN or class level
        
        all_instructors (bool): Boolean identifying "all instructors" vs "regular faculty"
        easy_a (bool): Boolean identifying % of A's vs % of D/F's

    Returns:
        something 
    """
    def __init__(self, req, md, instr, easyA):
        self.main_request = req
        self.meta_data = md   # list of 1+ elements
        self.all_instructors = instr
        self.easy_a = easyA


    def database_search(self):
        """
        High level function: 
        Calls specific database searches (as defined in database.py)
        
        --> is this bad coding??? feels kinda weird idk
        """

        if self.main_request == 0:
            class_search(self.meta_data, self.all_instructors, self.easy_a) 

        # since this query only requires one bit of information (department), we can explicitly pass [0]
        elif self.main_request == 1:
            department_search(self.meta_data[0], self.all_instructors, self.easy_a) 

        elif self.main_request == 2:
            level_department_search(self.meta_data, self.all_instructors, self.easy_a) 

        elif self.main_request == 3:
            class_level_search(self.meta_data, self.all_instructors, self.easy_a) 

        else:
            # error handling lol
            pass


    """
    TODO: need to figure out what the UI needs returned in order to make a graph
    idea:
        class GraphInformation:
        --> class object to be made in the UI.py file (and imported into this file)
        --> GraphInformation object returned to UI when a query is satified by handler
        --> then UI.py can take graph information and display 
    """