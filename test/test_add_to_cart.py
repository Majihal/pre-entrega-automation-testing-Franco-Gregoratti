import pytest
import time
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage

def test_add_backpack_to_cart(driver):

    loginPage = LoginPage(driver)
    loginPage.open()
    loginPage.login("standard_user", "secret_sauce")
    time.sleep(4)

    inventoryPage = InventoryPage(driver)
    inventoryPage.add_first_n_products(2)   
    inventoryPage.go_to_cart()
    time.sleep(4)

    cartPage = CartPage(driver)
    assert len(cartPage.get_items()) > 0
    time.sleep(5)