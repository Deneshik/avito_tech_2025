import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")  # Запуск без UI (ускоряет тесты)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://tech-avito-intern.jumpingcrab.com/")
    yield driver
    driver.quit()


