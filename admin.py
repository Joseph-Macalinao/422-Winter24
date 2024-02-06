# for processing the js file (and csv?)
import json
import csv
import scraper as scrapermodule

initial_data = "gradedata.js"

# function to call scraper
def scraper():
    """
    No input / return but will produce "export_data.csv" file
    """
    scrapermodule.data_scraper()
    return

# function to create a json file from the .csv and .js files

def file_open(file):
    """
    Open original JavaScript file and read each line in as a JSON dictionary
    """
    primary_dict = {}
    for line in file:
        primary_dict = json.load(file)
    return primary_dict

def rearrange_name(name):
    """
    Input: str
    Rearrange names from "last name, first name" into "first name, last name"
    Include middle initials/names
    Returns: str
    """

    name_parts = name.split(", ") #split name by common

    if len(name_parts) == 2: #if no middle name, identify first and last
        last_name, first_name = name_parts
    else:
        # If there is no comma or more than one comma, handle it accordingly
        last_name = name_parts[-1]  # Last part is the last name
        first_name_parts = name_parts[:-1]  # The rest are the first name parts
        first_name = " ".join(first_name_parts)

    if len(first_name) > 1: #if both middle and first name given, take first name
        first_name = first_name.split()[0]

    # Rearrange and concatenate to get "first name last name"
    name = f"{first_name} {last_name}"

    return name
    

def modify_js_file(initial_data_bank):
    """
    input: string representing a .js file
    Goes through JavaScript file and copies each line
    Stops copying once a ";" is reached
    Pastes the copied lines onto a new file that can now be accessed using json.load()
    returns: string representing a .js file
    """

    end_marker = "};\n" #denotes end of file to be copied
    data_bank = "modified_gradedata.js" #where modified code will go

    with open (initial_data_bank, "r") as input_file: #modify the .js file to remove functions and c code
        content_line = []
        for line in input_file: #cycles through each line
            if line == end_marker: #check if the line contains the final semi-colon
                content_line.append("}") #remove end semi-colon
                break
            content_line.append(line) #if the line is not the final line, add it to list

    with open(data_bank, "w") as modified_file:
        modified_file.writelines(content_line) #add lines to new file (new .js file)

    return

def create_json_data(initial_data_bank):
    """
    input: string representing .js file 

    - Modifies a .js file and loads data from file into dictionary
    - Cycles through the dictionary to get department and department codes
    - Makes a new JSON file to hold formatted JS file data and Regular Faculty list for each department
    - Stores all classes from one department in their associated department key
    - Compares all faculty with scraped CSV file - if names match, name is appended to Regular Faculty for that department 
    - All data is moved into results.json <-- new database

    return
    """

    web_data = "export_data.csv" #CSV file
    primary_dict1 = {} #dict that will hold .js data
    department_database = {} #final dict format that will be dumped into JSON file
    
    print("Modifying inputted JavaScript file into ideal format.")
    modify_js_file(initial_data_bank) #modify .js data in json format

    data_bank = "modified_gradedata.js"

    with open(data_bank) as fh:
        primary_dict1 = file_open(fh) #open modified file .js into json format

    filename = open(web_data) #open CSV file
    file = csv.DictReader(filename) #read dict into CSV file

    regular_faculty = [] #empty list for regular faculty -> if none, stays empty
    for col in file:
        regular_faculty.append(col["Faculty Member"]) #add all faculty members from CSV to list 

    print("Compiling information from modified JavaScript into JSON file format.")
    for coursecode, course_data in primary_dict1.items():
        #loop runs for each coursecode and associated data
        department = coursecode.split()[0] #grab the coursecode

        department_code = ''
        for char in department: #identify department acornoym
            if char.isdigit(): #check if character is a number
                break
            department_code += char
        
        if department_code not in department_database: #check if department already in the database
            department_database[department_code] = {
                "classes": [], #add class list to department dictionary
                "Regular_Faculty": [] #add regular faculty list to dictionary
            }

        department_database[department_code]["classes"].append({coursecode:course_data}) #add all the courses of the same class

        for courses in course_data: #for each course of this specific class
            JS_name = courses["instructor"]
            new_name = rearrange_name(JS_name) #rearrange the name to match CSV file
            if new_name in regular_faculty and new_name not in department_database[department_code]["Regular_Faculty"]: #check if name matches CSV and isn't already in list 
                department_database[department_code]["Regular_Faculty"].append(new_name) #add faculty name to regular faculty

    print("Adding JSON data to 'result.json' file.")
    with open('result.json', 'w') as fp: #dump the JSON formatted dictionary into a JSON file
        json.dump(department_database, fp, indent= 1)
    print("The 'result.json' file is successfully built.")
    return

if __name__ == "__main__":
    #scraper() #run scraper
    create_json_data(initial_data) #create JSON database
    





