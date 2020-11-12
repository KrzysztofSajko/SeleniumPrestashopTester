from selenium.webdriver import Chrome

from pages.basePage import BasePage
from pages.cartPage import CartPage
from pages.categoryPage import CategoryPage
from pages.mainPage import MainPage
from pages.productPage import ProductPage


class PageSet:
    def __init__(self, driver: Chrome):
        self.driver: Chrome = driver
        self.main: MainPage = MainPage(driver)
        self.base: BasePage = BasePage(driver)
        self.category: CategoryPage = CategoryPage(driver)
        self.product: ProductPage = ProductPage(driver)
        self.cart: CartPage = CartPage(driver)
