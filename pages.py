import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from typing import List

from locators import MainPageLocators, BasePageLocators, CategoryPageLocators, ProductPageLocators
from wrappers import CategoryWrapper, ProductWrapper, ProductToAddWrapper


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
    def get_product(self) -> ProductToAddWrapper:
        return ProductToAddWrapper(
            self.driver.find_element(*ProductPageLocators.COUNTER),
            self.driver.find_element(*ProductPageLocators.SUBMIT),
            self.driver.find_element(*ProductPageLocators.STOCK_SIZE).get_attribute("data-stock")
        )

    @property
    def popup_active(self) -> bool:
        try:
            popup_container: WebElement = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ProductPageLocators.POPUP_CONTAINER))

            print(popup_container.is_displayed())
            return popup_container.is_displayed()
        except TimeoutException:
            print("Timeout on checking cart popup")
            self.driver.quit()

    def popup_skip(self):
        time.sleep(1.5)
        if self.popup_active:
            self.driver.find_element(*ProductPageLocators.POPUP_SKIP).click()
            print("fired")

    def popup_accept(self):
        time.sleep(1.5)
        if self.popup_active:
            self.driver.find_element(*ProductPageLocators.POPUP_ACCEPT).click()


class CartPage(BasePage):
    pass


class PagesSet:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver
        self.main: MainPage = MainPage(driver)
        self.category: CategoryPage = CategoryPage(driver)
        self.product: ProductPage = ProductPage(driver)