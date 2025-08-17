import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_lista_tutores_sede import enviar_solicitud_sede

@pytest.mark.functional
@pytest.mark.positive
def test_RPL010_obtener_tutor_por_sede_invalida (get_url):
    logger.info("Iniciando Test Case RPL010")
    response = enviar_solicitud_sede(get_url, "ASDFJASDKNXCV")
    assert response.status_code == 200
    lista_tutores = response.json()
    assert len (lista_tutores) == 0
    logger.info(response.status_code)
    logger.info("Validando response")
    assert_validar_response_schema(response,cargar_schema("schema_tutores_sede.json"))