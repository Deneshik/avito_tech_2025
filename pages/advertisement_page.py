from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from selenium.webdriver.common.by import By


class AdvertisementPage(BasePage):
    TITLE_INPUT = (By.XPATH, "//input[@placeholder='Название']")
    PRICE_INPUT = (By.XPATH, "//input[@placeholder='Цена']")
    DESCRIPTION_INPUT = (By.XPATH, "//input[@placeholder='Описание']")
    IMAGE_URL_INPUT = (By.XPATH, "//input[@placeholder='URL изображения']")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    EDIT_SAVE_BUTTON = (By.CSS_SELECTOR, "#root > div > div.chakra-container.css-1lle71m > div > div.css-nb383z > svg")
    NEW_PRICE_INPUT = (By.XPATH, "//input[@name='price']")
    OPEN_CREATE_PRODUCT = (By.XPATH, "//*[@id='root']/div/div[2]/div[5]/div[1]/a/div/img")
    ADVERTISEMENT_BUTTON_HEADER = (By.XPATH, "//div[text()='Объявления']")

    def create_advertisement(self, title, price, description, image_url):
        self.enter_text(*self.TITLE_INPUT, title)
        self.enter_text(*self.PRICE_INPUT, price)
        self.enter_text(*self.DESCRIPTION_INPUT, description)
        self.enter_text(*self.IMAGE_URL_INPUT, image_url)
        self.click_element(*self.SAVE_BUTTON)

    def edit_advertisement(self, new_price):
        self.click_element(*self.OPEN_CREATE_PRODUCT)
        self.click_element(*self.EDIT_SAVE_BUTTON)

        # Ждем появления поля ввода цены
        price_input = self.find_element(*self.NEW_PRICE_INPUT)
        price_input.clear()
        price_input.send_keys(new_price)

        # Сохранение изменений
        self.click_element(*self.EDIT_SAVE_BUTTON)

        # Переход к объявлениям
        self.click_element(*self.ADVERTISEMENT_BUTTON_HEADER)

