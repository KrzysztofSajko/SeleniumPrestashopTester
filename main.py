from typing import Dict, Any
import json

from selenium.webdriver import Chrome

from pages import PagesSet
from executor import Executor

with open("config.json", encoding='utf-8') as config_json:
    config: Dict[str, Any] = json.load(config_json)

chromeDriverPath: str = config['driverPath']
shopAddress: str = config['shopAddress']

driver: Chrome = Chrome(chromeDriverPath)
driver.implicitly_wait(10)
driver.get(shopAddress)

pages: PagesSet = PagesSet(driver)

executor: Executor = Executor(driver, pages)

executor.scenario_1(2, 10)


