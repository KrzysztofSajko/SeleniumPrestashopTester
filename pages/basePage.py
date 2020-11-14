from typing import List, Union, Optional

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement

from locators import BasePageLocators
from utility.actions import Actions
from utility.myTypes import Locator
from utility.waiter import Waiter
from wrappers.categoryWrapper import CategoryWrapper


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver

    def goto(self, locator: Locator, container: Optional[Union[Chrome, WebElement]] = None) -> None:
        container = container or self.driver
        Actions.click(self.driver, Waiter.clickable(container, locator))

    def goto_account(self) -> None:
        self.goto(BasePageLocators.UserAccount)

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
        # containers: List[WebElement] = Waiter.all_found(self.driver, BasePageLocators.CATEGORY_CONTAINER)
        # category: WebElement = Waiter.clickable(containers[id], BasePageLocators.CATEGORY)
        # Actions.click(self.driver, category)
        self.goto(BasePageLocators.CATEGORY,
                  Waiter.all_found(self.driver,
                                   BasePageLocators.CATEGORY_CONTAINER)[id])

    def goto_cart(self):
        # button: WebElement = Waiter.clickable(self.driver, BasePageLocators.CART)
        # Actions.click(self.driver, button)
        self.goto(BasePageLocators.CART)

    def current_category_id(self):
        containers: List[WebElement] = Waiter.all_found(self.driver, BasePageLocators.CATEGORY_CONTAINER)
        cat_names: List[str] = [cat.text
                                for cat
                                in map(lambda container:
                                       Waiter.found(container, BasePageLocators.CATEGORY), containers)
                                ]
        current: WebElement = Waiter.found(self.driver,
                                           BasePageLocators.CURRENT_CATEGORY_CONTAINER).find_element(*BasePageLocators.CATEGORY).text
        for i, name in enumerate(cat_names):
            if name == current:
                return i
