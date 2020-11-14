from locators import ConfirmationPageLocators
from pages.basePage import BasePage
from utility.waiter import Waiter


class ConfirmationPage(BasePage):
    def wait_load(self, timeout=60) -> None:
        Waiter.found(self.driver, ConfirmationPageLocators.BODY, timeout=timeout)
