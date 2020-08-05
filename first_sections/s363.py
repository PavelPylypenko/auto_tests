import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(7)
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1 '])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    answer = str(math.log(int(time.time())))
    textarea = browser.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys(answer)
    button = browser.find_element_by_xpath("//button[text()= 'Submit']")
    button.click()
    pre = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    assert pre == 'Correct!', f"pre is different: {pre}"
