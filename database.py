"""
Module containing all database searching functions.
Primarily used by the Query Handler.
"""

import json
with open('result.json') as data:
    initial_database = data.read()
    data_bank = json.loads(initial_database)

# define functions required to search the database, including the following:

def class_search(class_num, dept, easy_a):
    """
    Given a class number and a department, search for all professors who have taught that class.
    """
    matching_professors = []

    for department_entry in easy_a["departments"]:
        for department_code, department_data in department_entry.items():
            if department_code == dept: 
                for class_entry in department_data["classes"]:
                    for class_code, class_data in class_entry.items():
                        if class_code == class_num:
                            for entry in class_data:
                                if entry["instructor"] in matching_professors:
                                    pass
                                else: 
                                    matching_professors.append(entry["instructor"])
    return matching_professors

def department_search(dept, easy_a):
    """
    Given a department, search for information regarding all professors
    of that specific department.
    """
    matching_professors = []
    for department_entry in easy_a["departments"]:
        for department_code, department_data in department_entry.items():
            if department_code == dept: 
                for class_entry in department_data["classes"]:
                    for class_code, class_data in class_entry.items():
                        for entry in class_data:
                            if entry["instructor"] in matching_professors:
                                    pass
                            else: 
                                matching_professors.append(entry["instructor"])
    return matching_professors


def level_department_search(class_level, dept, easy_a):
    """
    Given a class level and department, search for all professors teaching at that class level.
    """
    matching_professors = []
    classlevel = dept + str(class_level)
    classmax = dept + str(class_level + 100)
    for department_entry in easy_a["departments"]:
        for department_code, department_data in department_entry.items():
            if department_code == dept:
                for class_entry in department_data["classes"]:
                    for class_code, class_data in class_entry.items():
                        if class_code > classlevel and class_code < classmax:
                            for entry in class_data:
                                if entry["instructor"] in matching_professors:
                                        pass
                                else: 
                                    matching_professors.append(entry["instructor"])
                                    
    return matching_professors


def class_level_search(class_level, dept, easy_a):
    """
    Given a class level and department, search for all classes of that 
    particular level in that department.
    """
    matching_classes = []
    classlevel = dept + str(class_level)
    classmax = dept + str(class_level + 100)
    for department_entry in easy_a["departments"]:
        for department_code, department_data in department_entry.items():
            if department_code == dept: 
                for class_entry in department_data["classes"]:
                    for class_code, class_data in class_entry.items():
                        if class_code > classlevel and class_code < classmax:
                            matching_classes.append(class_data)

    return matching_classes