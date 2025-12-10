import pytest
from pages.login_page import SauceLoginPage
from pages.inventory_page import ProductsInventoryPage
from pages.cart_page import ProductsCartPage

# Credenciales
STANDARD_LOGIN = "standard_user"
SAUCE_PASSWORD = "secret_sauce"


@pytest.mark.ui
def test_add_product_verifies_cart_content(web_driver):
    """
    Caso de prueba:
    1. Login con credenciales válidas
    2. Agregar un producto (Sauce Labs Backpack) al carrito
    3. Verificar que el producto correcto esté en el carrito
    """
    login_page = SauceLoginPage(web_driver)
    inventory_page = ProductsInventoryPage(web_driver)
    cart_page = ProductsCartPage(web_driver)

    # 1) Abrir la página de login y autenticarse
    login_page.access_login_page()
    login_page.authenticate_user(username=STANDARD_LOGIN, password=SAUCE_PASSWORD)

    # 2) Verificamos que la página de inventario está cargada
    assert inventory_page.is_inventory_displayed(), "No se pudo acceder a la página de inventario después del login."

    # 3) Agregar al carrito
    inventory_page.add_backpack_to_cart()

    # 4) Verificar que el carrito muestre '1' 
    badge_count = inventory_page.get_cart_badge_value()
    assert badge_count == 1, f"ERROR: El contador del carrito indica {badge_count}, se esperaba 1."

    # 5) Ir al carrito
    inventory_page.go_to_shopping_cart()

    # 6) Verificar la cantidad de productos
    assert cart_page.get_number_of_items() == 1, "El carrito no contiene la cantidad exacta de productos esperada."

    item_names = cart_page.get_list_of_item_names()
    # Assert 
    assert "Sauce Labs Backpack" in item_names, (
        f"ERROR: El producto clave 'Sauce Labs Backpack' no fue encontrado en el carrito. Items: {item_names}"
    )