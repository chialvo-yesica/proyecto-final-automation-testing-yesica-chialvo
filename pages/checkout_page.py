from selenium.webdriver.common.by import By
from pages.base_page import SeleniumBasePage

#Representa las pantallas del flujo de checkout de SauceDemo
class SauceCheckoutPage(SeleniumBasePage):

    # Paso 1: formulario de información del cliente
    CAMPO_NOMBRE = (By.ID, "first-name")
    CAMPO_APELLIDO = (By.ID, "last-name")
    CAMPO_ZIP = (By.ID, "postal-code")
    BOTON_CONTINUAR = (By.ID, "continue")

    # Paso 2: overview y botón finalizar
    BOTON_FINALIZAR = (By.ID, "finish")

    # Paso 3: confirmación de compra
    TITULO_ORDEN_COMPLETADA = (By.CSS_SELECTOR, "[data-test='complete-header']")

    #Completa el formulario de información del cliente en el paso 1 del checkout
    def fill_client_data(self, nombre: str, apellido: str, codigo_postal: str):
        self.enter_text(*self.CAMPO_NOMBRE, text=nombre)
        self.enter_text(*self.CAMPO_APELLIDO, text=apellido)
        self.enter_text(*self.CAMPO_ZIP, text=codigo_postal)

    #Hace clic en el botón 'Continue' 
    def click_continue_button(self):
        self.click_on(*self.BOTON_CONTINUAR)

    #Hace clic en el botón 'Finish'
    def click_finish_button(self):
        self.click_on(*self.BOTON_FINALIZAR)

    #Verifica que se muestre el mensaje de orden completada
    def is_order_confirmation_visible(self) -> bool:
        return self.is_present_on_screen(*self.TITULO_ORDEN_COMPLETADA)

    #Devuelve el texto del mensaje de completado de la orden
    def get_confirmation_message(self) -> str:
        return self.retrieve_element_text(*self.TITULO_ORDEN_COMPLETADA)