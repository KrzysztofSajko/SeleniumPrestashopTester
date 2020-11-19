from dataclasses import dataclass
from random import choice
from typing import List, Optional

from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement

from locators import OrderPageLocators
from utility.myTypes import Gender, Locator
from utility.user import User
from utility.actions import Actions
from utility.waiter import Waiter
from wrappers.deliveryMethodWrapper import DeliveryMethodWrapper
from wrappers.paymentMethodWrapper import PaymentMethodWrapper

@dataclass
class OrderPage:
    driver: Chrome

    def select_gender(self, gender: Gender) -> None:
        locator: Locator = OrderPageLocators.PERSONAL_MR if gender == Gender.MALE else OrderPageLocators.PERSONAL_MRS
        Actions.click(self.driver, Waiter.found(self.driver, locator))

    def __enter_to_input(self, locator: Locator, text: str) -> None:
        Actions.input_text(self.driver, Waiter.found(self.driver, locator), text)

    def enter_name(self, name: str) -> None:
        self.__enter_to_input(OrderPageLocators.PERSONAL_NAME, name)

    def enter_surname(self, surname: str) -> None:
        self.__enter_to_input(OrderPageLocators.PERSONAL_SURNAME, surname)

    def enter_email(self, email: str) -> None:
        self.__enter_to_input(OrderPageLocators.PERSONAL_EMAIL, email)

    def enter_password(self, password: str) -> None:
        self.__enter_to_input(OrderPageLocators.PERSONAL_PASSWORD, password)

    def enter_birthday(self, birthday: str) -> None:
        self.__enter_to_input(OrderPageLocators.PERSONAL_BIRTHDAY, birthday)

    def enter_address(self, address: str) -> None:
        self.__enter_to_input(OrderPageLocators.ADDRESS_ADDRESS, address)

    def enter_postcode(self, postcode: str) -> None:
        self.__enter_to_input(OrderPageLocators.ADDRESS_POSTCODE, postcode)

    def enter_city(self, city: str) -> None:
        self.__enter_to_input(OrderPageLocators.ADDRESS_CITY, city)

    def next_personal(self) -> None:
        Actions.click(self.driver, Waiter.clickable(self.driver, OrderPageLocators.PERSONAL_NEXT))

    def next_address(self) -> None:
        Actions.click(self.driver, Waiter.clickable(self.driver, OrderPageLocators.ADDRESS_NEXT))

    def next_delivery(self) -> None:
        Actions.click(self.driver, Waiter.clickable(self.driver, OrderPageLocators.DELIVERY_METHOD_NEXT))

    def accept_payment(self) -> None:
        Actions.click(self.driver, Waiter.enabled(self.driver, OrderPageLocators.PAYMENT_ACCEPT))

    def wait_personal(self, timeout=60) -> None:
        Waiter.clickable(self.driver, OrderPageLocators.PERSONAL_NEXT, timeout=timeout)

    def wait_address(self, timeout=60) -> None:
        Waiter.clickable(self.driver, OrderPageLocators.ADDRESS_NEXT, timeout=timeout)

    def wait_delivery(self, timeout=60) -> None:
        Waiter.clickable(self.driver, OrderPageLocators.DELIVERY_METHOD_NEXT, timeout=timeout)

    def wait_payment(self, timeout=60) -> None:
        Waiter.found(self.driver, OrderPageLocators.PAYMENT_ACCEPT, timeout=timeout)

    def get_delivery_methods(self) -> List[DeliveryMethodWrapper]:
        return [
            DeliveryMethodWrapper(
                Waiter.found(method, OrderPageLocators.DELIVERY_METHOD_NAME).text,
                Waiter.found(method, OrderPageLocators.DELIVERY_METHOD_RADIO))
            for i, method
            in enumerate(Waiter.all_found(self.driver, OrderPageLocators.DELIVERY_METHODS))]

    def get_payment_methods(self) -> List[PaymentMethodWrapper]:
        return [
            PaymentMethodWrapper(
                Waiter.found(method, OrderPageLocators.PAYMENT_METHOD_NAME).text,
                Waiter.found(method, OrderPageLocators.PAYMENT_METHOD_RADIO))
            for method
            in Waiter.all_found(self.driver, OrderPageLocators.PAYMENT_METHODS)]

    def get_agree_terms(self) -> WebElement:
        return Waiter.found(self.driver, OrderPageLocators.PAYMENT_AGREE)

    def fill_personal_form(self, user: User) -> None:
        self.wait_personal()
        self.select_gender(user.gender)
        self.enter_name(user.name)
        self.enter_surname(user.surname)
        self.enter_email(user.email)
        self.enter_password(user.password)
        self.enter_birthday(user.birthday)
        self.next_personal()

    def fill_address_form(self, user: User) -> None:
        self.wait_address()
        self.enter_address(user.address)
        self.enter_postcode(user.postcode)
        self.enter_city(user.city)
        self.next_address()

    def choose_delivery_method(self, blacklist: Optional[List[str]] = None) -> None:
        blacklist = blacklist or []
        self.wait_delivery()
        method: DeliveryMethodWrapper = choice([method
                                                for method
                                                in self.get_delivery_methods()
                                                if method.name not in blacklist])
        Actions.click(self.driver, method.radio)
        self.next_delivery()

    def choose_payment_method(self, method: str) -> None:
        self.wait_payment()
        payment_method: List[PaymentMethodWrapper] = [m for m in self.get_payment_methods() if m.name == method]
        if payment_method:
            payment_method: PaymentMethodWrapper = payment_method.pop()
        else:
            raise ValueError(f"Payment method '{method}' is not among possible payment methods.")
        Actions.click(self.driver, payment_method.radio)
        Actions.click(self.driver, self.get_agree_terms())
        self.accept_payment()
