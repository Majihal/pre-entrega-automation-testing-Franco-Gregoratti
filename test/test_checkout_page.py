import pytest
import os
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage


def test_checkout_flow(driver):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login("standard_user", "secret_sauce")
    time.sleep(3)

    inventoryPage = InventoryPage(driver)
    inventoryPage.add_first_n_products(2)
    time.sleep(2)
    inventoryPage.go_to_cart()
    time.sleep(3)

    cartPage = CartPage(driver)
    assert len(cartPage.get_items()) > 0
    time.sleep(2)

    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    checkoutPage = CheckoutPage(driver)
    checkoutPage.fill_information("Franco", "Gregoratti", "1000")
    time.sleep(3)
    checkoutPage.finish_checkout()
    time.sleep(3)

    assert checkoutPage.get_complete_message().lower() == "thank you for your order!".lower()
    time.sleep(4)


def test_checkout_invalid_zip(driver):
    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login("standard_user", "secret_sauce")
    time.sleep(2)

    inventoryPage = InventoryPage(driver)
    inventoryPage.add_first_n_products(1)
    inventoryPage.go_to_cart()
    time.sleep(2)


    cartPage = CartPage(driver)
    assert len(cartPage.get_items()) > 0
    time.sleep(2)


    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    checkoutPage = CheckoutPage(driver)
    checkoutPage.fill_information("Franco", "Gregoratti", "")
    time.sleep(2)


    os.makedirs("reports/screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"reports/screenshots/checkout_invalid_zip_{timestamp}.png")

    error_message = driver.find_elements(By.CLASS_NAME, "error-message-container")
    assert len(error_message) > 0, "Debe completar los campos faltantes"