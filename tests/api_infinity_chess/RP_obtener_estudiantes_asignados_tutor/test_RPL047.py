import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_estudiantes_tutor import enviar_solicitud, validar_lista_un_estudiante

@pytest.mark.functional
def test_RPL047_obtener_estudiantes_de_un_tutor_con_un_solo_estudiante_asignado (get_url):
    logger.info("Iniciando Test Case RPL047")
    response = enviar_solicitud(get_url, "202418SOLARM")
    assert response.status_code == 200
    validar_lista_un_estudiante (response.json())
    logger.debug(f"response: {response.json()}")
    logger.info(response.status_code)
    logger.info("Validando response")
    assert_validar_response_schema(response,cargar_schema("schema_estudiante_tutor.json"))