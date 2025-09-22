from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

wait = WebDriverWait(driver, 90)

delay_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
delay_input.clear()
delay_input.send_keys("45")

btn_7 = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[contains(@class,'btn') and text()='7']")))
btn_plus = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='+']")))
btn_8 = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='8']")))
btn_eq = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='=']")))

btn_7.click()
btn_plus.click()
btn_8.click()
btn_eq.click()

screen = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

screen_element = driver.find_element(By.CSS_SELECTOR, "div.screen")
assert screen_element.text == "15"

driver.quit()
