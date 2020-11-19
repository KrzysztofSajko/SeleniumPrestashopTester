from time import time
from typing import Dict, Any, List
import json

from faker import Faker
from selenium.webdriver import Chrome

from pages.pageSet import PageSet
from executor import Executor


Faker.seed(int(time()))

with open("config.json", encoding='utf-8') as config_json:
    config: Dict[str, Any] = json.load(config_json)

chromeDriverPath: str = config['driverPath']
shopAddress: str = config['shopAddress']

driver: Chrome = Chrome(chromeDriverPath)
driver.implicitly_wait(10)
driver.get(shopAddress)

pages: PageSet = PageSet(driver)

executor: Executor = Executor(driver, pages)

executor.skip_https()
executor.scenario_1(config["scenario1"])
executor.scenario_2(config["scenario2"])
executor.scenario_3(config["scenario3"])

executor.scenario_4()


