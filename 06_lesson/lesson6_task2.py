from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://www.uitestingplayground.com/textinput")
search_field = "#newButtonName"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.clear()
search_input.send_keys("SkyPro")

driver.quit()
