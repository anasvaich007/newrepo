from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
)

third_image_selector = "img:nth-of-type(3)"

WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element_attribute(
        (By.CSS_SELECTOR, third_image_selector), "src", ""
        )
)

third_img_src = driver.find_element(
    By.CSS_SELECTOR, third_image_selector).get_attribute("src")

print(third_img_src)

driver.quit()
