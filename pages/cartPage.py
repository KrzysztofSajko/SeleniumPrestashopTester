from typing import List

from locators import CartPageLocators
from pages.basePage import BasePage
from utility.actions import Actions
from utility.waiter import Waiter
from wrappers.cartProductWrapper import CartProductWrapper


class CartPage(BasePage):
    def get_cart_products(self) -> List[CartProductWrapper]:
        return [
            CartProductWrapper(
                i,
                Waiter.found(product, CartPageLocators.PRODUCT_NAME).text,
                Waiter.clickable(product, CartPageLocators.PRODUCT_DELETE)
            )
            for i, product
            in enumerate(Waiter.all_found(self.driver, CartPageLocators.PRODUCT_LIST))
        ]

    def finish_order(self) -> None:
        Actions.click(self.driver, Waiter.clickable(self.driver, CartPageLocators.FINISH_BUTTON))
