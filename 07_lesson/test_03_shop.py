from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.shop_login_page import ShopLoginPage
from pages.shop_products_page import ShopProductsPage
from pages.shop_cart_page import ShopCartPage
from pages.shop_checkout_page import ShopCheckoutPage


def test_checkout_total():
    driver = webdriver.Firefox(
        service=FirefoxService(
            r"C:\Users\Nasvaychik\Desktop\obuchenie\автоматизация\geckodriver\geckodriver.exe")
    )
    driver.maximize_window()

    login_page = ShopLoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ShopProductsPage(driver)
    products_page.add_backpack()
    products_page.add_tshirt()
    products_page.add_onesie()
    products_page.go_to_cart()

    cart_page = ShopCartPage(driver)
    cart_page.checkout()

    checkout_page = ShopCheckoutPage(driver)
    checkout_page.fill_user_data("Анастасия", "Ануфриева", "12345")

    total = checkout_page.get_total()

    assert total == "Total: $58.29"

    driver.quit()
