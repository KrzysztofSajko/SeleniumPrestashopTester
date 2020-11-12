from selenium.webdriver.remote.webelement import WebElement


class BaseElementWrapper:
    def __init__(self, id: int, name: str, link: WebElement):
        self.id: int = id
        self.name: str = name
        self.link: WebElement = link
