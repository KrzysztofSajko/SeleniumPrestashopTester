from selenium.webdriver.common.by import By

from utility.myTypes import Locator


class BasePageLocators:
    TOP_MENU: Locator = (By.ID, "top-menu")
    CATEGORY: Locator = (By.CSS_SELECTOR, "a.dropdown-item")
    CATEGORY_CONTAINER: Locator = (By.CSS_SELECTOR, "#top-menu > li")
    CURRENT_CATEGORY_CONTAINER: Locator = (By.CSS_SELECTOR, "#top-menu > li.current")
    CART: Locator = (By.CSS_SELECTOR, "#_desktop_cart > div > div > a")
    UserAccount: Locator = (By.CSS_SELECTOR, "#_desktop_user_info > div > a.account")


class MainPageLocators:
    pass


class CategoryPageLocators:
    PRODUCT_LIST: Locator = (By.ID, "js-product-list")
    PRODUCT: Locator = (By.CLASS_NAME, "thumbnail-container")
    PRODUCT_NAME: Locator = (By.CSS_SELECTOR, ".product-description > h1")
    PRODUCT_LINK: Locator = (By.CSS_SELECTOR, ".product-image-block > a")


class ProductPageLocators:
    COUNTER: Locator = (By.ID, "quantity_wanted")
    SUBMIT: Locator = (By.CSS_SELECTOR, "#add-to-cart-or-refresh div.add > button")
    STOCK_SIZE: Locator = (By.CSS_SELECTOR, "#product-details > div.product-quantities > span")
    POPUP_SKIP: Locator = (By.CSS_SELECTOR, "#blockcart-modal div.cart-content-btn > button")
    POPUP_ACCEPT: Locator = (By.CSS_SELECTOR, "#blockcart-modal div.cart-content-btn > a")
    POPUP_CONTAINER: Locator = (By.CSS_SELECTOR, "#blockcart-modal")


class CartPageLocators:
    PRODUCT_LIST: Locator = (By.CSS_SELECTOR, "#main  ul.cart-items > li.cart-item")
    PRODUCT_NAME: Locator = (By.CSS_SELECTOR, "div.product-line-info > a")
    PRODUCT_DELETE: Locator = (By.CSS_SELECTOR,
                               "div.product-line-grid-right div.cart-line-product-actions > a.remove-from-cart")
    FINISH_BUTTON: Locator = (By.CSS_SELECTOR, "#main > div > div.cart-grid-right.col-xs-12.col-lg-4 > div.card.cart-summary > div.checkout.cart-detailed-actions.card-block > div > a")


class OrderPageLocators:
    PERSONAL_MR: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(1) > div.col-md-6.form-control-valign > label:nth-child(1) > span > input[type=radio]")
    PERSONAL_MRS: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(1) > div.col-md-6.form-control-valign > label:nth-child(2) > span > input[type=radio]")
    PERSONAL_NAME: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(2) > div.col-md-6 > input")
    PERSONAL_SURNAME: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(3) > div.col-md-6 > input")
    PERSONAL_EMAIL: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(4) > div.col-md-6 > input")
    PERSONAL_PASSWORD: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(6) > div.col-md-6 > div > input")
    PERSONAL_BIRTHDAY: Locator = (By.CSS_SELECTOR, "#customer-form > section > div:nth-child(7) > div.col-md-6 > input")
    PERSONAL_NEXT: Locator = (By.CSS_SELECTOR, "#customer-form > footer > button")

    ADDRESS_ADDRESS: Locator = (By.CSS_SELECTOR, "#delivery-address > div > section > div:nth-child(7) > div.col-md-6 > input")
    ADDRESS_POSTCODE: Locator = (By.CSS_SELECTOR, "#delivery-address > div > section > div:nth-child(9) > div.col-md-6 > input")
    ADDRESS_CITY: Locator = (By.CSS_SELECTOR, "#delivery-address > div > section > div:nth-child(10) > div.col-md-6 > input")
    ADDRESS_NEXT: Locator = (By.CSS_SELECTOR, "#delivery-address > div > footer > button")

    DELIVERY_METHODS: Locator = (By.CSS_SELECTOR, "#js-delivery div.delivery-option")
    DELIVERY_METHOD_NAME: Locator = (By.CSS_SELECTOR, "label span.carrier-name")
    DELIVERY_METHOD_RADIO: Locator = (By.CSS_SELECTOR, "input[type=radio]")
    DELIVERY_METHOD_NEXT: Locator = (By.CSS_SELECTOR, "#js-delivery > button")

    PAYMENT_METHODS: Locator = (By.CSS_SELECTOR, "#checkout-payment-step div.payment-options div.payment-option")
    PAYMENT_METHOD_NAME: Locator = (By.CSS_SELECTOR, "label > span")
    PAYMENT_METHOD_RADIO: Locator = (By.CSS_SELECTOR, "span > input[type=radio]")
    PAYMENT_AGREE: Locator = (By.CSS_SELECTOR, "#conditions-to-approve span.custom-checkbox > input[type=checkbox]")
    PAYMENT_ACCEPT: Locator = (By.CSS_SELECTOR, "#payment-confirmation button")


class ConfirmationPageLocators:
    BODY: Locator = (By.CSS_SELECTOR, "#order-confirmation")


class AccountPageLocators:
    OPTIONS_INFO: Locator = (By.CSS_SELECTOR, "#identity-link")
    OPTIONS_ADDRESS: Locator = (By.CSS_SELECTOR, "#addresses-link")
    OPTIONS_ORDER_HISTORY: Locator = (By.CSS_SELECTOR, "#history-link")
    OPTIONS_RECEIPTS: Locator = (By.CSS_SELECTOR, "#order-slips-link")


class OrderHistoryPageLocators:
    ORDER_TABLE: Locator = (By.CSS_SELECTOR, "#content > table")
    TABLE_ROWS: Locator = (By.CSS_SELECTOR, "#content > table > tbody > tr")
    ROW_ORDER_ID: Locator = (By.CSS_SELECTOR, "th")
    ROW_ORDER_DETAILS: Locator = (By.CSS_SELECTOR, "td.text-sm-center.order-actions > a:nth-child(1)")

    DIV_ORDER_CONTAINER: Locator = (By.CSS_SELECTOR, "#content > div.orders")
    DIV_ORDER: Locator = (By.CSS_SELECTOR, "#content > div.orders > div.order")
    DIV_ORDER_ID: Locator = (By.CSS_SELECTOR, "div.col-xs-10 > a > h3")
    DIV_ORDER_DETAILS: Locator = (By.CSS_SELECTOR, " div.col-xs-2.text-xs-right > div:nth-child(1) > a")


class HttpsPageLocators:
    ADVANCED: Locator = (By.CSS_SELECTOR, "#details-button")
    LINK: Locator = (By.CSS_SELECTOR, "#proceed-link")
