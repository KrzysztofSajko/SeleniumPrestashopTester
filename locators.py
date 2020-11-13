from selenium.webdriver.common.by import By

from myTypes import Locator


class BasePageLocators:
    TOP_MENU: Locator = (By.ID, "top-menu")
    CATEGORY: Locator = (By.CSS_SELECTOR, "a.dropdown-item")
    CATEGORY_CONTAINER: Locator = (By.CSS_SELECTOR, "#top-menu > li")
    CURRENT_CATEGORY_CONTAINER: Locator = (By.CSS_SELECTOR, "#top-menu > li.current")
    CART: Locator = (By.CSS_SELECTOR, "#_desktop_cart > div > div > a")


class MainPageLocators:
    pass


class CategoryPageLocators:
    PRODUCT_LIST: Locator = (By.ID, "js-product-list")
    PRODUCT: Locator = (By.CLASS_NAME, "thumbnail-container")
    PRODUCT_NAME: Locator = (By.CSS_SELECTOR, ".product-description > h1")
    PRODUCT_LINK: Locator = (By.CSS_SELECTOR, ".product-image-block > a")


class ProductPageLocators:
    COUNTER: Locator = (By.ID, "quantity_wanted")
    SUBMIT: Locator = (By.CSS_SELECTOR, "#add-to-cart-or-refresh div.add > button")
    STOCK_SIZE: Locator = (By.CSS_SELECTOR, "#product-details > div.product-quantities > span")
    POPUP_SKIP: Locator = (By.CSS_SELECTOR, "#blockcart-modal div.cart-content-btn > button")
    POPUP_ACCEPT: Locator = (By.CSS_SELECTOR, "#blockcart-modal div.cart-content-btn > a")
    POPUP_CONTAINER: Locator = (By.CSS_SELECTOR, "#blockcart-modal")


class CartPageLocators:
    PRODUCT_LIST: Locator = (By.CSS_SELECTOR, "#main  ul.cart-items > li.cart-item")
    PRODUCT_NAME: Locator = (By.CSS_SELECTOR, "div.product-line-info > a")
    PRODUCT_DELETE: Locator = (By.CSS_SELECTOR,
                               "div.product-line-grid-right div.cart-line-product-actions > a.remove-from-cart")
    FINISH_BUTTON: Locator = (By.CSS_SELECTOR, "#main > div > div.cart-grid-right.col-xs-12.col-lg-4 > div.card.cart-summary > div.checkout.cart-detailed-actions.card-block > div > a")


class OrderPageLocators:
    PERSONAL_MR: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(1) > div.col-md-6.form-control-valign > label:nth-child(1) > span > input[type=radio]")
    PERSONAL_MRS: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(1) > div.col-md-6.form-control-valign > label:nth-child(2) > span > input[type=radio]")
    PERSONAL_NAME: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(2) > div.col-md-6 > input")
    PERSONAL_SURNAME: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(3) > div.col-md-6 > input")
    PERSONAL_EMAIL: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(4) > div.col-md-6 > input")
    PERSONAL_PASSWORD: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(6) > div.col-md-6 > div > input")
    PERSONAL_BIRTHDAY: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(7) > div.col-md-6 > input")
    PERSONAL_NEXT: Locator = (By.CSS_SELECTOR, "#customer-form > footer > button")

