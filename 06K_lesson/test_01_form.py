from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService

driver = webdriver.Edge(service=EdgeService(
    r"C:\Users\Nasvaychik\Desktop\obuchenie\автоматизация\msedgedriver\msedgedriver.exe"
    ))
driver.maximize_window()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

driver.find_element(By.NAME, "first-name").send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job-position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

wait = WebDriverWait(driver, 5)
zip_code = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
assert "alert-danger" in zip_code.get_attribute("class")

assert "alert-success" in driver.find_element(
    By.ID, "first-name").get_attribute("class")
assert "alert-success" in driver.find_element(
    By.ID, "last-name").get_attribute("class")
assert "alert-success" in driver.find_element(
    By.ID, "address").get_attribute("class")
assert "alert-success" in driver.find_element(
    By.ID, "e-mail").get_attribute("class")
assert "alert-success" in driver.find_element(
    By.ID, "phone").get_attribute("class")
assert "alert-success" in driver.find_element(
    By.ID, "city").get_attribute("class")
assert "alert-success" in driver.find_element(
    By.ID, "country").get_attribute("class")
assert "alert-success" in driver.find_element(
    By.ID, "job-position").get_attribute("class")
assert "alert-success" in driver.find_element(
    By.ID, "company").get_attribute("class")

driver.quit()
