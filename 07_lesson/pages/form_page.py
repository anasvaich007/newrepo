from selenium.webdriver.common.by import By


class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self):
        self.driver.get(self.url)

    def fill_field(self, name, value):
        self.driver.find_element(By.NAME, name).send_keys(value)

    def submit(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']").click()

    def get_field_class(self, field_id):
        return self.driver.find_element(
            By.ID, field_id).get_attribute("class")
