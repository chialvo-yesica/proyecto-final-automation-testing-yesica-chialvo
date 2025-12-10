import pytest
from pages.login_page import SauceLoginPage
from pages.inventory_page import ProductsInventoryPage

# Credenciales
USER_OK = "standard_user"
PASSWORD_OK = "secret_sauce"


@pytest.mark.ui
def test_successful_login_redirects_to_inventory(web_driver):
    """
    Caso de prueba:
    1. Abrir la página de login
    2. Iniciar sesión con credenciales válidas
    3. Verificar que se muestra la página de inventario
    """
    login_page = SauceLoginPage(web_driver)
    inventory_page = ProductsInventoryPage(web_driver)

    # 1) Abrir la página de login
    login_page.access_login_page()

    # 2) Hacer login con usuario válido
    login_page.authenticate_user(username=USER_OK, password=PASSWORD_OK)

    # 3) Verificar que se abrió la página de inventario 
    assert inventory_page.is_inventory_displayed(), "Fallo: La vista de productos no cargó, la autenticación no fue exitosa."
    assert inventory_page.get_page_header_text().lower() == "products", "Fallo: El encabezado principal no es 'Products'."