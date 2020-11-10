from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Optional, Dict, Union
from locators import MainPageLocators, BasePageLocators, CategoryPageLocators
from myTypes import ListedProduct


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver

    def get_category(self, category_name: str) -> Optional[WebElement]:
        main_menu: WebElement = self.driver.find_element(*BasePageLocators.TOP_MENU)
        categories: List[WebElement] = main_menu.find_elements(*BasePageLocators.TOP_MENU_CATEGORY)
        try:
            return [cat for cat in categories if cat.text.lower() == category_name].pop()
        except IndexError:
            print(f"No such category: {category_name}")
            self.driver.quit()
            return None

    def goto_category(self, category_name: str) -> None:
        category: Optional[WebElement] = self.get_category(category_name)
        if category is not None:
            category.click()


class MainPage(BasePage):
    pass


class CategoryPage(BasePage):
    def goto_product(self, index: int):
        pass

    def get_products(self) -> List[ListedProduct]:
        products_container: WebElement = self.driver.find_element(*CategoryPageLocators.PRODUCT_LIST)
        return [{
            "id": i,
            "name": product.find_element(*CategoryPageLocators.PRODUCT_NAME).text,
            "link": product.find_element(*CategoryPageLocators.PRODUCT_LINK)
        } for i, product in enumerate(products_container.find_elements(*CategoryPageLocators.PRODUCT))]


class ProductPage(BasePage):
    pass


class CartPage(BasePage):
    pass
