from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def is_basket_empty_text(self):
        assert self.try_find_element(*BasketPageLocators.BASKET_EMPTY).text, "There's no 'Your basket is empty.'"

    def is_not_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), 'Basket not empty'