from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def get_products(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located(self._PRODUCTS)
        )

    def add_first_n_products(self, n):
        products = self.get_products()
        for i in range(min(n, len(products))):
            add_btn = products[i].find_element(By.TAG_NAME, "button")
            add_btn.click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._CART_BUTTON)
        ).click()

    def get_cart_badge_number(self):
        badge = self.driver.find_elements(*self._CART_BADGE)
        return badge[0].text if badge else "0"
