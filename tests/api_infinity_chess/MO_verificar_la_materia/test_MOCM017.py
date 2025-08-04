import requests
import pytest
import random
from src.api_infinity_chess.obtener_curso import obtener_cursos
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_validar_que_se_recuperen_la_materia_con_nombre_de_curso(get_url):
    logger.info("Iniciando test MOCM017.")
    lista_materias = obtener_cursos(get_url)
    CURSO = random.choice(lista_materias)["CURSO"]
    logger.debug(f"Curso aleatorio seleccionado {CURSO}.")
    endpoint = "verificarCurso/" + CURSO
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    response = requests.get(lista_url)
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_materias.json")) 
    logger.info("Test MOCM017 realizado.")
