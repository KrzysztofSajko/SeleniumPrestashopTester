from selenium.webdriver.remote.webelement import WebElement


class OrderHistoryWrapper:
    def __init__(self, id: str, details: WebElement):
        self.id: str = id
        self.details: WebElement = details
