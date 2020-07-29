import math
import os

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
try:
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.window(browser.window_handles[-1])
    time.sleep(1)
    val = browser.find_element(By.ID, 'input_value').text
    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(str(math.log(abs(12 * math.sin(int(val))))))
    button = browser.find_element_by_xpath("//button[text()= 'Submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
