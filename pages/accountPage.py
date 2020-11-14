from locators import AccountPageLocators
from pages.basePage import BasePage


class AccountPage(BasePage):
    def goto_info(self):
        self.goto(AccountPageLocators.OPTIONS_INFO)

    def goto_address(self):
        self.goto(AccountPageLocators.OPTIONS_ADDRESS)

    def goto_order_history(self):
        self.goto(AccountPageLocators.OPTIONS_ORDER_HISTORY)

    def goto_receipts(self):
        self.goto(AccountPageLocators.OPTIONS_ORDER_HISTORY)
