from typing import List

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement

from locators import BasePageLocators
from utility.actions import Actions
from utility.waiter import Waiter
from wrappers.categoryWrapper import CategoryWrapper


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
        current: WebElement = Waiter.found(self.driver,
                                           BasePageLocators.CURRENT_CATEGORY_CONTAINER).find_element(*BasePageLocators.CATEGORY).text
        for i, name in enumerate(cat_names):
            if name == current:
                return i
