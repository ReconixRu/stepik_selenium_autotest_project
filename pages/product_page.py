from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        assert product_name.text == added_product_name.text, "Added product '{}' <> current product '{}'".format(added_product_name.text, product_name.text)

    def should_be_correct_basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text == basket_price.text, "Added product price '{}' <> current product price'{}'".format(basket_price.text, product_price.text)
