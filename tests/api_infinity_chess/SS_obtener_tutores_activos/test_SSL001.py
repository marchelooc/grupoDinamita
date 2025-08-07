import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_tutores import enviarSolicitud, verificar_tutores_activos

@pytest.mark.smoke
def test_obtener_lista_de_tutores_activos_correctamente(get_url):
    logger.info("Iniciando test SSL001.")
    response = enviarSolicitud(get_url)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_tutores.json"))
    lista_tutores = response.json()
    logger.debug(lista_tutores)
    logger.info("Validando lista tutores activos.")
    verificar_tutores_activos(lista_tutores)
