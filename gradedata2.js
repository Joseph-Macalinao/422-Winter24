# for processing the js file (and csv?)
import json
import csv
import scraper as scrapermodule

# function to call scraper
def scraper():
    scrapermodule.data_scraper()

# function to create a json file from the .csv and .js files

initial_data_bank = "gradedata.js"
data_bank = "modified_gradedata.js"
end_marker = "};\n"
web_data = "export_data.csv"
primary_dict1 = {}
department_database = {}
comparison_list = []

def file_open(file):
    primary_dict = {}
    for line in file:
        primary_dict = json.load(file)
    return primary_dict

def rearrange_name(name):
    # Split the name into last name and first name
    name_parts = name.split(", ")

    if len(name_parts) == 2:
        last_name, first_name = name_parts
    else:
        # If there is no comma or more than one comma, handle it accordingly
        last_name = name_parts[-1]  # Last part is the last name
        first_name_parts = name_parts[:-1]  # The rest are the first name parts
        first_name = " ".join(first_name_parts)
    if len(first_name) > 1:
        first_name = first_name.split()[0]

    # Rearrange and concatenate to get "first name last name"
    name = f"{first_name} {last_name}"

    return name
    
with open (initial_data_bank, "r") as input_file: #modify the .js file to remove functions and c code
    content_line = []
    for line in input_file:
        if line == end_marker:
            content_line.append("}") #remove end semi-colon
            break
        content_line.append(line)

with open(data_bank, "w") as modified_file:
    modified_file.writelines(content_line) #add lines to new file (new .js file)

with open(data_bank) as fh:
    primary_dict1 = file_open(fh)

filename = open(web_data)
file = csv.DictReader(filename) #read dict of filename
regular_faculty = []
for col in file:
    regular_faculty.append(col["Faculty Member"]) #add faculty members to regular list 

department_key = ''
for coursecode, course_data in primary_dict1.items():

    department = coursecode.split()[0]

    department_code = ''
    for char in department:
        if char.isdigit():
            break
        department_code += char
        
        print(department_code)
    if department_code not in department_database:
        department_database[department_code] = {
            "classes": [],
            "Regular_Faculty": []
        }

    department_database[department_code]["classes"].append({coursecode:course_data})

    for courses in course_data:
        JS_name = courses["instructor"]
        new_name = rearrange_name(JS_name)
        if new_name in regular_faculty and new_name not in department_database[department_code]["Regular_Faculty"]:
            department_database[department_code]["Regular_Faculty"].append(new_name)

with open('result.json', 'w') as fp:
    json.dump(department_database, fp, indent= 1)
    





