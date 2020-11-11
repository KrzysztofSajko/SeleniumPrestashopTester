import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.remote.webelement import WebElement

from myTypes import Locator
from waiter import Waiter

from typing import List

from locators import BasePageLocators, CategoryPageLocators, ProductPageLocators, CartPageLocators
from wrappers import CategoryWrapper, ProductWrapper, ProductToAddWrapper, CartProductWrapper


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver

    def get_categories(self) -> List[CategoryWrapper]:
        containers: List[WebElement] = Waiter.all_found(self.driver, BasePageLocators.TOP_MENU_CATEGORY_CONTAINER)
        return [
            CategoryWrapper(
                i,
                category.text,
                category
            )
            for i, category
            in enumerate(map(lambda container:
                             Waiter.clickable(container, BasePageLocators.TOP_MENU_CATEGORY),
                             containers))
        ]


class MainPage(BasePage):
    pass


class CategoryPage(BasePage):
    def get_products(self) -> List[ProductWrapper]:
        products_container: WebElement = Waiter.found(self.driver, CategoryPageLocators.PRODUCT_LIST)
        return [
            ProductWrapper(
                i,
                product.find_element(*CategoryPageLocators.PRODUCT_NAME).text,
                Waiter.clickable(product, CategoryPageLocators.PRODUCT_LINK)
            )
            for i, product
            in enumerate(Waiter.all_found(products_container, CategoryPageLocators.PRODUCT))
        ]


class ProductPage(BasePage):
    def get_product(self) -> ProductToAddWrapper:
        return ProductToAddWrapper(
            Waiter.clickable(self.driver, ProductPageLocators.COUNTER),
            Waiter.clickable(self.driver, ProductPageLocators.SUBMIT),
            Waiter.found(self.driver, ProductPageLocators.STOCK_SIZE).get_attribute("data-stock")
        )

    @property
    def popup_active(self) -> bool:
        try:
            popup_container: WebElement = Waiter.visible(self.driver, ProductPageLocators.POPUP_CONTAINER)
            return popup_container.is_displayed()
        except TimeoutException:
            print("Timeout on checking cart popup")
            self.driver.quit()

    def __popup_action(self, action_button: Locator):
        time.sleep(2)
        if self.popup_active:
            time.sleep(1)
            button: WebElement = Waiter.clickable(self.driver, action_button)
            self.driver.execute_script("arguments[0].scrollIntoView();", button)
            ActionChains(self.driver).click(button).perform()

    def popup_skip(self):
        self.__popup_action(ProductPageLocators.POPUP_SKIP)

    def popup_accept(self):
        self.__popup_action(ProductPageLocators.POPUP_ACCEPT)


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


class PagesSet:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver
        self.main: MainPage = MainPage(driver)
        self.category: CategoryPage = CategoryPage(driver)
        self.product: ProductPage = ProductPage(driver)
        self.cart: CartPage = CartPage(driver)
