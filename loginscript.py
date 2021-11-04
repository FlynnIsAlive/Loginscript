import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.safari.options import Options
import time
import datetime
import os
import random
import string

############
#test
############
def random_char(char_num):
    return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Safari(options=options)
driver.get("https://de.wikipedia.org/w/index.php?title=Spezial:Anmelden")

for x in range(2):
    username_element = driver.find_element(By.ID, "wpName1")
    password_element = driver.find_element(By.NAME, "wpPassword")
    username_element.send_keys(random_char(7)+"@gmail.com")
    password_element.send_keys("123")
    checkbox = driver.find_element(By.ID, "wpRemember")
    checkbox.click()
    time.sleep(2)
    signInButton = driver.find_element(By.ID, "wpLoginAttempt")
    signInButton.click()
    time.sleep(3)