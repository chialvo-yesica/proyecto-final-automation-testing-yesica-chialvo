from selenium.webdriver.common.by import By
from pages.base_page import SeleniumBasePage

#Representa la página de carrito de SauceDemo
class ProductsCartPage(SeleniumBasePage):

    ELEMENTOS_CARRITO = (By.CLASS_NAME, "cart_item")
    NOMBRES_ITEMS = (By.CSS_SELECTOR, ".inventory_item_name")
    BOTON_CHECKOUT = (By.ID, "checkout")

    #Verifica que la página carrito esté cargada
    def is_cart_page_visible(self) -> bool:
        return self.is_present_on_screen(By.ID, "cart_contents_container")

    #Devuelve la cantidad de productos en carrito
    def get_number_of_items(self) -> int:
        elements = self.webdriver.find_elements(*self.ELEMENTOS_CARRITO)
        return len(elements)

    #Devuelve una lista con los nombres de los productos del carrito
    def get_list_of_item_names(self):
        elements = self.webdriver.find_elements(*self.NOMBRES_ITEMS)
        return [el.text for el in elements]

    #Hace click en checkout
    def go_to_checkout(self):
        self.click_on(*self.BOTON_CHECKOUT)