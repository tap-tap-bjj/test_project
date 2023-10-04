from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input#id_registration-email')
    LOGIN_PASWORD1 =(By.CSS_SELECTOR, 'input#id_registration-password1')
    LOGIN_PASWORD2 = (By.CSS_SELECTOR, 'input#id_registration-password2')
    REG_BUTTON = (By.NAME, 'registration_submit')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages strong')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, '.basket-items')
    GO_TO_BASKET = (By.CSS_SELECTOR, '.basket-mini .btn-group a.btn.btn-default')
