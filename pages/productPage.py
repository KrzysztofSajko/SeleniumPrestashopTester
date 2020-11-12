import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

from locators import ProductPageLocators
from myTypes import Locator
from pages.basePage import BasePage
from utility.actions import Actions
from utility.waiter import Waiter
from wrappers.productAdderWrapper import ProductAdderWrapper


class ProductPage(BasePage):
    def get_product(self) -> ProductAdderWrapper:
        return ProductAdderWrapper(
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
            Actions.click(self.driver, button)

    def popup_skip(self):
        self.__popup_action(ProductPageLocators.POPUP_SKIP)

    def popup_accept(self):
        self.__popup_action(ProductPageLocators.POPUP_ACCEPT)
