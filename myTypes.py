from typing import Dict, Tuple, Union
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# ListedProduct = Dict[str, Union[int, str, WebElement]]
# ListedCategory = Dict[str, Union[int, str, WebElement]]
Locator = Tuple[By, str]
