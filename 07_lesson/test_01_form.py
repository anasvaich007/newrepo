from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from pages.form_page import FormPage
from time import sleep


def test_form_fields():
    driver = webdriver.Edge(
        service=EdgeService(
            r"C:\Users\Nasvaychik\Desktop\obuchenie\msedgedriver\msedgedriver.exe"
        )
    )
    driver.maximize_window()

    page = FormPage(driver)
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

    for field, value in fields.items():
        page.fill_field(field, value)

    page.submit()

    assert "alert-danger" in page.get_field_class("zip-code")

    for field in fields.keys():
        assert "alert-success" in page.get_field_class(field)

    sleep(5)
    driver.quit()
