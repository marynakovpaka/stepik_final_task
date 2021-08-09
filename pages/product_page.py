from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
       basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
       product_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
       product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
       basket.click()
       #self.solve_quiz_and_get_code()
       product_name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_BASKET).text
       product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
       assert product_name == product_name_in_basket, "Product name in basket is wrong"
       assert product_price == product_price_in_basket, "Product name in basket is wrong"

    def should_not_be_success_message(self):
       assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
       assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should dissapear, but it is not"
















