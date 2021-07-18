from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM =(By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FORM = (By.ID, 'id_registration-email')
    REGISTER_PASS_FORM = (By.ID, 'id_registration-password1')
    REGISTER_CONFIRM_PASS_FORM = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form > .btn')

class CatalogLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    ADD_PRODUCT_PRICE = (By.CSS_SELECTOR, '#messages >.alert:last-child > .alertinner > p:first-child > strong')
    ADD_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages >.alert:first-child > .alertinner > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages >.alert:first-child > .alertinner')

class BasketPageLocators:
        EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
        NOT_EMPTY_BASKET = (By.CSS_SELECTOR, '.row > h2')

