import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_lista_tutores_sede import obtener_tutores_sede_con_formato_invalido

@pytest.mark.functional
@pytest.mark.positive
def test_RPL016_obtener_tutor_por_sede_con_formato_invalido (get_url):
    logger.info("Iniciando Test Case RPL016")
    logger.info(get_url)
    response = obtener_tutores_sede_con_formato_invalido (get_url)
    assert response.status_code == 404
    logger.info(response.status_code)
    logger.info("Validando response")