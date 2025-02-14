# avito_tech_2025

## Инструкция по запуску и тестированию

## 1. Установка и настройка окружения

Требования:

- Python 3.12+

- Google Chrome

- ChromeDriver (должен соответствовать версии Chrome)

- pip для управления пакетами


Клонируйте репозиторий:

  ```sh
git clone https://github.com/Deneshik/avito_tech_2025
  ```

Создайте и активируйте виртуальное окружение:
  ```sh
python -m venv venv
source venv/bin/activate  # Для macOS/Linux
venv\Scripts\activate     # Для Windows
  ```

Установите зависимости:
  ```sh
pip install -r requirements.txt
  ```
## 2. Запуск тестов

Тесты написаны с использованием pytest и selenium. Для их выполнения:
  ```sh
pytest tests/
  ```
## 3. Описание тестов

## 3.1. Файл TESTCASES.md

В файле TESTCASES.md содержатся основные тест-кейсы, которые проверяют:

Создание объявления

Редактирование объявления

Поиск объявлений

## 3.2. Автоматизированные тесты

Автотесты находятся в каталоге tests/:
  ```sh
test_advertisements.py — проверяет создание, редактирование и поиск объявлений.
  ```
Использует классы MainPage и AdvertisementPage из pages/ для удобного взаимодействия с UI.