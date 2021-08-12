from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET_EXIST), "Product exist in basket, but basket should be empty"

    def should_be_message_that_basket_is_empty(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)
        assert message, "Text 'Your basket is empty.' is absent"