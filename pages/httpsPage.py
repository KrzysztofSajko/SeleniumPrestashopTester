from selenium.webdriver import Chrome

from locators import HttpsPageLocators
from utility.actions import Actions
from utility.waiter import Waiter


class HttpsPage:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver

    def wait_loaded(self, timeout: int = 120) -> None:
        Waiter.clickable(self.driver, HttpsPageLocators.ADVANCED)

    def skip(self) -> None:
        Actions.click(self.driver, Waiter.clickable(self.driver, HttpsPageLocators.ADVANCED))
        Actions.click(self.driver, Waiter.clickable(self.driver, HttpsPageLocators.LINK))