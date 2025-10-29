import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.shop_login_page import ShopLoginPage
from pages.shop_products_page import ShopProductsPage
from pages.shop_cart_page import ShopCartPage
from pages.shop_checkout_page import ShopCheckoutPage

@allure.title("Проверка итоговой суммы заказа")
@allure.description("Проверяем, что сумма на странице оформления совпадает с ожидаемой.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.BLOCKER)
def test_checkout_total():
    driver = webdriver.Firefox(
        service=FirefoxService(r"C:\Users\Nasvaychik\Desktop\obuchenie\автоматизация\geckodriver\geckodriver.exe")
    )
    driver.maximize_window()

    login_page = ShopLoginPage(driver)
    products_page = ShopProductsPage(driver)
    cart_page = ShopCartPage(driver)
    checkout_page = ShopCheckoutPage(driver)

    with allure.step("Авторизация"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров"):
        products_page.add_backpack()
        products_page.add_tshirt()
        products_page.add_onesie()
        products_page.go_to_cart()

    with allure.step("Оформление заказа"):
        cart_page.checkout()

    with allure.step("Заполнить данные покупателя"):
        checkout_page.fill_user_data("Анастасия", "Ануфриева", "12345")

    with allure.step("Проверка итоговой суммы"):
        total = checkout_page.get_total()
        assert total == "Total: $58.29"

    driver.quit()
