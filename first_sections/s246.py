import math
import os

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()
# browser.implicitly_wait(3)
try:
    browser.get(link)
    browser.find_element_by_id("button")

finally:
    time.sleep(2)
    browser.quit()
