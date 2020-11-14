from selenium.webdriver import Chrome

from pages.accountPage import AccountPage
from pages.confirmationPage import ConfirmationPage
from pages.orderHistoryPage import OrderHistoryPage
from pages.orderPage import OrderPage
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
        self.order: OrderPage = OrderPage(driver)
        self.account: AccountPage = AccountPage(driver)
        self.order_history: OrderHistoryPage = OrderHistoryPage(driver)
        self.confirmation: ConfirmationPage = ConfirmationPage(driver)
