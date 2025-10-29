import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import allure
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from pages.form_page import FormPage

@allure.title("Проверка заполнения формы и подсветки полей")
@allure.description("Тест проверяет, что корректные поля подсвечиваются зелёным, а поле zip-code — красным.")
@allure.feature("Форма регистрации")
@allure.severity(allure.severity_level.NORMAL)
def test_form_fields():
    driver = webdriver.Edge(
        service=EdgeService(r"C:\Users\Nasvaychik\Desktop\obuchenie\msedgedriver\msedgedriver.exe")
    )
    driver.maximize_window()
    page = FormPage(driver)

    with allure.step("Открыть страницу формы"):
        page.open()

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    with allure.step("Заполнить все поля формы"):
        for field, value in fields.items():
            page.fill_field(field, value)

    with allure.step("Отправить форму"):
        page.submit()

    with allure.step("Проверить поле zip-code"):
        assert "alert-danger" in page.get_field_class("zip-code")

    with allure.step("Проверить остальные поля"):
        for field in fields.keys():
            assert "alert-success" in page.get_field_class(field)

    driver.quit()
