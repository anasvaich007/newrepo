from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService

def test_form_fields():
    driver = webdriver.Edge(service=EdgeService(
        r"C:\Users\Nasvaychik\Desktop\obuchenie\автоматизация\msedgedriver\msedgedriver.exe"
    ))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    fields_filling = {
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

    for locator, value in fields_filling.items():
        driver.find_element(By.NAME, locator).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait = WebDriverWait(driver, 5)
    zip_code = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_code.get_attribute("class")

    for locator in fields_filling.keys():
        assert "alert-success" in driver.find_element(
            By.ID, locator
        ).get_attribute("class")

    driver.quit()
