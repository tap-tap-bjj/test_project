from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def item_should_be_in_basket(self):
        self.should_be_button_basket()
        self.try_find_element(*ProductPageLocators.BASKET_BUTTON).click()
        #self.solve_quiz_and_get_code()
        self.right_item_in_basket()
        self.right_price_in_basket()

    def should_be_button_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Tehere is no BASKET_BUTTON'

    def right_item_in_basket(self):
        assert self.try_find_element(*ProductPageLocators.PRODUCT_NAME).text == self.try_find_element(*ProductPageLocators.NAME_IN_BASKET).text,\
        'Name in basket incorrect'

    def right_price_in_basket(self):
        assert self.try_find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.try_find_element(
            *ProductPageLocators.PRICE_IN_BASKET).text, 'Price in basket incorrect'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
        'Success message not disappeared, but should be'