#!/usr/bin/env python
import getpass
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()# Enter the Driver path inside the paranthesis

#browser = webdriver.Chrome('Chrome_Driver_Path') for chrome browser 
#You may need to export the web driver path As  'export PATH=$PATH:/home/user/Desktop/Prahasanam-Etlab-Survey-Automation/Autoscript' on terminal

browser.implicitly_wait(30)#initiating Wait() function for browser to load.

browser.get('https://www.stthomas.etlab.in/survey/user/answer/26')
#Enter the full path of your college ETLAB website Survey portal link ,ie the link of the Page that you are getting after pressing the button 'Do the Survey'. 
#Or Update the last number in the link with 1 (Eg :'https://www.stthomas.etlab.in/survey/user/answer/25' then change it to 'https://www.stthomas.etlab.in/survey/user/answer/26' )

user = browser.find_element_by_id('LoginForm_username')
pswd = browser.find_element_by_id('LoginForm_password')

#Enter the Username and Password through Terminal.

UserName = input("\nEnter User Name : ")
PassWord = getpass.getpass(prompt="\nEnter the Password : ", stream=None)
user.send_keys(UserName)
pswd.send_keys(PassWord)
pswd.send_keys(Keys.ENTER)

#x is the No. of subjects that are present on the Survey portal.
x=15

# The Function surveyForm() Select the each subjects in Survey page, Select the First Option and Submit it.Here 'm' is the name for each subject in HTML source

def surveyForm(m) :

    y = browser.find_element_by_name(m)
    y.click()
    a = browser.find_element_by_xpath("//input[@value='355']")
    a.click()
    b = browser.find_element_by_xpath("//input[@value='360']")
    b.click()
    c = browser.find_element_by_xpath("//input[@value='365']")
    c.click()
    d = browser.find_element_by_xpath("//input[@value='370']")
    d.click()
    e = browser.find_element_by_xpath("//input[@value='374']")
    e.click()
    f = browser.find_element_by_xpath("//input[@value='377']")
    f.click()
    g = browser.find_element_by_xpath("//input[@value='381']")
    g.click()
    h = browser.find_element_by_xpath("//input[@value='384']")
    h.click()
    j = browser.find_element_by_xpath("//input[@value='388']")
    j.click()
    z = browser.find_element_by_xpath("//input[@value='392']")
    z.click()
    w = browser.find_element_by_xpath("//input[@value='396']")
    w.click()
    l = browser.find_element_by_name('yt0')
    l.click()

for i in range(0,x+1):

    m = 'yt'+str(i)
    surveyForm(m)
