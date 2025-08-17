import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_tutores import enviar_solicitud, verificar_tutores_activos

@pytest.mark.functional
def test_solicitud_sin_headers(get_url):
    logger.info("Iniciando test SSL006.")
    headers = {
    }
    response = enviar_solicitud(get_url,headers)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.debug(f"Response: {response.json()}")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
    lista_tutores = response.json()
    logger.info("Validando lista tutores activos.")
    verificar_tutores_activos(lista_tutores)
    logger.info("Test completado.")