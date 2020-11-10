from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Optional, Dict, Union
from locators import MainPageLocators, BasePageLocators, CategoryPageLocators
from wrappers import CategoryWrapper, ProductWrapper


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver

    def get_categories(self) -> List[CategoryWrapper]:
        main_menu: WebElement = self.driver.find_element(*BasePageLocators.TOP_MENU)
        return [
            CategoryWrapper(i, category.text, category)
            for i, category
            in enumerate(main_menu.find_elements(*BasePageLocators.TOP_MENU_CATEGORY))
        ]


class MainPage(BasePage):
    pass


class CategoryPage(BasePage):
    def get_products(self) -> List[ProductWrapper]:
        products_container: WebElement = self.driver.find_element(*CategoryPageLocators.PRODUCT_LIST)
        return [
            ProductWrapper(
                i,
                product.find_element(*CategoryPageLocators.PRODUCT_NAME).text,
                product.find_element(*CategoryPageLocators.PRODUCT_LINK)
            )
            for i, product
            in enumerate(products_container.find_elements(*CategoryPageLocators.PRODUCT))
        ]


class ProductPage(BasePage):
    pass


class CartPage(BasePage):
    pass
