from selenium import webdriver
from pages.main import MainPage
from pages.item_card import ItemCardPage
from pages.products_menu import ProductsMenuPage
from pages.cart import CartPage
import configparser
import allure


@allure.epic("Тестовы епик")
@allure.title("Тестовый заголовок")
@allure.description("Тестируем покупку продукта в Достаевском")
def test_select_product(set_up):
    config = configparser.ConfigParser()
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    config.read("./data/config.ini", encoding='utf-8')
    path_drive = config["Config"]["driver_path"]
    driver = webdriver.Remote(command_executor=path_drive,
                              options=options)
    mp = MainPage(driver)
    mp.select_menu_item(config["Config"]["type_product"])
    pm = ProductsMenuPage(driver)
    pm.select_product(config["Config"]["name_product"])
    ic = ItemCardPage(driver)
    dict_result_1 = ic.add_to_carts()
    cart = CartPage(driver)
    dict_result_2 = cart.get_data_from_cart()
    for key in dict_result_1.keys():
        assert dict_result_1[key] == dict_result_2[key]
        print("Success")
        cart.screenshot()
    driver.quit()
