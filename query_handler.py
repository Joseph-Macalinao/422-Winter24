"""
Module containing functions for handling and resolving queries.
Primarily used by the standard UI.
"""

class Query:
    """
    Query objects contain all specifications required to fully identify a query.

    Parameters:
        main_request: Enumerated identifier for (0) specific class, (1) specific department, 
                                            (2) level in department, and (3) all classes of given level                                  
        
        meta_data: Data to satisfy actual query, such as actual CRN or class level
                    (may need to extend datatype)
        
        all_instructors: Boolean identifying "all instructors" vs "regular faculty"
        easy_a: Boolean identifying % of A's vs % of D/F's

    Returns:
        something 
    """
    def __init__(self, req, md, instr, easyA):
        self.main_request = req
        self.meta_data = md
        self.all_instructors = instr
        self.easy_a = easyA