from typing import Dict, Tuple, Union
from selenium.webdriver.common.by import By
from enum import Enum, auto, unique

Locator = Tuple[By, str]


@unique
class Gender(Enum):
    FEMALE = auto()
    MALE = auto()


