from bs4 import BeautifulSoup
import requests
from mechanize import Browser
roll = raw_input()
password = raw_input()
br = Browser()

# Logging in the Moodle Page
page = br.open('https://courses.iitm.ac.in/login/index.php')
br.select_form(nr=0)
br.form["username"] = roll
br.form["password"] = password
br.submit()
print "Logged In"

# Going to the attendence page
resp = br.open('https://courses.iitm.ac.in/mod/questionnaire/complete.php?id=8133')
# Entered the attendence page
br.select_form(nr=0)
br.form['q799'] = ["y"]
br.submit()

#Attendence Marked