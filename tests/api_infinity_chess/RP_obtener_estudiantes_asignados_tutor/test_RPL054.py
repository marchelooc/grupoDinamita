import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_estudiantes_tutor import enviar_solicitud

@pytest.mark.functional
@pytest.mark.smoke
def test_RPL054_obtener_estudiantes_cuando_CODTUTOR_es_igual_CODESTUDIANTE (get_url):
    logger.info("Iniciando Test Case RPL054")
    response = enviar_solicitud(get_url, "20231227GUSHER")
    assert response.status_code == 200
    lista_tutores = response.json()
    assert len (lista_tutores) > 0
    logger.debug(response.json())
    logger.info(response.status_code)
    logger.info("Validando response")
    assert_validar_response_schema(response,cargar_schema("schema_estudiante_tutor.json"))