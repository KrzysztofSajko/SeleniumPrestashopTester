from selenium.webdriver.remote.webelement import WebElement


class BaseElementWrapper:
    def __init__(self, id: int, name: str, link: WebElement):
        self.id: int = id
        self.name: str = name
        self.link: WebElement = link


class CategoryWrapper(BaseElementWrapper):
    pass


class ProductWrapper(BaseElementWrapper):
    pass


class ProductToAddWrapper:
    def __init__(self, counter: WebElement, submit_button: WebElement, stock_size: int):
        self.counter: WebElement = counter
        self.submit_button: WebElement = submit_button
        self.stock_size: int = stock_size


class CartProductWrapper:
    def __init__(self, id: int, name: str, delete: WebElement):
        self.id: int = id
        self.name: str = name
        self.delete: WebElement = delete
