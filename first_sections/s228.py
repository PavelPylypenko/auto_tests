import math
import os

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('1')
    browser.find_element(By.NAME, 'lastname').send_keys('1')
    browser.find_element(By.NAME, 'email').send_keys('1')
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lorem.txt')
    browser.find_element(By.ID, 'file').send_keys(path)
    button = browser.find_element_by_xpath("//button[text()= 'Submit']")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
