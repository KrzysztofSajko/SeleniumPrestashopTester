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

n_products: int = int(config["scenario_1"]["n_categories"])
n_items: int = int(config["scenario_1"]["n_items"])
product_cap: int = int(config["scenario_1"]["product_cap"])
executor.scenario_1(n_products, n_items, product_cap)

n_products: int = int(config["scenario_2"]["n_products"])
executor.scenario_2(n_products)

delivery_blacklist: List[str] = config["scenario_3"]["delivery_method_blacklist"]
payment_method: str = config["scenario_3"]["payment_method"]
executor.scenario_3(delivery_blacklist, payment_method)

executor.scenario_4()


