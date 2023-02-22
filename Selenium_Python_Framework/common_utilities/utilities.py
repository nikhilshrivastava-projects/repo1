from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class utilities:
    def explicit_wait(driver, element):
        print('Explicit wait for 10 seconds for element : ', element)
        try:
            element = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located(By.NAME,'firstname'))
        finally:
            driver.quit()