from typing import Union, List


from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ActionChains

from myTypes import Locator




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
