
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    OPEN_BASKET_SCREEN_BUTTON = (By.CSS_SELECTOR,".btn-group :first-child")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR,".content_inner :first-child")
    PRODUCT_IN_BASKET_EXIST = (By.CSS_SELECTOR,"a.btn.btn-lg.btn-primary.btn-block")


class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main :first-child")
    NAME_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong:first-child")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "div .alertinner p:first-child strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div .alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    BASKET_IS_EMPTY_MESSAGE = (By.XPATH, "//p[contains(text(),'empty')]")
    PRODUCT_IN_BASKET_EXIST = (By.CSS_SELECTOR, "a.btn.btn-lg.btn-primary.btn-block")

