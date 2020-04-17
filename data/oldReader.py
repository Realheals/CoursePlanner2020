from bs4 import BeautifulSoup
from selenium import webdriver
import re

chromedriver = "C:\\Users\\GGPC\\OneDrive\\Documents\\pythonew\\chromedriver"
driver = webdriver.Chrome(chromedriver)

while True:
    courseToSearch = input("Enter in course code (STAT 193): ")

    if not re.fullmatch(r"[A-Z]{4}\s[0-9]{3}", courseToSearch):
        break

    subjectCode = courseToSearch[:4]
    courseNumber = courseToSearch[5:]

    url = f"https://www.wgtn.ac.nz/courses/{subjectCode}/{courseNumber}/2020/"
    driver.get(url)

    elem = driver.find_elements_by_css_selector('.course-id-block')

    if elem:
        toFormat = elem[0].text.split("\n")
        print(f"\n{toFormat[0]} - {toFormat[3]}\n\n{toFormat[4]}\n")
    else:
        print(f"\nSorry, {courseToSearch} does not exist\n")

driver.quit()
