from bs4 import BeautifulSoup
from selenium import webdriver
import json

courseDict = {}
subjectDict = {}

# Loads web scraper to get HTML code
chromedriver = "C:\\Users\\GGPC\\OneDrive\\Documents\\pythonew\\chromedriver"
driver = webdriver.Chrome(chromedriver)
url = "https://service-web.wgtn.ac.nz/dotnet2/catprint.aspx?d=all&t=u2020"
driver.get(url)
htmlElement = driver.find_elements_by_tag_name("p")
currView = None

for course in htmlElement:

    classAttribute = course.get_attribute("class")
    currView = course.text

    # Checks what type of paragraph the data is stored in
    if classAttribute == "courseid":

        # Exampe of currView: STAT 193 - Statistics in Practice
        fourletterCode = currView[:4]
        threenumberCode = currView[5:8]
        courseCodeID = currView[:8]
        courseName = currView[11:]

        # Stores items in subjectDict as i.e {"STAT" : [193,292,293,335]}
        if fourletterCode not in subjectDict:
            subjectDict[fourletterCode] = set()

        subjectDict[fourletterCode].add(threenumberCode)

        # Course object (to be stored in .json file)
        courseDict[courseCodeID] = {"id": courseCodeID,
                                    "name": courseName,
                                    "isOffered": True,
                                    "timetable": [],
                                    "courseDesc": "",
                                    "limitedEntry": False,
                                    "pointPre": ""
                                    }

    elif classAttribute == "notoffered":
        courseDict[courseCodeID]["isOffered"] = False
    elif classAttribute == "timetable":
        courseDict[courseCodeID]["timetable"].append(currView)
    elif classAttribute == "coursepoints":
        courseDict[courseCodeID]["pointPre"] = currView
    elif classAttribute == "subjectsbody":
        courseDict[courseCodeID]["courseDesc"] = currView
    elif classAttribute == "coursenote":
        courseDict[courseCodeID]["limitedEntry"] = True

# JSON can't store set, converts to list
for subject in subjectDict:
    subjectDict[subject] = sorted(list(subjectDict[subject]))

with open("courseList.json", "w") as file:
    json.dump(courseDict, file)

with open("courseType.json", "w") as file:
    json.dump(subjectDict, file)

driver.quit()
