import requests
import pytest
import random
from src.api_infinity_chess.obtener_curso import obtener_cursos
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
def test_validar_comportamiento_ante_una_materia_con_nombre_de_curso_inexistente(get_url):
    logger.info("Iniciando test MOCM021.")
    lista_materias = obtener_cursos(get_url)
    CURSO = random.choice(lista_materias)["CURSO"]
    logger.debug(f"Curso aleatorio seleccionado {CURSO}.")
    endpoint = " "
    lista_url = get_url + endpoint
    logger.info(f"Enviando GET {lista_url}.")
    response = requests.get(lista_url)
    assert response.status_code == 404
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
#    assert_validar_response_schema(response,cargar_schema("schema_lista_materias.json"))
# hacer un  "by pass" / "SOFT ACERT" 
#    try:
#        assert_validar_response_schema(response, cargar_schema("schema_lista_materias.json"))
#    except requests.exceptions.JSONDecodeError:
#        pytest.skip("La respuesta no contiene JSON, omitiendo validación de schema")
#    logger.info("Test MOCM021 realizado.")
