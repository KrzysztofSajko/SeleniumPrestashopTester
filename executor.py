from dataclasses import dataclass
from functools import reduce
from typing import List, Dict, Tuple, Optional, Any
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


@dataclass
class Executor:
    driver: Chrome
    pages: PageSet

    def __add_product_to_cart(self,
                              product: ProductWrapper,
                              product_cap: Optional[int] = None,
                              checkout: bool = False) -> None:
        Actions.click(self.driver, product.link)

        product_adder: ProductAdderWrapper = self.pages.product.get_product()
        if product_adder.stock_size == 0:
            return

        product_adder.counter.clear()
        if product_cap:
            limit: int = (product_adder.stock_size
                          if product_adder.stock_size < product_cap
                          else product_cap)
            amount: int = randint(1, limit)
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
            category_product_count[category.id] = len(self.pages.category.get_products())

        return category_product_count

    def __remove_product_from_cart(self):
        product: CartProductWrapper = choice(self.pages.cart.get_cart_products())
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
            if not reduce(lambda a, b: a or b, (product_list for product_list in category_products.values())):
                break

        return product_list

    def skip_https(self) -> None:
        self.pages.https.wait_loaded()
        self.pages.https.skip()

    def scenario_1(self, config: Dict[str, str]) -> None:
        category_product_count: Dict[int, int] = self.__get_category_product_count()
        category_product_count = {k: val
                                  for k, val
                                  in sample(list(category_product_count.items()), k=int(config["categories"]))}
        product_list: List[Tuple[int, int]] = self.__generate_product_list(category_product_count, int(config["products"]))

        for cat_id, product_id in product_list:
            self.pages.base.goto_category(cat_id)
            product: ProductWrapper = self.pages.category.get_product(product_id)
            self.__add_product_to_cart(product, int(config["maxQuantity"]))

    def scenario_2(self, config: Dict[str, str]) -> None:
        self.pages.base.goto_cart()
        for i in range(int(config["products"])):
            self.__remove_product_from_cart()

    def scenario_3(self, config: Dict[str, Any]) -> User:
        self.pages.cart.finish_order()
        user: User = User.create_normal_user()

        self.pages.order.fill_personal_form(user)
        self.pages.order.fill_address_form(user)
        self.pages.order.choose_delivery_method(config["deliveryMethodBlacklist"])
        self.pages.order.choose_payment_method(config["paymentMethod"])
        self.pages.confirmation.wait_load()
        return user

    def scenario_4(self) -> None:
        self.pages.base.goto_account()
        self.pages.account.goto_order_history()
        orders: List[OrderHistoryWrapper] = self.pages.order_history.get_history_orders()
        self.pages.order_history.goto_order_details(orders[0])
