import requests
import pytest
import random
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
def test_validar_obtención_de_todas_las_materias_de_sede_inexistente(get_url):
    logger.info("Iniciando test MOCM002.")
    logger.debug("sede seleccionada: SEDE NO EXISTE")
    endpoint = "obtenerCursos/Modulo 4"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    response = requests.get(lista_url)
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_vacio.json")) 
    logger.info("Test MOCM002 realizado.")
    
