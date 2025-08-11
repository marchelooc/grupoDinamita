import requests
import pytest
from src.utils.response_500 import response_500
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
def test_validar_que_se_recuperen_la_materia_con_nombre_inexistente(get_url):
    endpoint = "verificarCurso/" + "CURSOInexistente"
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    response = requests.get(lista_url)
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    respuestaJSON = response.json()
    assert len(respuestaJSON) == 0
    logger.info(f"Contenido de la lista = {len(respuestaJSON)}.")
    logger.info("Validando schema del response")
    assert_validar_response_schema(response,cargar_schema("schema_lista_materias.json")) 
    logger.info("Test MOCM017 realizado.")
