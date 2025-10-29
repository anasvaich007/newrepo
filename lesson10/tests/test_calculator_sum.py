import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.calc_page import CalcPage

@allure.title("Проверка операции сложения в калькуляторе")
@allure.description("Проверяем, что при вводе 7 + 8 калькулятор отображает результат 15.")
@allure.feature("Онлайн-калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_sum():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    calc = CalcPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calc.open()

    with allure.step("Установить задержку"):
        calc.set_delay("45")

    with allure.step("Ввести 7 + 8 и нажать ="):
        calc.click_button("7")
        calc.click_button("+")
        calc.click_button("8")
        calc.click_button("=")

    with allure.step("Проверить результат"):
        WebDriverWait(driver, 90).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
        )
        result = calc.get_result()
        assert result == "15"

    driver.quit()
