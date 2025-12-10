import pytest


@pytest.mark.api
def test_retrieve_specific_resource_success(rest_client):
    """
    Caso de prueba:
    1. Realizar un GET a /posts/1
    2. Verificar que el status code sea 200
    3. Validar que la respuesta tenga la estructura esperada
    """
    post_id_to_check = "/posts/1"
    response = rest_client.execute_get(post_id_to_check)

    # Status 
    assert response.status_code == 200, (
        f"El status code para GET en {post_id_to_check} no fue 200. Obtenido: {response.status_code}"
    )

    # Estructura JSON 
    json_data = response.json()
    expected_keys = ["userId", "id", "title", "body"]
    for key in expected_keys:
        assert key in json_data, f"ERROR: La clave obligatoria '{key}' está ausente en el objeto JSON."

    # Tipos de datos básicos 
    assert isinstance(json_data["userId"], int), "El tipo de dato de 'userId' no es un entero."
    assert isinstance(json_data["title"], str), "El tipo de dato de 'title' no es un string."