from selenium.webdriver.common.by import By


def test_button_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    element = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert element
