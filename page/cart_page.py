from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    _CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver

    def get_items(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located(self._CART_ITEMS)
        )

    def item_in_cart(self, item_name):
        items = self.get_items()

        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text

            if title.strip().lower() == item_name.strip().lower():
                return True

        return False
