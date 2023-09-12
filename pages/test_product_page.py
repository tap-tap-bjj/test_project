from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def item_should_be_in_basket(self):
        self.should_be_button_basket()
        self.element_click(*ProductPageLocators.BASKET_BUTTON)
        self.solve_quiz_and_get_code()
        self.right_item_in_basket()
        self.right_price_in_basket()

    def should_be_button_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Tehere is no BASKET_BUTTON'

    def right_item_in_basket(self):
        assert self.element_text(*ProductPageLocators.PRODUCT_NAME) == self.element_text(*ProductPageLocators.NAME_IN_BASKET),\
        'Name in basket incorrect'

    def right_price_in_basket(self):
        assert self.element_text(*ProductPageLocators.PRODUCT_PRICE) == self.element_text(
            *ProductPageLocators.PRICE_IN_BASKET), 'Price in basket incorrect'


