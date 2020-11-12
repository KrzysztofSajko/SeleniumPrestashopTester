from selenium.webdriver.remote.webelement import WebElement


class ProductAdderWrapper:
    def __init__(self, counter: WebElement, submit_button: WebElement, stock_size: int):
        self.counter: WebElement = counter
        self.submit_button: WebElement = submit_button
        self.stock_size: int = stock_size
