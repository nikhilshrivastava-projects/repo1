from locale import DAY_1
from mimetypes import init
import os
import sys
from time import sleep
from selenium import webdriver
from common_utilities.utilities import utilities as ut
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest

class Demo (unittest.TestCase):

    @classmethod
    def setup(self):
        try:
            PATH = "/Users/nikhil/nikhil_workspace/Selenium_Python_Framework/chromedriver/chromedriver"
            driver = webdriver.Chrome(PATH)
            # command executed in terminal to give access permission to chromedriver in mac os
            # sudo xattr -d com.apple.quarantine /Users/nikhil/nikhil_workspace/Selenium_Python_Framework/chromedriver/chromedriver

            driver = webdriver.Chrome(PATH)
            # driver.get("https://www.techwithtim.net")
            driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
            driver.maximize_window()
            print('Title: ',driver.title)
            search = driver.find_element_by_name('firstname')
            explicit_wait(driver, search)
            search.send_keys('Nikhil')
            # explicit_wait(driver)
            # print(driver.page_source)
        finally:
            sleep(10)
            # teardown(driver)

    @classmethod
    def teardown(driver):
        driver.quit()

def explicit_wait(driver, element):
    print('Explicit wait for 10 seconds for element: ', element)
    element = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located((By.NAME,'firstname')))

if __name__ == "__main__":
    d1 = Demo()
    d1.setup()