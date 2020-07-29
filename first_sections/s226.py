import math

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    val = browser.find_element(By.ID, 'input_value').text
    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(str(math.log(abs(12 * math.sin(int(val))))))
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    rb = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", rb)
    rb.click()
    button = browser.find_element_by_xpath("//button[text()= 'Submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
