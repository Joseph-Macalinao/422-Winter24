from bs4 import BeautifulSoup
import requests, csv, time

# all natural science urls
urls =['https://web.archive.org/web/20141107201402/http://catalog.uoregon.edu/arts_sciences/biology/',
        'https://web.archive.org/web/20141107201414/http://catalog.uoregon.edu/arts_sciences/chemistry/',
        'https://web.archive.org/web/20141107201434/http://catalog.uoregon.edu/arts_sciences/computerandinfoscience/',
        'https://web.archive.org/web/20141107201454/http://catalog.uoregon.edu/arts_sciences/environmentalstudies/',
        'https://web.archive.org/web/20141107201647/http://catalog.uoregon.edu/arts_sciences/humanphysiology/',
        'https://web.archive.org/web/20141014075611/http://catalog.uoregon.edu/arts_sciences/geography/',
        'https://web.archive.org/web/20141107201628/http://catalog.uoregon.edu/arts_sciences/geologicalsciences/',
        'https://web.archive.org/web/20141010081859/http://catalog.uoregon.edu/arts_sciences/mathematics/',
        'https://web.archive.org/web/20141107202116/http://catalog.uoregon.edu/arts_sciences/mathematicsandcomputerscience/',
        'https://web.archive.org/web/20141107202132/http://catalog.uoregon.edu/arts_sciences/neuroscience/',
        'https://web.archive.org/web/20141101180027/http://catalog.uoregon.edu/arts_sciences/physics/',
        'https://web.archive.org/web/20141101200122/http://catalog.uoregon.edu/arts_sciences/psychology/',
        'https://web.archive.org/web/20141107202247/http://catalog.uoregon.edu/arts_sciences/statistics/']

def scrape_export_data(url, names_set):
    """ scrape_export_data(url): input is string (url)
    returns void but creates a .csv file called "export_data.csv"
    """

    website = url
    result = requests.get(website, verify=True) # make HTTP get request on url
    
    content = result.text # get text from HTTP request
    soup = BeautifulSoup(content, 'lxml') # make a BeautifulSoup object out of pulled text

    box = soup.find('div', {'id': 'facultytextcontainer'}) #identify {id: facultytextcontainer} sections in the HTML
    
    if box: # if section found, access the data
        faculty_info = [] # create empty list for faculty info
        major = soup.find('div', attrs={'id': 'breadcrumb'}).find('span', {'class': 'active'}).get_text(strip=True) #find the specific major being listed
        print(major) # list majors
        person = box.find('p') # check for <p> class 

        if person: # catch a specific case of HTML faculty not listed in facultylist:
            person_text = person.get_text(strip=True) # get HTML text of faculty and strip whitespace

            if ',' in person_text: # check for "," separator of faculty name and role

                name, department1 = person.get_text(strip = True).split(",",1)# identify person name and faculty role, split into 2 variables
                department = department1.split('.')[0] + ' ' # remove excessive text of department

                if name not in names_set:  # Check if name is not already in the set of unique names

                    names_set.add(name)  # Add name to the set
                    faculty_info.append((name, major, department)) # add name, major, department to faculty_info list

        for faculty in box.find_all('p', {'class': 'facultylist' }): # check through every instance of <p> <class: facultylist>

            faculty_text = faculty.get_text(strip=True) # get HTML text of faculty and strip whitespace
 
            if ',' in faculty_text: #check for comma separating faculty name and role

                name, department1 = faculty.get_text(strip = True).split(",", 1) ##identify person name and faculty role, split into two variables
                department = department1.split('.')[0] + ' ' #remove unnecessary info from department
                
                if name not in names_set: #if name not in unique set, continue - if in unique set, do not add to list

                    names_set.add(name) #add name to unique set
                    faculty_info.append((name, major, department)) #add name, major, department to faculty_info list

        if faculty_info: #if faculty_info list exists for this page
                
                with open('export_data.csv', 'a', newline='', encoding = 'utf-8') as file: #open export_data.csv file

                    writer = csv.writer(file) #write to file

                    if file.tell() == 0: #check if file is empty. If empty, add headers
                        headers = ['Faculty Member', 'Department', 'Role'] #create headers
                        writer.writerow(headers) #write headers onto file

                    for name, department, major in faculty_info: #cycle through each person and their information in faculty info

                        nums = [name, department, major] #put information into list
                        writer.writerow(nums) #write list into csv file, appending each data pt into their category

                    file.close() #close file

                return
        else:
            print("No data") #if there is no faculty to append, print "no data"
            return

def data_scraper():
    '''Uses built in list of urls. Scrapes each url for that specific major, all necessary faculty names, and their role in the department. Writes that information into an export_data.csv file'''
    unique_names_set = set() #Initialize an empty list of names to catch reptitions
    filename = 'export_data.csv'
    f = open(filename, "w+")
    f.close()
    for url in urls:
        scrape_export_data(url, unique_names_set)
        time.sleep(9)

data_scraper()