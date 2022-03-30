from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl
from random import randint
import os 

username=os.environ.get("USERNAME")

password=os.environ.get("PASSWORD")

sapurl=os.environ.get("SAP")

x = randint(1,600)
sl(x)

driver = webdriver.Chrome()

driver.get(sapurl)
logon_field = driver.find_element_by_id("logonuidfield")
logon_field.send_keys(username)
pass_field = driver.find_element_by_id("logonpassfield")
pass_field.send_keys(password)
logon_button = driver.find_element_by_name("uidPasswordLogon")
logon_button.click()

driver.implicitly_wait(30)

att_click = driver.find_element_by_css_selector("#__tile3")
att_click.send_keys(Keys.SPACE)


att_click = driver.find_element_by_css_selector("#__tile20")

att_click.click()
sl(15)
driver.quit()

