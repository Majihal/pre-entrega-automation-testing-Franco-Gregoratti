import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
from utils.helpers import login_saucedemo, get_driver, validar_catalogo



@pytest.fixture
def driver():
    # Configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()



def test_login(driver):

    # logeo de usuario con username y password
    # Click al boton de login
    login_saucedemo(driver)

    #rediriga a la pagina inventario
    assert '/inventory.html' in driver.current_url
    
    #verificar el titulo de la pagina
    titulo = driver.find_element(By.CLASS_NAME, 'title').text
    assert titulo == 'Products'
    driver.save_screenshot("reports/capturas/redireccion_exitosa.png")
    time.sleep(3)

def test_catalogo(driver):  
   #indica si hay alguna card de los items de la lista
    products = validar_catalogo(driver)
    for producto in products:
        nombre = producto.find_element(By.CLASS_NAME, 'inventory_item_name').text
        precio = producto.find_element(By.CLASS_NAME, 'inventory_item_price').text

        # Imprimir para ver en consola
        print(f"Nombre: {nombre} | Precio: {precio}")


def test_carrito(driver):
    
    products = validar_catalogo(driver)

    # Si hay al menos 2 productos, agrega los dos primeros
    if len(products) >= 2:
        products[0].find_element(By.TAG_NAME, 'button').click()
        products[1].find_element(By.TAG_NAME, 'button').click()

        # Verifica que el carrito muestre '2'
        badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert badge == "2"
        driver.save_screenshot("reports/capturas/carrito_badge.png")
    #Revisar lo que hay dentro del carrito
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    driver.save_screenshot("reports/capturas/carrito_elementos.png")
    
    time.sleep(5)