
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
import json
import time
import sys

options = Options()
options.headless = True
driver = webdriver.Firefox(options = options , executable_path='/root/firefox/geckodriver')
print("please enter the URL address")
url = str(sys.argv[0])
driver.implicitly_wait(30)
driver.get(url)
email = driver.find_element_by_id('identifierId')
email.click()
print("please enter Google Account")
email.send_keys("jackjie330@gmail.com")
email.send_keys(Keys.ENTER)
time.sleep(10)
passwd = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
passwd.click()
print("please enter passwd")
passwd.send_keys("Google3366662")
passwd.send_keys(Keys.ENTER)
time.sleep(10)
driver.save_screenshot("screenshot.png")

while True:
    time.sleep(60)
    driver.save_screenshot("screenshot.png")
    driver.get(url)


