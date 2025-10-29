from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        self.wait = WebDriverWait(self.driver, 90)

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, value):
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, value):
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[text()='{value}']"))).click()

    def get_result(self):
        screen = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.screen")))
        return screen.text