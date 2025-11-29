from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://www.saucedemo.com/'

def get_driver():

    #instalacion de driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)


    # time.sleep(5)
    driver.implicitly_wait(5)

    return driver