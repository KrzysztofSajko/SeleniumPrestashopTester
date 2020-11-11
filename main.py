import time
from random import choice

from selenium.webdriver import Chrome, ActionChains

from typing import Dict, Any, List
import json

from pages import PagesSet
from wrappers import ProductWrapper, CategoryWrapper, ProductToAddWrapper, CartProductWrapper

with open("config.json", encoding='utf-8') as config_json:
    config: Dict[str, Any] = json.load(config_json)

chromeDriverPath: str = config['driverPath']
shopAddress: str = config['shopAddress']

driver: Chrome = Chrome(chromeDriverPath)
driver.implicitly_wait(10)
driver.get(shopAddress)

pages: PagesSet = PagesSet(driver)

categories: List[CategoryWrapper] = pages.main.get_categories()

delay: int = 0
for i in range(10):
    time.sleep(delay)
    category: CategoryWrapper = choice(categories)
    print(f"Picked category id: {category.id}")
    # driver.execute_script("arguments[0].scrollIntoView();", category.link)
    ActionChains(driver).move_to_element(category.link).click().perform()
    time.sleep(delay)

    products: List[ProductWrapper] = pages.category.get_products()
    products = [p for p in products if p.name != "Customizable Mug"]
    random_product: ProductWrapper = choice(products)
    print(f"Picked product id: {random_product.id}")
    driver.execute_script("arguments[0].scrollIntoView();", random_product.link)
    ActionChains(driver).move_to_element(random_product.link).click().perform()
    time.sleep(delay)

    product: ProductToAddWrapper = pages.product.get_product()
    product.counter.clear()
    product.counter.send_keys("5")
    # driver.execute_script("arguments[0].scrollIntoView();", product.submit_button)
    ActionChains(driver).move_to_element(product.submit_button).click().perform()
    time.sleep(delay)

    if i != 9:
        pages.product.popup_skip()
        categories = pages.product.get_categories()

pages.product.popup_accept()

cart_products: List[CartProductWrapper] = pages.cart.get_cart_products()
for p in cart_products:
    print(p.id, p.name)

driver.quit()


