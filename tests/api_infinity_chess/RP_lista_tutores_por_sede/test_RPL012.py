import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger 

@pytest.mark.funtional
@pytest.mark.positive
def test_RPL012_obtener_tutor_por_sede_escrita_en_MAYUSCULAS_minusculas (get_url):
    logger.info("Iniciando Test Case RPL012")
    logger.info(get_url)
    endpoint = "obtenerTutores/MoDuLo 4"
    lista_url = get_url + endpoint
    logger.debug(lista_url)
    response = requests.get(lista_url)
    assert response.status_code == 200
    lista_tutores = response.json()
    assert len (lista_tutores) > 0
    logger.info(response.status_code)
    logger.info("Validando response")
    assert_validar_response_schema(response,cargar_schema("schema_tutores_sede.json"))