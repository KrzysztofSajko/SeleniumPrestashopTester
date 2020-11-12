from selenium.webdriver.remote.webelement import WebElement

from wrappers.baseElementWrapper import BaseElementWrapper


class ProductWrapper(BaseElementWrapper):
    def __init__(self, id: int, category_id: int, name: str, link: WebElement):
        super().__init__(id, name, link)
        self.category_id: int = category_id
