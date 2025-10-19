from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

URL = 'https://www.saucedemo.com/'
USSERNAME = 'standard_user'
PASSWORD =  'secret_sauce'


def get_driver ():
    #instalacion de driver
    options = Options ()
    options.add_argument('--start-maximized')



    service = Service (ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)


    return driver



def login_saucedemo(driver):
    driver.get(URL)
    time.sleep(3)
    #Ingresar las credenciales
    driver.find_element(By.NAME, 'user-name').send_keys (USSERNAME)
    driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
    driver.find_element(By.ID, 'login-button').click()
    time.sleep(3)


def validar_catalogo(driver):
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0
    return products