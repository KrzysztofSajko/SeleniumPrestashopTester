from typing import Union, List


from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ActionChains

from myTypes import Locator


class Waiter:
    @classmethod
    def clickable(cls, element: Union[WebElement, Chrome], locator: Locator, timeout: int = 10) -> WebElement:
        return WebDriverWait(element, timeout).until(EC.element_to_be_clickable(locator))

    @classmethod
    def all_found(cls, element: Union[WebElement, Chrome], locator: Locator, timeout: int = 10) -> List[WebElement]:
        return WebDriverWait(element, timeout).until(EC.presence_of_all_elements_located(locator))

    @classmethod
    def found(cls, element: Union[WebElement, Chrome], locator: Locator, timeout: int = 10) -> WebElement:
        return WebDriverWait(element, timeout).until(EC.presence_of_element_located(locator))

    @classmethod
    def visible(cls, element: Union[WebElement, Chrome], locator: Locator, timeout: int = 10) -> WebElement:
        return WebDriverWait(element, timeout).until(EC.visibility_of_element_located(locator))


class Actions:
    @classmethod
    def click(cls, driver: Chrome, element: WebElement, scroll_to: bool = True, move_to: bool = True):
        chain: ActionChains = ActionChains(driver)
        if scroll_to:
            driver.execute_script("arguments[0].scrollIntoView();", element)
        if move_to:
            chain.move_to_element(element)
        chain.click()
        chain.perform()
