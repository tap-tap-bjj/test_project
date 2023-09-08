import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_basket_assert(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button, 'No basket button'