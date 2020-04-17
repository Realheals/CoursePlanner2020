import json
import textwrap
import re

with open('courseList.json') as f:
    courseList = json.load(f)

with open('courseType.json') as f:
    subjectList = json.load(f)


def printFullCourseInfo(courseID):
    courseObj = courseList[courseID]
    soFar = f"\n{courseID} - {courseObj['name']}\n"
    triList = [stream[0] for stream in courseObj['timetable']]

    # Need to add in for 1+2/3 and 1+2+3/3, 2+3/3, 3+1/3
    if not courseObj['isOffered']:
        soFar += "Not Offered in 2020"
    elif len(triList) == 1:
        soFar += "Trimester "
    else:
        soFar += "Trimesters "
    soFar += ", ".join(triList) + "\n"

    pointsObj = courseObj['pointPre'].split("•")
    points = pointsObj[0]

    wrappedText = textwrap.wrap(courseObj['courseDesc'], width=70)
    descriptionText = "\n".join(wrappedText)

    soFar += f"{points}\n\n{descriptionText}\n"

    # Checks for pre-reqs or restrictions
    if len(pointsObj) > 1:
        pointsObj = pointsObj[1].replace(" (P)", "Pre-reqs")
        pointsObj = pointsObj.replace(" (X)", "Restrictions")

        for preReqRestriction in pointsObj.split(";"):
            soFar += f"\n{preReqRestriction}"

    if courseObj['limitedEntry']:
        soFar += f"\nLimited Entry"

    soFar += "\n"

    return soFar


def sepLine():
    return "-" * 70


def courseListFromCode(code):
    string = f"\nALL {code} COURSES\n\n"

    for num in subjectList[code]:
        course = courseList[f"{code} {num}"]
        string += f"{course['id']} -  {course['name']}\n"

    return string


def courseListFromCodeLevel(code, level):
    string = f"\n{level} LEVEL {code} COURSES\n\n"

    for num in subjectList[code]:
        if num[0] == str(level)[0]:
            course = courseList[f"{code} {num}"]
            string += f"{course['id']} -  {course['name']}\n"

    return string

while True:
    print(sepLine())
    userInput = input("TYPE YOUR INPUT: ")
    print(sepLine())

    validCourseCode = re.fullmatch(r"[A-Z]{4}\s[1-4]([1-9][0-9]|[0-9][1-9])",
                                   userInput) is not None
    validLevelCode = re.fullmatch(r"[A-Z]{4}\s[1-4][0]{2}",
                                  userInput) is not None
    validSubjectCode = re.fullmatch(r"[A-Z]{4}", userInput) is not None

    if validCourseCode and userInput in courseList:
        print(printFullCourseInfo(userInput))
    # Needs exception for ENGR SWEN COMP NWEN CYBR
    elif validLevelCode and userInput[:4] in subjectList:
        subject, code = userInput.split(" ")
        print(courseListFromCodeLevel(subject, code))
    elif validSubjectCode and userInput in subjectList:
        print(courseListFromCode(userInput))
    elif userInput == "Finished":
        break
    else:
        print("\nInvalid input - try again\n")
