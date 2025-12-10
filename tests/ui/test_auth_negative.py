import pytest
from pages.login_page import SauceLoginPage
from utils.data_reader import load_test_data_from_json 

# Cargamos los datos de prueba desde el archivo JSON
ERROR_SCENARIOS = load_test_data_from_json("data/login_auth_errors.json")

@pytest.mark.ui
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        (item["login_id"], item["clave"], item["mensaje_esperado"])
        for item in ERROR_SCENARIOS
    ],
)
def test_login_validation_shows_correct_error(web_driver, username, password, expected_error):
    """
    Caso de prueba:
    1. Abrir la página de login
    2. Intentar iniciar sesión con credenciales inválidas
    3. Verificar que se muestre un mensaje de error adecuado
    """
    login_page = SauceLoginPage(web_driver)

    # 1) Abrir la página de login
    login_page.access_login_page()

    # 2) Intentar login con credenciales inválidas
    login_page.authenticate_user(username=username, password=password)

    # 3) Verificar que el mensaje de error es visible
    assert login_page.is_error_displayed(), "ERROR: La alerta de credenciales inválidas no fue visualizada."

    error_text = login_page.get_alert_error_message()

    # Assert
    assert expected_error in error_text, (
        f"El texto del mensaje de error no coincide con el caso de prueba.\n"
        f"Esperado (fragmento): '{expected_error}'\n"
        f"Recibido: '{error_text}'"
    )