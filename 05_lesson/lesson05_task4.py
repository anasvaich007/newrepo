from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
    )
driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(
    By.ID, "username"
    ).send_keys("tomsmith")
driver.find_element(
    By.ID, "password"
    ).send_keys("SuperSecretPassword!")

sleep(2)

driver.find_element(
    By.CSS_SELECTOR, "button.radius"
    ).click()

sleep(2)

success_message = driver.find_element(
    By.CSS_SELECTOR, "div.flash.success"
    ).text
print(success_message.strip())

sleep(5)

driver.quit()
