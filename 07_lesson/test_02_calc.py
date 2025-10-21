from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.calc_page import CalcPage


def test_calculator_sum():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    calc = CalcPage(driver)
    calc.open()
    calc.set_delay("45")

    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")

    WebDriverWait(driver, 90).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div.screen"), "15"))
    result = calc.get_result()
    assert result == "15"

    driver.quit()
