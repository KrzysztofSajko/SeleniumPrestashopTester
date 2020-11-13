import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Chrome, ActionChains


class Actions:
    @classmethod
    def click(cls,
              driver: Chrome,
              element: WebElement,
              scroll_to_element: bool = True,
              move_to: bool = True):
        chain: ActionChains = ActionChains(driver)
        if scroll_to_element:
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(0.5)
        if move_to:
            chain.move_to_element(element)
        chain.click(element)
        chain.perform()
