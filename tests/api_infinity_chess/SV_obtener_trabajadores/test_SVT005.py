import pytest
from src.api_infinity_chess.obtener_trabajadores import obtener_codigo_de_trabajador, enviar_GET, obtener_contraseña_trabajador
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.regression
def test_validar_que_la_contraseña_se_muestre_cifrada(get_url):
    logger.info("Inicio de test SVT005.")
    response = enviar_GET (get_url, obtener_codigo_de_trabajador(get_url))
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_obtener_trabajador.json"))
    info_contra = obtener_contraseña_trabajador(response)
    assert info_contra["CODTRABAJADOR"]
    logger.info("Test completado.")