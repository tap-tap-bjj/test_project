from .pages.main_page import MainPage
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.go_to_login_page()

# def go_to_login_page(browser):
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()