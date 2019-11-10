import time
from selenium.common.exceptions import NoSuchElementException

def test_button_is_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    except NoSuchElementException:
        assert False, "button is not exist"

    time.sleep(30)