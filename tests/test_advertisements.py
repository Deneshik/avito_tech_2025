from selenium.webdriver.common.by import By
from pages.advertisement_page import AdvertisementPage
from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_create_advertisement(driver):
    main_page = MainPage(driver)
    main_page.open_create_advertisement()

    ad_page = AdvertisementPage(driver)
    ad_page.create_advertisement(
        title="iPhone 12 128GB",
        price="50000",
        description="Продаю iPhone 12 белого цвета",
        image_url="https://technolove.ru/upload/iblock/aa7/orig_3.png"
    )

    assert "iPhone 12 128GB" in driver.page_source, "Объявление не создано!"


def test_search_advertisement(driver):
    main_page = MainPage(driver)
    main_page.search_advertisement("iPhone 12")

    assert "iPhone 12" in driver.page_source, "Поиск не работает!"


def test_edit_advertisement(driver):
    ad_page = AdvertisementPage(driver)
    ad_page.edit_advertisement(new_price="55000")

    # Ожидаем появления нового значения цены на странице
    price_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[text()='55000']"))
    )

    # Проверяем, что новая цена установлена в поле
    assert "55000" in price_input.text, "Измененная цена не отображается!"

