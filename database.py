"""
Module containing all database searching functions.
Primarily used by the Query Handler.
"""

import json
with open('result.json') as data:
    initial_database = data.read()
    data_bank = json.loads(initial_database)

# define functions required to search the database, including the following:

def class_search(class_num, dept, all_instructors, easy_a):
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
                    
                    if all_instructors == False:
                        # when all_instructors is False (regular faculty is toggled ON), filter out non-regular faculty
                        # split intructor name string so we can compare to the faculty list
                        name_list = instructor_name.split(",")  # separate last name from first+middle
                        first_middle = name_list[1].split(" ")  # separate first+middle with space

                        instructor_name = first_middle[1] + " " + name_list[0]  # first_middle[1] gets first name, name_list[0] gets last
                        if instructor_name not in department_info_dict["Regular_Faculty"]:
                            continue

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


def department_search(dept, all_instructors, easy_a):
    """
    Given a department, search for information regarding all professors
    of that specific department.
    """
    returning_data = {}  # key = professor, val = [percentage, num_entries]  (since tuples are immutable)
    department_info_dict = data_bank[dept]  # attempt to load database entry for given dept

    if department_info_dict:  # department exists
        class_list = department_info_dict["classes"]  # list of classes (ofc)
        for class_obj in class_list: 
            for class_data in class_obj.values():
                for class_instance in class_data:
                    instructor_name = class_instance["instructor"]
                    
                    if all_instructors == False:
                        # when all_instructors is False (regular faculty is toggled ON), filter out non-regular faculty
                        # split intructor name string so we can compare to the faculty list
                        name_list = instructor_name.split(",")  # separate last name from first+middle
                        first_middle = name_list[1].split(" ")  # separate first+middle with space

                        instructor_name = first_middle[1] + " " + name_list[0]  # first_middle[1] gets first name, name_list[0] gets last
                        if instructor_name not in department_info_dict["Regular_Faculty"]:
                            continue

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
    

def level_department_search(class_level, dept, all_instructors, easy_a):
    """
    Given a class level and department, search for all professors teaching at that class level.
    """
    returning_data = {}  # key = professor, val = [percentage, num_entries]  (since tuples are immutable)
    department_info_dict = data_bank[dept]  # attempt to load database entry for given dept

    class_max = dept + str(class_level + 100)
    class_level = dept + str(class_level)

    if department_info_dict:  # department exists
        class_list = department_info_dict["classes"]  # list of classes (ofc)
        for class_obj in class_list: 

            for class_code, class_data in class_obj.items():
                # for each class_code, determine if it's in correct range (i.e. 100~199)
                if class_code >= class_level and class_code < class_max:
                    for class_instance in class_data:
                        instructor_name = class_instance["instructor"]
                        
                        if all_instructors == False:
                            # when all_instructors is False (regular faculty is toggled ON), filter out non-regular faculty
                            # split intructor name string so we can compare to the faculty list
                            name_list = instructor_name.split(",")  # separate last name from first+middle
                            first_middle = name_list[1].split(" ")  # separate first+middle with space

                            instructor_name = first_middle[1] + " " + name_list[0]  # first_middle[1] gets first name, name_list[0] gets last
                            if instructor_name not in department_info_dict["Regular_Faculty"]:
                                continue
                        
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
                    # class is not in the correct level (i.e., not between 100~199)
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


def class_level_search(class_level, dept, all_instructors, easy_a):
    """
    Given a class level and department, search for all classes of that 
    particular level in that department.
    """

    returning_data = {}  # key = class name, val = [percentage, num_entries]  (since tuples are immutable)
    department_info_dict = data_bank[dept]  # attempt to load database entry for given dept

    class_max = dept + str(class_level + 100)
    class_level = dept + str(class_level)

    if department_info_dict:  # department exists
        class_list = department_info_dict["classes"]  # list of classes (ofc)
        for class_obj in class_list: 

            for class_code, class_data in class_obj.items():
                # for each class_code, determine if it's in correct range (i.e. 100~199)
                if class_code >= class_level and class_code < class_max:
                    for class_instance in class_data:
                        instructor_name = class_instance["instructor"]

                        if all_instructors == False:
                            # when all_instructors is False (regular faculty is toggled ON), filter out non-regular faculty
                            # split intructor name string so we can compare to the faculty list
                            name_list = instructor_name.split(",")  # separate last name from first+middle
                            first_middle = name_list[1].split(" ")  # separate first+middle with space

                            instructor_name = first_middle[1] + " " + name_list[0]  # first_middle[1] gets first name, name_list[0] gets last
                            if instructor_name not in department_info_dict["Regular_Faculty"]:
                                continue
                            
                        if class_code not in returning_data:  # first_time entry --> make dict entry
                            returning_data[class_code] = [0.0,0] 

                        # gather running sum of desired percentage and frequency (for final avg)
                        if easy_a:  
                            returning_data[class_code][1] += 1
                            returning_data[class_code][0] += float(class_instance["aprec"])
                        else:
                            returning_data[class_code][1] += 1
                            returning_data[class_code][0] += float(class_instance["dprec"])
                            returning_data[class_code][0] += float(class_instance["fprec"])
                    else:
                        # print(f"Invalid class search: {class_to_find} not found")
                        pass
                else:
                    # class is not in the correct level (i.e., not between 100~199)
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


if __name__ == "__main__":

    # query testing (probably remove for final product)
    # easy_a_res = class_search(122, "CIS", True, True)
    # pass_res = class_search(122, "CIS", True, False)
    
    # easy_a_res = department_search("CIS", True, True)
    # pass_res = department_search("CIS", True, False)
    
    # easy_a_res = level_department_search(600, "CIS", True, True)
    # pass_res = level_department_search(600, "CIS", True, False)
    
    easy_a_res = class_level_search(600, "CIS", True, True)
    pass_res = class_level_search(600, "CIS", True, False)
    # goal --> get res to print relevant data to send back to the query handler
    print(easy_a_res)
    print(pass_res)

    print(f"\n\n{len(easy_a_res)}")
