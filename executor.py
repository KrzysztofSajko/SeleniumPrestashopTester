from functools import reduce
from typing import List, Dict, Tuple
from random import shuffle, sample, randint

from pages import PagesSet
from selenium.webdriver import Chrome

from utilty import Actions
from wrappers import ProductWrapper, ProductToAddWrapper, CategoryWrapper


class Executor:
    def __init__(self, driver: Chrome, pages: PagesSet):
        self.driver: Chrome = driver
        self.pages: PagesSet = pages

    def add_product_to_cart(self, product: ProductWrapper, checkout: bool = False) -> None:
        Actions.click(self.driver, product.link)

        product_adder: ProductToAddWrapper = self.pages.product.get_product()
        product_adder.counter.clear()
        product_adder.counter.send_keys(f"{randint(1, product_adder.stock_size)}")
        Actions.click(self.driver, product_adder.submit_button)

        if checkout:
            self. pages.product.popup_accept()
        else:
            self. pages.product.popup_skip()

    def pick_categories(self, quantity: int) -> List[int]:
        return [c.id for c in sample(self.pages.base.get_categories(), k=quantity)]

    def __get_category_product_count(self) -> Dict[int, int]:
        categories: List[CategoryWrapper] = self.pages.base.get_categories()
        category_product_count: Dict[int, int] = {}
        for category in categories:
            self.pages.base.goto_category(category.id)
            products: List[ProductWrapper] = self.pages.category.get_products()
            category_product_count[category.id] = len(products)
        return category_product_count

    @staticmethod
    def __generate_product_list(category_product_count: Dict[int, int], quantity: int) -> List[Tuple[int, int]]:
        product_list: List[Tuple[int, int]] = []
        category_products: Dict[int, List[int]] = {k: list(range(val))
                                                   for k, val
                                                   in category_product_count.items()}
        for products in category_products.values():
            shuffle(products)

        i: int = 0
        j: int = 0
        while i < quantity:
            cat_id: int = list(category_products.keys())[j % len(category_products)]
            if category_products[cat_id]:
                product_list.append((cat_id, category_products[cat_id].pop()))
                i += 1
            j += 1
            if not reduce(lambda a, b: a or b, category_products.values()):
                break

        return product_list

    def scenario_1(self, n_categories: int, n_products: int):
        category_product_count: Dict[int, int] = self.__get_category_product_count()
        category_product_count = {k: val
                                  for k, val
                                  in sample(list(category_product_count.items()), k=n_categories)}
        product_list: List[Tuple[int, int]] = self.__generate_product_list(category_product_count, n_products)
        for cat_id, product_id in product_list:
            self.pages.base.goto_category(cat_id)
            product: ProductWrapper = self.pages.category.get_product(product_id)
            if product.name.lower() != "customizable mug":
                self.add_product_to_cart(product)
