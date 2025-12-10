import pytest


@pytest.mark.api
def test_create_new_entity_with_post_method(rest_client):
    """
    Caso de prueba:
    1. Hacer un POST a /posts con un body simple
    2. Checkear si el status code es 201 
    3. Ver que la respuesta tenga los datos enviados y un id generado
    """
    payload_to_send = {
        "title": "Automation Test Post",
        "body": "This resource was created during automated testing.",
        "userId": 10,
    }
    post_endpoint = "/posts"

    response = rest_client.execute_post(post_endpoint, body=payload_to_send)

    # Status 
    assert response.status_code == 201, (
        f"El status code de creación no fue 201. Obtenido: {response.status_code}"
    )

    response_data = response.json()

    # Validar respuesta: los datos enviados deben estar presentes 
    for key, value in payload_to_send.items():
        assert key in response_data, f"ERROR: La clave '{key}' enviada no está en la respuesta."
        assert response_data[key] == value, (
            f"ERROR: El valor de '{key}' recibido no coincide. Esperado: {value}, Recibido: {response_data[key]}"
        )

    # Validar la generación de un nuevo id
    assert "id" in response_data and isinstance(response_data["id"], int), "ERROR: El recurso creado no contiene un 'id' numérico."