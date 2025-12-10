from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import SeleniumBasePage

#Representa la página de inventario (productos) de SauceDemo
class ProductsInventoryPage(SeleniumBasePage):

    CONTENEDOR_PRODUCTOS = (By.ID, "inventory_container")
    TITULO_PAGINA = (By.CSS_SELECTOR, ".title")

    #Producto específico y botón
    BOTON_ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")

    #Icono del carrito
    ICONO_CARRITO = (By.ID, "shopping_cart_container")
    BADGE_CARRITO = (By.CSS_SELECTOR, ".shopping_cart_badge")

    #Verifica que la página de inventario esté cargada
    def is_inventory_displayed(self) -> bool:
        return self.is_present_on_screen(*self.CONTENEDOR_PRODUCTOS)

    #Devuelve el texto del título de la página
    def get_page_header_text(self) -> str:
        return self.retrieve_element_text(*self.TITULO_PAGINA)

    #Agrega el producto 'Sauce Labs Backpack' al carrito
    def add_backpack_to_cart(self):
        self.click_on(*self.BOTON_ADD_BACKPACK)

    #Hace clic en el icono del carrito
    def go_to_shopping_cart(self):
        self.click_on(*self.ICONO_CARRITO)

    #Devuelve la cantidad de productos mostrada en el badge del carrito
    def get_cart_badge_value(self) -> int:
        try:
            #Intentamos encontrar el elemento con una espera corta para evitar Timeout
            element = self.find_element_present(*self.BADGE_CARRITO, timeout=1) 
            text = element.text
            return int(text)
        except (TimeoutException, ValueError):
            #Si el elemento no está presente o el texto no es un número, se asume 0
            return 0