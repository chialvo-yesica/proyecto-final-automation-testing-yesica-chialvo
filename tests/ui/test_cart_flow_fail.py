import pytest
from pages.login_page import SauceLoginPage
from pages.inventory_page import ProductsInventoryPage 
from pages.cart_page import ProductsCartPage 


@pytest.mark.ui
@pytest.mark.negative_inventory
def test_add_item_fails_for_error_user(web_driver):
    """
    Caso de prueba diseñado para FALLAR: Prueba que el 'error_user' 
    no puede agregar productos al carrito y verifica el fallo del test.
    
    Escenario: Login con 'error_user', intenta agregar 'Fleece Jacket', verifica el carrito.
    - El 'error_user' falla al cargar el inventario correctamente (aunque los botones existan).
    - El assert fallará al verificar el conteo del carrito (será 0, no 1).
    - El test fallido activa la captura de pantalla de la página de inventario defectuosa.
    """
    login_page = SauceLoginPage(web_driver)
    inventory_page = ProductsInventoryPage(web_driver)
    cart_page = ProductsCartPage(web_driver)
    
    # El conteo esperado (que sabemos que fallará)
    EXPECTED_ITEM_COUNT = 1
    
    # 1. Login con el usuario 'error_user' (Problemas de inventario)
    login_page.access_login_page()
    login_page.authenticate_user("error_user", "secret_sauce")
    
    # Verificamos que se haya accedido a la página de inventario
    inventory_page.is_inventory_displayed()
    
    # 2. Intentar agregar el producto 
    inventory_page.add_fleece_jacket_to_cart()
    
    # 3. Navegar al carrito
    inventory_page.go_to_shopping_cart()

    # 4. Verificación
    actual_item_count = cart_page.get_number_of_items()
    
    # Este assert fallará porque el conteo real será 0 (o no se encontrará el producto).
    assert actual_item_count == EXPECTED_ITEM_COUNT, (
        f"El carrito debería tener {EXPECTED_ITEM_COUNT} item, pero tiene {actual_item_count}. "
        f"El 'error_user' falló al agregar el producto. Screenshot adjunta."
    )