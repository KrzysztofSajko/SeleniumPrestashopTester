from typing import List

from selenium.webdriver.remote.webelement import WebElement

from locators import CartPageLocators
from pages.basePage import BasePage
from utility.waiter import Waiter
from wrappers.cartProductWrapper import CartProductWrapper


class CartPage(BasePage):
    def get_cart_products(self) -> List[CartProductWrapper]:
        products: List[WebElement] = Waiter.all_found(self.driver, CartPageLocators.PRODUCT_LIST)
        return [
            CartProductWrapper(
                i,
                Waiter.found(product, CartPageLocators.PRODUCT_NAME).text,
                Waiter.clickable(product, CartPageLocators.PRODUCT_DELETE)
            )
            for i, product
            in enumerate(products)
        ]