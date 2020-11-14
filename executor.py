from functools import reduce
from typing import List, Dict, Tuple, Optional
from random import shuffle, sample, randint, choice

from pages.pageSet import PageSet
from selenium.webdriver import Chrome

from utility.user import User
from utility.actions import Actions
from utility.waiter import Waiter
from wrappers.cartProductWrapper import CartProductWrapper
from wrappers.orderHistoryWrapper import OrderHistoryWrapper
from wrappers.productWrapper import ProductWrapper
from wrappers.productAdderWrapper import ProductAdderWrapper
from wrappers.categoryWrapper import CategoryWrapper


class Executor:
    def __init__(self, driver: Chrome, pages: PageSet):
        self.driver: Chrome = driver
        self.pages: PageSet = pages

    def __add_product_to_cart(self, product: ProductWrapper, product_cap: Optional[int] = None, checkout: bool = False, ) -> None:
        Actions.click(self.driver, product.link)

        product_adder: ProductAdderWrapper = self.pages.product.get_product()
        product_adder.counter.clear()
        if product_cap:
            amount: int = randint(1,
                                  product_adder.stock_size
                                  if product_adder.stock_size < product_cap
                                  else product_cap)
        else:
            amount: int = randint(1, product_adder.stock_size)
        product_adder.counter.send_keys(f"{amount}")
        Actions.click(self.driver, product_adder.submit_button)

        if checkout:
            self. pages.product.popup_accept()
        else:
            self. pages.product.popup_skip()

    def __get_category_product_count(self) -> Dict[int, int]:
        categories: List[CategoryWrapper] = self.pages.base.get_categories()
        category_product_count: Dict[int, int] = {}
        for category in categories:
            self.pages.base.goto_category(category.id)
            products: List[ProductWrapper] = self.pages.category.get_products()
            category_product_count[category.id] = len(products)
        return category_product_count

    def __remove_product_from_cart(self):
        products: List[CartProductWrapper] = self.pages.cart.get_cart_products()
        product: CartProductWrapper = choice(products)
        Actions.click(self.driver, product.delete)
        Waiter.not_in_dom(self.driver, product.delete)

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

    def scenario_1(self, n_categories: int, n_products: int, product_cap: int) -> None:
        category_product_count: Dict[int, int] = self.__get_category_product_count()
        category_product_count = {k: val
                                  for k, val
                                  in sample(list(category_product_count.items()), k=n_categories)}
        product_list: List[Tuple[int, int]] = self.__generate_product_list(category_product_count, n_products)
        for cat_id, product_id in product_list:
            self.pages.base.goto_category(cat_id)
            product: ProductWrapper = self.pages.category.get_product(product_id)
            if product.name.lower() != "customizable mug":
                self.__add_product_to_cart(product, product_cap)

    def scenario_2(self, n_products: int) -> None:
        self.pages.base.goto_cart()
        for i in range(n_products):
            self.__remove_product_from_cart()

    def scenario_3(self, delivery_blacklist: List[str], payment_method: str) -> User:
        self.pages.cart.finish_order()
        user: User = User.create_normal_user()
        self.pages.order.fill_personal_form(user)
        self.pages.order.fill_address_form(user)
        self.pages.order.choose_delivery_method(delivery_blacklist)
        self.pages.order.choose_payment_method(payment_method)
        self.pages.confirmation.wait_load()
        return user

    def scenario_4(self) -> None:
        self.pages.base.goto_account()
        self.pages.account.goto_order_history()
        orders: List[OrderHistoryWrapper] = self.pages.order_history.get_history_orders()
        self.pages.order_history.goto_order_details(orders[0])
