from base.base_class import Base


class ItemCardPage(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)

    # Locators

    button_add = "//div[@class='add-to-cart']"
    product_price = "//div[@class='product-price__value']"
    name_product = "//h1[@class='product__title']"
    cart = "//div[@class='catalog-cart__info']"
    title = "//div[@class='cart-header__item']"

    # Getters

    def get_button_add(self):
        return self.get_object(self.button_add)

    def get_price_field(self):
        return self.get_object(self.product_price)

    def get_cart(self):
        return self.get_object(self.cart)

    # Actions

    def click_button_add(self):
        self.get_button_add().click()
        print("click button add")

    def click_cart(self):
        self.get_cart().click()
        print("click cart")

    def get_price_value(self):
        int_price = int(self.get_dig(self.get_price_field().text))
        print(f"Цена: {int_price}")
        return int_price

    def get_name_value(self):
        str_name = self.get_title(self.name_product)
        print(f"Наименование: {str_name}")
        return str_name

    # Methods

    def add_to_carts(self):
        name = self.get_name_value()
        price = self.get_price_value()
        self.click_button_add()
        self.click_cart()
        self.assert_link("https://dostaevsky.ru/cart")
        return {name: price}