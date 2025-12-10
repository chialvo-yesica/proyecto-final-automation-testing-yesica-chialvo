import pytest
from pages.login_page import SauceLoginPage
from pages.inventory_page import ProductsInventoryPage
from pages.cart_page import ProductsCartPage
from pages.checkout_page import SauceCheckoutPage

# Credenciales
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.mark.ui
def test_end_to_end_purchase_completes(web_driver):
    """
    Caso de prueba:
    1. Login
    2. Agregar producto
    3. Checkout (Información y Finalizar)
    4. Verificar mensaje de confirmación
    """
    login_page = SauceLoginPage(web_driver)
    inventory_page = ProductsInventoryPage(web_driver)
    cart_page = ProductsCartPage(web_driver)
    checkout_page = SauceCheckoutPage(web_driver)

    # 1) Login
    login_page.access_login_page()
    login_page.authenticate_user(username=VALID_USERNAME, password=VALID_PASSWORD)
    assert inventory_page.is_inventory_displayed(), "Fallo en el paso de Login/Inventario."

    # 2) Agregar producto al carrito
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_badge_value() == 1, "El contador del carrito no está en 1."

    # 3) Ir al carrito y Checkout
    inventory_page.go_to_shopping_cart()
    cart_page.go_to_checkout()

    # 4) Completar información del cliente
    checkout_page.fill_client_data(
        nombre="Yesica",
        apellido="Chialvo",
        codigo_postal="1667",
    )
    checkout_page.click_continue_button()

    # 5) Finalizar compra
    checkout_page.click_finish_button()

    # 6) Verificar mensaje de confirmación 
    assert checkout_page.is_order_confirmation_visible(), "La pantalla de confirmación de compra no se mostró."
    confirmation_text = checkout_page.get_confirmation_message()
    assert "Thank you for your order" in confirmation_text, (
        f"El mensaje final esperado no fue encontrado. Mensaje real: '{confirmation_text}'"
    )