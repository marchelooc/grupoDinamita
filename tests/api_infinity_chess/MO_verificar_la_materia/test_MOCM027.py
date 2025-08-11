import requests
import pytest
import random
from src.api_infinity_chess.obtener_curso import obtener_cursos
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import headers_json

@pytest.mark.functional
def test_agregar_una_materia_con_headers_de_tipo_json(get_url):
    logger.info("Iniciando test MOCM026.")
    lista_materias = obtener_cursos(get_url)
    CURSO = random.choice(lista_materias)["CURSO"]
    logger.debug(f"Curso aleatorio seleccionado {CURSO}.")
    endpoint = "verificarCurso/" + CURSO
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    response = requests.get(lista_url, headers_json)
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_materias.json")) 
    logger.info("Test MOCM026 realizado.")
    
