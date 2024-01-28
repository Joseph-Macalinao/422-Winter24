# for processing the js file (and csv?)
import json
import csv

# function to call scraper

# function to create a json file from the .csv and .js files

initial_data_bank = "gradedata.js"
data_bank = "modified_gradedata.js"
end_marker = "};\n"
web_data = "export_data.csv"
primary_dict1 = {}
secondary_dict2 = {"departments": []}
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
    
with open (initial_data_bank, "r") as input_file:
    content_line = []
    for line in input_file:
        if line == end_marker:
            content_line.append("}")
            break
        content_line.append(line)

with open(data_bank, "w") as modified_file:
    modified_file.writelines(content_line)

with open(data_bank) as fh:
    primary_dict1 = file_open(fh)

filename = open(web_data)
file = csv.DictReader(filename)
regular_faculty = []
for col in file:
    regular_faculty.append(col["Faculty Member"])

#print(names)
department_key = ''
for coursecode, course_data in primary_dict1.items():

    department = coursecode.split()[0]
    #print(course_data)
    #print(course_data[0]["instructor"])
    department_code = ''
    for char in department:
        if char.isdigit():
            break
        department_code += char

        department_entry = next(
            (dept for dept in secondary_dict2["departments"] if dept.get(department_code)),
            None
        )

    if department_entry is None:
        department_key = department_code
        department_entry = {
            department_key: {
                "classes": [],
                "Regular_Faculty": []
            }
        }
        secondary_dict2["departments"].append(department_entry)

    # Append class details to the classes list
    department_entry[department_key]["classes"].append({coursecode: course_data})

    #secondary_dict2[department_code].append({coursecode: course_data})
    for courses in course_data:
        JS_name = courses["instructor"]
        new_name = rearrange_name(JS_name)
        if new_name in regular_faculty and new_name not in department_entry[department_key]["Regular_Faculty"]:
            department_entry[department_key]["Regular_Faculty"].append(new_name)

with open('result.json', 'w') as fp:
    json.dump(secondary_dict2, fp, indent= 1)
    




