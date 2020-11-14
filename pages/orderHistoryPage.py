from typing import List

from selenium.webdriver.remote.webelement import WebElement

from locators import OrderHistoryPageLocators
from pages.basePage import BasePage
from utility.actions import Actions
from utility.waiter import Waiter
from wrappers.orderHistoryWrapper import OrderHistoryWrapper


class OrderHistoryPage(BasePage):
    def goto_order_details(self, order: OrderHistoryWrapper) -> None:
        Actions.click(self.driver, order.details)

    def check_if_table(self) -> bool:
        table: WebElement = Waiter.found(self.driver, OrderHistoryPageLocators.ORDER_TABLE)
        return table.is_displayed()

    def get_history_orders(self) -> List[OrderHistoryWrapper]:
        if self.check_if_table():
            return [
                OrderHistoryWrapper(
                    Waiter.found(row, OrderHistoryPageLocators.ROW_ORDER_ID).text,
                    Waiter.clickable(row, OrderHistoryPageLocators.ROW_ORDER_DETAILS))
                for row
                in Waiter.all_found(self.driver, OrderHistoryPageLocators.TABLE_ROWS)]
        else:
            return [
                OrderHistoryWrapper(
                    Waiter.found(div, OrderHistoryPageLocators.DIV_ORDER_ID).text,
                    Waiter.clickable(div, OrderHistoryPageLocators.DIV_ORDER_DETAILS))
                for div
                in Waiter.all_found(self.driver, OrderHistoryPageLocators.DIV_ORDER)]
