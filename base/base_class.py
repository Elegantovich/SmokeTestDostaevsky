from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as dt, timedelta as add
from selenium.webdriver.common.action_chains import ActionChains
import re


class Base:
    def __init__(self, driver) -> None:
        self.driver = driver

    url = "https://dostaevsky.ru/"
    FORMAT = "%Y.%m.%d.%H.%M.%S"

    def get_current_url(self):
        """Method get current url"""
        url = self.driver.current_url
        print(f"current url: {url}")
        return url

    def get_object(self, xpath, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))

    def get_title(self, xpath):
        return self.get_object(xpath).text

    def get_dig(self, string):
        """Get digital from sting"""
        return re.findall(r"\d+", string)[0]

    def assert_word(self, word, result):
        """Method assert two values"""
        assert word.upper() == result.upper()
        print("Good value")

    def assert_link(self, link):
        """Method assert two link"""
        current_link = self.get_current_url()
        assert link == current_link
        print("Good link")

    def input_data(self, ui_object, value):
        ui_object.send_keys(value)
        print(f"input: {value}")

    def screenshot(self):
        """Getting screen"""
        path = ("../screen/"
                f"{(dt.utcnow() + add(hours=5)).strftime(self.FORMAT)}")
        self.driver.save_screenshot(f"./screen/{path}.png")

    def move_to_item(self, item):
        ActionChains(self.driver).move_to_element(item).perform()
