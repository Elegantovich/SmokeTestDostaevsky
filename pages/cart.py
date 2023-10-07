from base.base_class import Base
from utilites.logger import Logger
import allure


@allure.epic("Операции в коризне")
class CartPage(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)

    # Locators

    product_price = "//p[@class='basket__product-price__value']"
    product_name = "//p[@class='basket__product-title']"

    # Getters

    def get_product_name(self):
        return self.get_object(self.product_name)

    def get_product_price(self):
        return self.get_object(self.product_price)

    # Actions

    def get_product_name_value(self):
        str_name = self.get_product_name().text
        print(f"get text of name: {str_name}")
        return str_name

    def get_price_value(self):
        int_price = int(self.get_dig(self.get_product_price().text))
        print(f"get price: {int_price}")
        return int_price

    # Methods

    def get_data_from_cart(self):
        with allure.step("Сверка в корзине"):
            Logger.add_start_step(self.get_data_from_cart.__name__)
            name = self.get_product_name_value()
            price = self.get_price_value()
            Logger.add_end_step(self.get_current_url(),
                                self.get_data_from_cart.__name__)
            return {name: price}
