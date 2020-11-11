import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.remote.webelement import WebElement

from myTypes import Locator
from utilty import Waiter, Actions

from typing import List

from locators import BasePageLocators, CategoryPageLocators, ProductPageLocators, CartPageLocators
from wrappers import CategoryWrapper, ProductWrapper, ProductToAddWrapper, CartProductWrapper


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver

    def get_categories(self) -> List[CategoryWrapper]:
        containers: List[WebElement] = Waiter.all_found(self.driver, BasePageLocators.CATEGORY_CONTAINER)
        return [
            CategoryWrapper(
                i,
                category.text,
                category
            )
            for i, category
            in enumerate(map(lambda container:
                             Waiter.clickable(container, BasePageLocators.CATEGORY),
                             containers))
        ]

    def goto_category(self, id: int) -> None:
        containers: List[WebElement] = Waiter.all_found(self.driver, BasePageLocators.CATEGORY_CONTAINER)
        category: WebElement = Waiter.clickable(containers[id], BasePageLocators.CATEGORY)
        Actions.click(self.driver, category)

    def current_category_id(self):
        containers: List[WebElement] = Waiter.all_found(self.driver, BasePageLocators.CATEGORY_CONTAINER)
        cat_names: List[str] = [cat.text
                                for cat
                                in map(lambda container:
                                       Waiter.found(container, BasePageLocators.CATEGORY), containers)
                                ]
        current: WebElement = Waiter.found(self.driver, BasePageLocators.CURRENT_CATEGORY_CONTAINER).find_element(*BasePageLocators.CATEGORY).text
        for i, name in enumerate(cat_names):
            if name == current:
                return i


class MainPage(BasePage):
    pass


class CategoryPage(BasePage):
    def get_products(self) -> List[ProductWrapper]:
        products_container: WebElement = Waiter.found(self.driver, CategoryPageLocators.PRODUCT_LIST)
        category_id: int = self.current_category_id()
        return [
            ProductWrapper(
                i,
                category_id,
                product.find_element(*CategoryPageLocators.PRODUCT_NAME).text,
                Waiter.clickable(product, CategoryPageLocators.PRODUCT_LINK)
            )
            for i, product
            in enumerate(Waiter.all_found(products_container, CategoryPageLocators.PRODUCT))
        ]

    def get_product(self, id: int) -> ProductWrapper:
        products_container: WebElement = Waiter.found(self.driver, CategoryPageLocators.PRODUCT_LIST)
        products: List[WebElement] = Waiter.all_found(products_container, CategoryPageLocators.PRODUCT)
        return ProductWrapper(id,
                              self.current_category_id(),
                              products[id].find_element(*CategoryPageLocators.PRODUCT_NAME).text,
                              Waiter.clickable(products[id], CategoryPageLocators.PRODUCT_LINK))


class ProductPage(BasePage):
    def get_product(self) -> ProductToAddWrapper:
        return ProductToAddWrapper(
            Waiter.clickable(self.driver, ProductPageLocators.COUNTER),
            Waiter.clickable(self.driver, ProductPageLocators.SUBMIT),
            int(Waiter.found(self.driver, ProductPageLocators.STOCK_SIZE).get_attribute("data-stock"))
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
        self.base: BasePage = BasePage(driver)
        self.category: CategoryPage = CategoryPage(driver)
        self.product: ProductPage = ProductPage(driver)
        self.cart: CartPage = CartPage(driver)
