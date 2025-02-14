from base.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    CREATE_BUTTON = (By.XPATH, "//button[text()='Создать']")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Поиск по объявлениям']")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Найти']")
    FILTER_BUTTON = (By.XPATH, "//button[@id='menu-button-:rc:']")
    PRICE_FILTER = (By.XPATH, "//button[text()='Цена']")

    def open_create_advertisement(self):
        self.click_element(*self.CREATE_BUTTON)

    def search_advertisement(self, title):
        self.enter_text(*self.SEARCH_INPUT, title)
        self.click_element(*self.SEARCH_BUTTON)

