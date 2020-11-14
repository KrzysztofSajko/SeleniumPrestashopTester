from selenium.webdriver.remote.webelement import WebElement


class PaymentMethodWrapper:
    def __init__(self, name: str, radio: WebElement):
        self.name: str = name
        self.radio: WebElement = radio
