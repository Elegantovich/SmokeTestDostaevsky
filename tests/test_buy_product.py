from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages.main import MainPage
from pages.item_card import ItemCardPage
from pages.products_menu import ProductsMenuPage
from pages.cart import CartPage
import configparser
import allure


@allure.description("Тестируем покупку продукта в Достаевском")
def test_select_product(set_up):
    config = configparser.ConfigParser()
    config.read("data\\config.ini", encoding='utf-8')
    path_drive = config["Config"]["driver_path"]
    driver = webdriver.Remote(path_drive, DesiredCapabilities.CHROME)
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
