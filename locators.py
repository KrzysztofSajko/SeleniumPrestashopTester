from selenium.webdriver.common.by import By

from myTypes import Locator


class BasePageLocators:
    TOP_MENU: Locator = (By.ID, "top-menu")
    TOP_MENU_CATEGORY: Locator = (By.CLASS_NAME, "dropdown-item")


class MainPageLocators:
    pass


class CategoryPageLocators:
    PRODUCT_LIST: Locator = (By.ID, "js-product-list")
    PRODUCT: Locator = (By.CLASS_NAME, "thumbnail-container")
    PRODUCT_NAME: Locator = (By.CSS_SELECTOR, ".product-description > h1")
    PRODUCT_LINK: Locator = (By.CSS_SELECTOR, ".product-image-block > a")


class ProductPageLocators:
    pass


class CartPageLocators:
    pass
