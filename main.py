from random import choice

from selenium.webdriver import Chrome

from typing import Dict, Any, List
import json

from myTypes import ListedProduct
from pages import MainPage, CategoryPage

with open("config.json", encoding='utf-8') as config_json:
    config: Dict[str, Any] = json.load(config_json)

chromeDriverPath: str = config['driverPath']
driver: Chrome = Chrome(chromeDriverPath)

shopAddress: str = config['shopAddress']
driver.get(shopAddress)

main_page: MainPage = MainPage(driver)
category_page: CategoryPage = CategoryPage(driver)

categories: List[str] = config['categories']

main_page.goto_category(choice(categories))

products: List[ListedProduct] = category_page.get_products()
choice(products)["link"].click()

# driver.quit()


