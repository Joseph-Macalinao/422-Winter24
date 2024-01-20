"""
Module containing all database searching functions.
Primarily used by the Query Handler.
"""

# define functions required to search the database, including the following:

def class_search(crn:int, all_instructors, easy_a):
    """
    Given a crn, search for all professors who have taught that class.
    """
    pass

def department_search(dept:str, all_instructors, easy_a):
    """
    Given a department, search for information regarding all professors
    of that specific department.
    """
    pass

def level_department_search(data:list, all_instructors, easy_a):
    """
    Given a level and department (packed into data[]), search for all professors teaching at that class level.
    """
    pass

def class_level_search(data:list, all_instructors, easy_a):
    """
    Given a level and department (packed into data[]), search for all classes of that 
    particular level in that department.
    """
    pass