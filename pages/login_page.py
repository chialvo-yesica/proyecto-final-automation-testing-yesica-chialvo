from selenium.webdriver.common.by import By
from pages.base_page import SeleniumBasePage

#Representa la página de login de SauceDemo
class SauceLoginPage(SeleniumBasePage):

    # Localizadores
    CAMPO_USUARIO = (By.ID, "user-name")
    CAMPO_CLAVE = (By.ID, "password")
    BOTON_INICIAR_SESION = (By.ID, "login-button")
    CONTENEDOR_ALERTA = (By.CSS_SELECTOR, "[data-test='error']")

    #Abre la página de login
    def access_login_page(self):
        self.go_to_url("")

    #Realiza el proceso de login con las credenciales dadas
    def authenticate_user(self, username: str, password: str):
        self.enter_text(*self.CAMPO_USUARIO, text=username)
        self.enter_text(*self.CAMPO_CLAVE, text=password)
        self.click_on(*self.BOTON_INICIAR_SESION)

    #Devuelve el texto del mensaje de error mostrado en el login
    def get_alert_error_message(self) -> str:
        return self.retrieve_element_text(*self.CONTENEDOR_ALERTA)

    #Verifica si el mensaje de error está visible
    def is_error_displayed(self) -> bool:
        return self.is_present_on_screen(*self.CONTENEDOR_ALERTA)