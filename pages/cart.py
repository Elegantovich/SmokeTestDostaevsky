from base.base_class import Base


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
        name = self.get_product_name_value()
        price = self.get_price_value()
        return {name: price}
