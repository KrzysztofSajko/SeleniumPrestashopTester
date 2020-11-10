from random import choice

from selenium.webdriver import Chrome

from typing import Dict, Any, List
import json

from pages import PagesSet
from wrappers import ProductWrapper, CategoryWrapper, ProductToAddWrapper

with open("config.json", encoding='utf-8') as config_json:
    config: Dict[str, Any] = json.load(config_json)

chromeDriverPath: str = config['driverPath']
shopAddress: str = config['shopAddress']

driver: Chrome = Chrome(chromeDriverPath)
driver.implicitly_wait(5)
driver.get(shopAddress)

pages: PagesSet = PagesSet(driver)

categories: List[CategoryWrapper] = pages.main.get_categories()
choice(categories).link.click()

products: List[ProductWrapper] = pages.category.get_products()
choice(products).link.click()

product: ProductToAddWrapper = pages.product.get_product()
product.counter.clear()
product.counter.send_keys("5")
print(product.stock_size)
product.submit_button.click()
pages.product.popup_skip()

# driver.quit()


