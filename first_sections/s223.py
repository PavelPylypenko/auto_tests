import math

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
try:
    browser.get(link)
    val1 = browser.find_element(By.ID, 'num1').text
    val2 = browser.find_element(By.ID, 'num2').text
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(int(val1) + int(val2)))
    button = browser.find_element_by_xpath("//button[text()= 'Submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
