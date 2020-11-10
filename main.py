from random import choice

from selenium.webdriver import Chrome, ActionChains

from typing import Dict, Any, List
import json

from pages import PagesSet
from wrappers import ProductWrapper, CategoryWrapper, ProductToAddWrapper

with open("config.json", encoding='utf-8') as config_json:
    config: Dict[str, Any] = json.load(config_json)

chromeDriverPath: str = config['driverPath']
shopAddress: str = config['shopAddress']

driver: Chrome = Chrome(chromeDriverPath)
driver.implicitly_wait(2)
driver.get(shopAddress)

pages: PagesSet = PagesSet(driver)

categories: List[CategoryWrapper] = pages.main.get_categories()
ActionChains(driver).click(choice(categories).link).perform()

products: List[ProductWrapper] = pages.category.get_products()
ActionChains(driver).click(choice(products).link).perform()

product: ProductToAddWrapper = pages.product.get_product()
product.counter.clear()
product.counter.send_keys("5")
print(product.stock_size)
ActionChains(driver).click(product.submit_button).perform()
pages.product.popup_skip()

driver.quit()


