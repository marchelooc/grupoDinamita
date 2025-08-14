import requests
import pytest
import random
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import headers_json

@pytest.mark.functional
def test_obtener_materias_de_una_sede_con_header_de_tipo_json(get_url):
    logger.info("Iniciando test MOCM001.")
    logger.debug("sede seleccionada: Modulo 4")
    endpoint = "obtenerCursos/Modulo 4"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    response = requests.get(lista_url, headers=headers_json)
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_materias_sede.json")) 
    logger.info("Test MOCM001 realizado.")
    
