import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import TEST_BROWSER, WAIT_IMPLICIT, TIMEOUT_PAGE_LOAD

#Crea una instancia de WebDriver (Chrome) con configuraciones predefinidas.
def initialize_driver(is_headless: bool = False):
    browser_type = TEST_BROWSER.lower()

    if browser_type == "chrome":
        chrome_options = Options() 

        # Modo headless
        if is_headless or os.getenv("HEADLESS_MODE", "false").lower() == "true":
            chrome_options.add_argument("--headless=new")

        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        driver_instance = webdriver.Chrome(options=chrome_options)
    else:
        raise ValueError(f"ERROR: El navegador '{TEST_BROWSER}' no es compatible.")

    # Ajustes de tiempo
    driver_instance.implicitly_wait(WAIT_IMPLICIT)
    driver_instance.set_page_load_timeout(TIMEOUT_PAGE_LOAD)

    return driver_instance