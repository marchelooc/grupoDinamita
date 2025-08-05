import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger 

@pytest.mark.funtional
@pytest.mark.smoke
def test_RPL008_obtener_tutor_por_sede_valida (get_url):
    logger.info("Iniciando Test Case RPL008")
    logger.info(get_url)
    endpoint = "obtenerTutores/Modulo 4"
    lista_url = get_url + endpoint
    logger.debug(lista_url)
    response = requests.get(lista_url)
    assert response.status_code == 200
    lista_tutores = response.json()
    assert len (lista_tutores) > 0
    logger.debug(response.json())
    logger.info(response.status_code)
    logger.info("Validando response")
    assert_validar_response_schema(response,cargar_schema("schema_tutores_sede.json"))
