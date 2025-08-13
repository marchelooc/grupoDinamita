import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_estudiantes_tutor import enviar_solicitud

@pytest.mark.functional
@pytest.mark.smoke
def test_RPL051_obtener_estudiantes_sin_enviar_CODTUTOR_en_URL (get_url):
    logger.info("Iniciando Test Case RPL051")
    response = enviar_solicitud(get_url, "")
    assert response.status_code == 404
    lista_tutores = response.json()
    assert len (lista_tutores) > 0
    logger.debug(response.json())
    logger.info(response.status_code)
    logger.info("Validando response")
    assert_validar_response_schema(response,cargar_schema("schema_estudiante_tutor.json"))