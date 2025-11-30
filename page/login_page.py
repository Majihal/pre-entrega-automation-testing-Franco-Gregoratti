import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL
from selenium.webdriver.common.by import By


class LoginPage:

    _INPUT_NAME = (By.NAME, 'user-name')
    _INPUT_PASSWORD = (By.NAME, 'password')
    _LOGIN_BUTTON = (By.NAME, 'login-button')

    def __init__(self, driver):
        self.driver = driver

        # Logger LOCAL — cada clase puede tener el suyo
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)

    def open(self):
        self.logger.info(f"Abrir página de login: {URL}")
        self.driver.get(URL)

    def login(self, username, password):
        self.logger.info(f"Iniciando login con usuario: {username}")

        self.logger.info("Ingresando nombre de usuario...")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._INPUT_NAME)
        ).send_keys(username)

        self.logger.info("Ingresando contraseña...")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._INPUT_PASSWORD)
        ).send_keys(password)

        self.logger.info("Haciendo click en el botón de login")
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        ).click()

        self.logger.info("Login enviado")
