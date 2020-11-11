from selenium.webdriver.common.by import By

from myTypes import Locator


class BasePageLocators:
    TOP_MENU: Locator = (By.ID, "top-menu")
    CATEGORY: Locator = (By.CSS_SELECTOR, "a.dropdown-item")
    CATEGORY_CONTAINER: Locator = (By.CSS_SELECTOR, "#top-menu > li")
    CURRENT_CATEGORY_CONTAINER: Locator = (By.CSS_SELECTOR, "#top-menu > li.current")


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
