import pytest
# Renombré las clases para coincidir con las definiciones en tus archivos pages/
from pages.login_page import SauceLoginPage
from pages.inventory_page import ProductsInventoryPage 
from pages.cart_page import ProductsCartPage 
from pages.checkout_page import SauceCheckoutPage 


@pytest.mark.ui
@pytest.mark.validation_fail
def test_purchase_fails_due_to_missing_first_name(web_driver):
    """
    Caso de prueba diseñado para FALLAR y generar un screenshot.
    
    Escenario: Intentar completar el formulario de Checkout sin ingresar el Nombre (First Name).
    - La aplicación mostrará un mensaje de error de validación.
    - El test fallará intencionalmente al ASUMIR que la compra fue exitosa.
    - Al fallar el test, Pytest debería generar la captura de pantalla del error.
    """
    # Usar las clases correctamente nombradas:
    login_page = SauceLoginPage(web_driver)
    inventory_page = ProductsInventoryPage(web_driver)
    cart_page = ProductsCartPage(web_driver)
    checkout_page = SauceCheckoutPage(web_driver)

    # 1. Login y navegar al carrito
    login_page.access_login_page()
    login_page.authenticate_user("standard_user", "secret_sauce")
    
    # 2. Agregar un producto y navegar al checkout
    inventory_page.add_backpack_to_cart() 
    inventory_page.go_to_shopping_cart() 
    cart_page.go_to_checkout()           

    # 3. Llenar información de Checkout (ERROR: DEJAMOS EL NOMBRE VACÍO)
    checkout_page.fill_client_data(       
        nombre="",                        # El fallo de validación real (Missing First Name)
        apellido="Test Fallido",
        codigo_postal="12345"
    )
    checkout_page.click_continue_button()
    
    # 4. VERIFICACIÓN INTENCIONALMENTE ERRÓNEA (PUNTO DE FALLO)
    
    # Intentamos verificar que se muestra el mensaje de ORDEN COMPLETADA.
    # Esto FALLARÁ porque la aplicación se detuvo en el formulario de Checkout debido al error de validación.
    
    assert checkout_page.is_order_confirmation_visible(), \
        "FALLO INTENCIONAL: Se esperaba la página de éxito, pero falló la validación en Checkout. Screenshot adjunta en reports."