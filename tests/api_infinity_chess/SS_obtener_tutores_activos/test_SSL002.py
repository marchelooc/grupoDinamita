import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_tutores import enviar_solicitud, verificar_estructura_tutores

@pytest.mark.functional
def test_validar_estructura_de_respuesta(get_url):
    logger.info("Iniciando test SSL002.")
    response = enviar_solicitud(get_url)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.debug(f"Response: {response.json()}")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
    lista_tutores = response.json()
    logger.info("Validando estructura de tutores activos.")
    verificar_estructura_tutores(lista_tutores)
    logger.info("Test completado.")