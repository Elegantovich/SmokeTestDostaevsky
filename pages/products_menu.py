from base.base_class import Base


class ProductsMenuPage(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)

    # Locators

    title = "//h1[@class='product__title']"

    # Getters

    def get_product_item(self, product):
        return self.get_object("//div[@class='catalog-list__item' "
                               f"and @data-name='{product}']")

    # Actions

    def click_product_item(self, product):
        self.get_product_item(product).click()
        print(f"click {product} in product menu")

    # Methods

    def select_product(self, product):
        self.move_to_item(self.get_product_item(product))
        self.click_product_item(product)
        self.assert_word(self.get_title(self.title), product)
