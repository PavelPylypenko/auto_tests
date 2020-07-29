import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_required_fields(link: str):
    """Populate all required fields to pass registration"""
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        elements = browser.find_elements(By.CSS_SELECTOR, 'input:required')
        for element in elements:
            element.send_keys("↑")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(2)
        browser.quit()


def test_special_fields(link: str):
    """Populate only three fields with classes first, second, third
     to pass the course"""
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        for element in ['first', 'second', 'third']:
            browser.find_element(By.CLASS_NAME, '{}:required'.format(element)
                                 ).send_keys('↓')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        time.sleep(1)
        browser.quit()


if __name__ == "__main__":
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    test_special_fields(link1)
    test_special_fields(link2)
