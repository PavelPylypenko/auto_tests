import math

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
try:
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    y = str(math.log(abs(12*math.sin(int(x)))))
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    rb = browser.find_element(By.ID, 'robotsRule')
    rb.click()
    button = browser.find_element_by_xpath("//button[text()= 'Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
