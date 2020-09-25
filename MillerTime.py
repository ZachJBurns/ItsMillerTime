import requests
import random
import json
import wget
import os
import pickle
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from azcaptchaapi import AZCaptchaApi

"""
Again use your own information here. No one deserves to be spammed with random information.
"""
API_KEY = ""
DOMAIN = "@randomdomain12312452.com"
ADDRESS = ""
CITY = ""
STATE = ""
ZIP = ""
PHONENUMBER = ["", "", ""] #EX ["xxx", "xxx", "xxx"] for (xxx) xxx-xxxx
SIZE = "" #EX LARGE
DOWNLOAD_DIR = "" #EX /Users/zachburns/Desktop/ItsMillerTime/captcha/
CHROMEDRIVER = "" #EX /Users/zachburns/Downloads/chromedriver

# Import name files
firstNames = json.loads(open("firstnames.json").read())
lastNames = json.loads(open("lastnames.json").read())

# Open stored data
try:
    f = open('data.pckl', 'rb')
    database = pickle.load(f)
    f.close()
except:
    db = {"Wins": 0,
        "Total Submissions": 0,
        "Total Captcha Failures": 0,
        "Total Wins":0
        }
    with open('data.pckl', 'wb') as file:
        pickle.dump(db, file)
    with open("data.pckl", "rb") as file:
        database = pickle.load(file)

def updateDatabase(obj):
    f = open('data.pckl', 'wb')
    pickle.dump(obj, f)
    f.close()

api = AZCaptchaApi(API_KEY)

chromedriver = CHROMEDRIVER
options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument('user-agent={userAgent}')
options.add_argument("--incognito")
browser = webdriver.Chrome(options=options, executable_path = chromedriver)

browser.get('https://digitalbeerpromo.com/IW4/MC4038/en-us/Enter')

month = browser.find_element_by_id("PL_AgeGate_Birthdate_month")
month.send_keys("April")
day = browser.find_element_by_id("PL_AgeGate_Birthdate_day")
day.send_keys("23")
year = browser.find_element_by_id("PL_AgeGate_Birthdate_year")
year.send_keys("1996")
browser.find_element_by_class_name("btn").click()

while True:
    FIRSTNAME = random.choice(firstNames)
    LASTNAME = random.choice(lastNames)
    EMAILADDRESS = FIRSTNAME + "." + LASTNAME + str(random.randint(100, 1000)) + DOMAIN

    browser.get('https://digitalbeerpromo.com/IW4/MC4038/en-us/Enter')

    element = WebDriverWait(browser, 10).until(lambda x: x.find_element_by_id("Email_Identifier"))
    email = browser.find_element_by_id("Email_Identifier")
    email.send_keys(EMAILADDRESS)

    browser.find_element_by_class_name("btn").click()

    element = WebDriverWait(browser, 10).until(lambda x: x.find_element_by_id("User_FirstName"))
    firstName = browser.find_element_by_id("User_FirstName")
    firstName.send_keys(FIRSTNAME)

    lastName = browser.find_element_by_id("User_LastName")
    lastName.send_keys(LASTNAME)

    gender = browser.find_element_by_id("User_Gender_Male")
    gender.click()

    address = browser.find_element_by_id("User_Address_Address1")
    address.send_keys(ADDRESS)

    aptNum = browser.find_element_by_id("User_Address_Address2")
    aptNum.send_keys(str(random.randint(1, 100000)))

    city = browser.find_element_by_id("User_Address_City")
    city.send_keys(CITY)

    state = browser.find_element_by_id("state")
    state.send_keys(STATE)

    zipCode = browser.find_element_by_id("User_Address_PostalCode")
    zipCode.send_keys(ZIP)

    areaCode = browser.find_element_by_id("PL_User_Phone_areacode")
    areaCode.send_keys(PHONENUMBER[0])
    areaCode2 = browser.find_element_by_id("PL_User_Phone_prefix")
    areaCode2.send_keys(PHONENUMBER[1])
    areaCode3 = browser.find_element_by_id("PL_User_Phone_suffix")
    areaCode3.send_keys(PHONENUMBER[2])

    size = browser.find_element_by_id("preference")
    size.send_keys(SIZE)

    rules = browser.find_element_by_id("User_AgreeToRules")
    rules.click()

    captcha = browser.find_element_by_id("Captcha_Value")
    captchaLink = browser.find_element_by_class_name("captcha_image").get_attribute("src")
    captchaImage = captchaLink.replace('?', '/')
    captchaImage = captchaImage.split('/')

    wget.download(captchaLink, out=DOWNLOAD_DIR+captchaImage[-2])

    with open(DOWNLOAD_DIR+captchaImage[-2], 'rb') as captcha_file:
        captchaKey = api.solve(captcha_file)

    answer = captchaKey.await_result().upper()
    captcha.send_keys(answer)
    captcha.send_keys(Keys.RETURN)

    while True:
        try:
                browser.find_element_by_class_name("validation-summary-errors")
                database["Captcha Failures"] += 1
                os.remove(DOWNLOAD_DIR+captchaImage[-2])
                captcha = browser.find_element_by_id("Captcha_Value")
                captchaLink = browser.find_element_by_class_name("captcha_image").get_attribute("src")
                captchaImage = captchaLink.replace('?', '/')
                captchaImage = captchaImage.split('/')
                wget.download(captchaLink, out=DOWNLOAD_DIR+captchaImage[-2])

                with open(DOWNLOAD_DIR+captchaImage[-2], 'rb') as captcha_file:
                    captchaKey = api.solve(captcha_file)

                answer = captchaKey.await_result().upper()
                captcha.send_keys(answer)
                captcha.send_keys(Keys.RETURN)
        except:
            break

    os.rename(DOWNLOAD_DIR+captchaImage[-2], DOWNLOAD_DIR+answer + ".png")
    element = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_class_name("text-color"))
    print()

    if "Sorry, you didn’t score any gear this time." not in browser.page_source:
            database['Wins'] += 1
    for i in range(2):
        if "Sorry, you didn’t score any gear this time." not in browser.page_source:
            database['Wins'] += 1
        enterAgain = browser.find_element_by_link_text("Enter Again")
        enterAgain.click()
        browser.implicitly_wait(3)

    database['Total Submissions'] += 1
    print("Total Submissions", database['Total Submissions'])
    print("Total Captcha Failures", database['Captcha Failures'])
    print("Total Wins", database['Wins'])
    updateDatabase(database)
