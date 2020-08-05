import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class RegistrationTestCase(unittest.TestCase):

    def _execute(self, link):
        browser = webdriver.Chrome()
        try:
            browser.get(link)
            for element in ['first', 'second', 'third']:
                browser.find_element(By.CLASS_NAME,
                                     '{}:required'.format(element)
                                     ).send_keys('↓')
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)
            welcome_text = browser.find_element(By.TAG_NAME, "h1").text
            return welcome_text

        finally:
            time.sleep(1)
            browser.quit()

    def test_first_registration(self):
        """Populate only three fields with classes first, second, third
         to pass the course"""
        link1 = "http://suninjuly.github.io/registration1.html"
        actual_res = self._execute(link1)
        self.assertEqual("Congratulations! You have successfully registered!", actual_res)

    def test_second_registration(self):
        """Populate only three fields with classes first, second, third
         to pass the course"""
        link2 = "http://suninjuly.github.io/registration2.html"
        actual_res = self._execute(link2)
        self.assertEqual("Congratulations! You have successfully registered!", actual_res)


if __name__ == "__main__":
    unittest.main()
