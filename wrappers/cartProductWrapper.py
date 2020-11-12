from selenium.webdriver.remote.webelement import WebElement


class CartProductWrapper:
    def __init__(self, id: int, name: str, delete: WebElement):
        self.id: int = id
        self.name: str = name
        self.delete: WebElement = delete
