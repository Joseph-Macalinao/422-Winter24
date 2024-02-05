from bs4 import BeautifulSoup
import requests, csv, time

# all URLs from wayback machine archive of UO course catalog
urls =[ 'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/africanstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/anthropology/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/asianstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/canadianstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/cinemastudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/classics/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/comparativeliterature/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/creativewriting/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/eastasianlanguagesandlit/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/economics/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/english/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/ethnicstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/europeanstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/folklore/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/generalscience/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/generalsocialscience/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/germanandscandinavian/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/germanstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/history/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/humanities/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/humanphysiology/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/internationalstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/judaicstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/latinamericanstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/linguistics/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/medievalstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/nativeamerican/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/pacificislandstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/peacestudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/philosophy/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/politicalscience/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/religiousstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/romancelanguages/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/russianandeasteuropeanstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/scandinavianstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/sociology/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/southeastasianstudies/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/theaterarts/',
        'https://web.archive.org/web/20140901091007/http://catalog.uoregon.edu/arts_sciences/womensandgenderstudies/',
        'https://web.archive.org/web/20141107201402/http://catalog.uoregon.edu/arts_sciences/biology/',
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

def scrape_export_data(url, names_set, count):
    """ 
    scrape_export_data(url): input is string (url)
    returns void but creates a .csv file called "export_data.csv"

    - checks URL for key HTML tags, reading the faculty names from the tags if found
    - identifes 
    """

    website = url
    result = requests.get(website, verify=True) # make HTTP get request on url
    
    content = result.text # get text from HTTP request
    soup = BeautifulSoup(content, 'lxml') # make a BeautifulSoup object out of pulled text

    box = soup.find('div', {'id': 'facultytextcontainer'}) #identify {id: facultytextcontainer} sections in the HTML
    
    if box: # if section found, access the data

        faculty_info = [] # create empty list for faculty info
        major = soup.find('div', attrs={'id': 'breadcrumb'}).find('span', {'class': 'active'}).get_text(strip=True) #find the specific major being listed
               
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

                print("{}. {}".format(count, major)) # list majors

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

            major = soup.find('div', attrs={'id': 'breadcrumb'}).find('span', {'class': 'active'}).get_text(strip=True) #find the specific major being listed
            print("{}. {}: No data".format(count, major))  #if there is no faculty to append, print "no data"
            
            return
    else:
        major = soup.find('div', attrs={'id': 'breadcrumb'}).find('span', {'class': 'active'}).get_text(strip=True) #find the specific major being listed
        print("{}. {}: No data".format(count, major))  #if there is no faculty to append, print "no data"
            

def data_scraper():
    '''
    Uses built in list of urls. 
    Scrapes each url for that specific major, all necessary faculty names, and their role in the department. 
    Writes that information into an export_data.csv file
    '''
    unique_names_set = set() #Initialize an empty list of names to catch reptitions
    count = 0
    print("Starting the web scraper. The output will show which department's data has been collected and will print 'No data' if there was no information available.\n")
    time.sleep(3)
    print("The web scraper may take around 13 minutes to run in order to prevent the scraper from being flagged as a malicious attack on the website.\n")
    time.sleep(3)
    print("If the web scraper stops before 'Scraper has finished running.', please wait a few minutes and try again.\n")
    time.sleep(4)
    print("Departments Collected:")

    for url in urls:
        count = count + 1
        scrape_export_data(url, unique_names_set, count)
        time.sleep(9)
    
    print("Scraper has finished running.")

if __name__ == "__main__":
    data_scraper()