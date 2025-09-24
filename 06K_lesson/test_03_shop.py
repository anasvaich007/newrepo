from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService


def test_checkout_total():
    driver = webdriver.Firefox(
        service=FirefoxService(
            r"C:\Users\Nasvaychik\Desktop\obuchenie\автоматизация\geckodriver\geckodriver.exe"
        )
    )

    driver.maximize_window()
    wait = WebDriverWait(driver, 20)

    driver.get("https://www.saucedemo.com/")

    username_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
    username_input.send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    driver.find_element(By.ID, "first-name").send_keys("Анастасия")
    driver.find_element(By.ID, "last-name").send_keys("Ануфриева")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    total_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text

    expected_total = "Total: $58.29"
    assert total_text == expected_total, f"Ожидали {expected_total}, но получили {total_text}"

    driver.quit()
