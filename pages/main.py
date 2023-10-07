from base.base_class import Base
from utilites.logger import Logger
from selenium.common.exceptions import ElementClickInterceptedException
import allure


@allure.epic("Операции на главной странице")
class MainPage(Base):

    def __init__(self, driver) -> None:
        super().__init__(driver)

    # Locators

    title = "//div[@class='title']"
    warning_button = ("//div[@class='info-button']/"
                      "button[contains(string(.), 'Понятно')]")
    select_city_button = "//aside//button[contains(string(.), 'Да')]"

    # Getters

    def get_menu_option(self, menu_item):
        return self.get_object(f"//li/a[@data-title='{menu_item}']")

    def get_warning_button(self):
        return self.get_object(self.warning_button, 3)

    def get_city_button(self):
        return self.get_object(self.select_city_button, 3)

    # Actions

    def click_menu_option(self, menu_item):
        self.get_menu_option(menu_item).click()
        print(f"click {menu_item} option in menu")

    def click_warning_button(self):
        self.get_warning_button().click()
        print("click warning button")

    def click_city_button(self):
        self.get_city_button().click()
        print("click city button")

    # Methods
    def select_menu_item(self, menu_item):
        try:
            with allure.step("Выбор опции м меню"):
                Logger.add_start_step(self.select_menu_item.__name__)
                self.driver.get(self.url)
                self.driver.maximize_window()
                self.get_current_url()
                try:
                    self.click_city_button()
                    self.click_warning_button()
                except ElementClickInterceptedException:
                    pass
                self.move_to_item(self.get_menu_option(menu_item))
                self.click_menu_option(menu_item)
                self.assert_word(self.get_title(self.title), menu_item)
                Logger.add_end_step(self.get_current_url(),
                                    self.select_menu_item.__name__)
        except Exception as error:
            self.screenshot()
            print(f"Ошибка :( - {error}")
