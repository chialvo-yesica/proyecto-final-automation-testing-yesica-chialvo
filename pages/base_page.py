from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from config.settings import BASE_URL_WEB, TIMEOUT_PAGE_LOAD

# Clase base
class SeleniumBasePage:
    def __init__(self, driver: WebDriver):
        self.webdriver = driver
        self.site_url = BASE_URL_WEB

    #Navega a URL relativa al sitio base
    def go_to_url(self, endpoint: str = ""):
        url = self.site_url.rstrip("/") + "/" + endpoint.lstrip("/")
        self.webdriver.get(url)

    #Espera a que un elemento esté en el DOM y lo devuelve
    def find_element_present(self, by: By, locator: str, timeout: int = TIMEOUT_PAGE_LOAD):
        try:
            wait_manager = WebDriverWait(self.webdriver, timeout)
            return wait_manager.until(EC.presence_of_element_located((by, locator)))
        except TimeoutException as e:
            raise TimeoutException(f"El elemento {locator} no apareció en el DOM después de {timeout}s.") from e

    #Espera a que un elemento sea visible en la página y lo devuelve
    def find_element_visible(self, by: By, locator: str, timeout: int = TIMEOUT_PAGE_LOAD):
        try:
            wait_manager = WebDriverWait(self.webdriver, timeout)
            return wait_manager.until(EC.visibility_of_element_located((by, locator)))
        except TimeoutException as e:
            raise TimeoutException(f"El elemento {locator} no se hizo visible después de {timeout}s.") from e

    #Espera a que un elemento sea clickeable y hace click.
    def click_on(self, by: By, locator: str, timeout: int = TIMEOUT_PAGE_LOAD):
        wait_manager = WebDriverWait(self.webdriver, timeout)
        element = wait_manager.until(EC.element_to_be_clickable((by, locator)))
        element.click()

    #Ingresa texto en campo de entrada
    def enter_text(self, by: By, locator: str, text: str, timeout: int = TIMEOUT_PAGE_LOAD):
        element = self.find_element_visible(by, locator, timeout)
        element.clear()
        element.send_keys(text)

    #Obtiene el texto de un elemento
    def retrieve_element_text(self, by: By, locator: str, timeout: int = TIMEOUT_PAGE_LOAD) -> str:
        element = self.find_element_visible(by, locator, timeout)
        return element.text

    #Verifica si un elemento es visible en la página
    def is_present_on_screen(self, by: By, locator: str, timeout: int = 5) -> bool:
        try:
            # Buscamos presencia en DOM primero (más rápido), luego visibilidad
            element = self.find_element_present(by, locator, timeout=0.1) 
            if element.is_displayed():
                return True
            return False
        except (TimeoutException, NoSuchElementException):
            return False