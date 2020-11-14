from typing import List

from selenium.webdriver.remote.webelement import WebElement

from locators import CategoryPageLocators
from pages.basePage import BasePage
from utility.waiter import Waiter
from wrappers.productWrapper import ProductWrapper


class CategoryPage(BasePage):
    def get_products(self) -> List[ProductWrapper]:
        products_container: WebElement = Waiter.found(self.driver, CategoryPageLocators.PRODUCT_LIST)
        category_id: int = self.current_category_id()
        return [
            ProductWrapper(
                i,
                category_id,
                product.find_element(*CategoryPageLocators.PRODUCT_NAME).text,
                Waiter.clickable(product, CategoryPageLocators.PRODUCT_LINK))
            for i, product
            in enumerate(Waiter.all_found(products_container, CategoryPageLocators.PRODUCT))]

    def get_product(self, id: int) -> ProductWrapper:
        products_container: WebElement = Waiter.found(self.driver, CategoryPageLocators.PRODUCT_LIST)
        products: List[WebElement] = Waiter.all_found(products_container, CategoryPageLocators.PRODUCT)
        return ProductWrapper(id,
                              self.current_category_id(),
                              products[id].find_element(*CategoryPageLocators.PRODUCT_NAME).text,
                              Waiter.clickable(products[id], CategoryPageLocators.PRODUCT_LINK))
