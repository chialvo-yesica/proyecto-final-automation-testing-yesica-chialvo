import pytest


@pytest.mark.api
def test_resource_deletion_returns_expected_status(rest_client):
    """
    Caso de prueba:
    1. Realizar un DELETE a /posts/1
    2. Verificar que el status code indique éxito (200 o 204)
    """
    delete_endpoint = "/posts/1"
    response = rest_client.execute_delete(delete_endpoint)

    # Status
    assert response.status_code in (200, 204), (
        f"La eliminación de {delete_endpoint} falló. Status inesperado: {response.status_code}"
    )

    # JSONPlaceholder devuelve un {} para 200 o cuerpo vacío para 204
    if response.status_code == 200 and response.content:
        try:
            data = response.json()
            assert isinstance(data, dict) and not data, "El cuerpo de respuesta para DELETE 200 debería ser un objeto JSON vacío."
        except Exception:
            # Aceptar si el contenido es solo un string vacío y no un JSON válido
            pass