from selenium.webdriver.remote.webelement import WebElement


class DeliveryMethodWrapper:
    def __init__(self, name: str, radio: WebElement):
        self.name: str = name
        self.radio: WebElement = radio
