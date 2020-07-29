import math
import os

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
# browser.implicitly_wait(3)
try:
    browser.get(link)
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element_by_id("book").click()
    val = browser.find_element(By.ID, 'input_value').text
    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(str(math.log(abs(12 * math.sin(int(val))))))
    button = browser.find_element_by_xpath("//button[text()= 'Submit']")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
