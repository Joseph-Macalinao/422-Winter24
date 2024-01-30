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
    Given a class number and a department, search for (a % or d/f %) of all professors who have taught that class.
    """
    # classes (a list w/ dicts for each class), Regular_Faculty (a list of faculty members)
    
    returning_data = {}  # key = professor, val = [percentage, num_entries]  (since tuples are immutable)
    
    class_to_find = dept + str(class_num)  # e.g., "CIS110"
    department_info_dict = data_bank[dept]  # attempt to load database entry for given dept

    if department_info_dict:  # department exists
        class_list = department_info_dict["classes"]  # list of classes (ofc)
        for class_obj in class_list:
            
            # search for class_obj that contains class_title as a key 
            if class_to_find in class_obj:  # MATCH --> pull relevant data from each dict
                for class_instance in class_obj[class_to_find]:
                    instructor_name = class_instance["instructor"]
                    
                    if instructor_name not in returning_data:  # first_time entry --> make dict entry
                        returning_data[instructor_name] = [0.0,0] 

                    # gather running sum of desired percentage and frequency (for final avg)
                    if easy_a:  
                        returning_data[instructor_name][1] += 1
                        returning_data[instructor_name][0] += float(class_instance["aprec"])
                    else:
                        returning_data[instructor_name][1] += 1
                        returning_data[instructor_name][0] += float(class_instance["dprec"])
                        returning_data[instructor_name][0] += float(class_instance["fprec"])
            else:
                # print(f"Invalid class search: {class_to_find} not found")
                pass
    else:
        # print(f"Invalid department search: {dept} not found")
        pass

    if returning_data:  # if returning data has entries, we need to find avg
        for professor in returning_data:
            curr_dict = returning_data[professor]
            if easy_a:
                curr_dict[0] = round(curr_dict[0] / curr_dict[1], 2)
            else:  # twice as many data points as classes --> divide by 2* class_num
                curr_dict[0] = round(curr_dict[0] / (curr_dict[1]) * 2, 2)
    return returning_data 

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


def print_class_info():
    # debugging function just to confirm data to the given list
    # too lazy to write out rn 
    pass


if __name__ == "__main__":
    # query testing (probably remove for final product)
    easy_a_res = class_search(122, "CIS", True)
    pass_res = class_search(122, "CIS", False)
    
    # goal --> get res to print relevant data to send back to the query handler
    print(easy_a_res)
    print(pass_res)
