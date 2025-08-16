import requests
import pytest
from src.api_infinity_chess.materia import obtener_nombre_materia_aleatoria, verificar_curso_nombre_con_header
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
def test_recuperar_una_materia_sin_headers(get_url):
    logger.info("Iniciando test MOCM026.")
    CURSO = obtener_nombre_materia_aleatoria(get_url)
    logger.debug(f"Curso aleatorio seleccionado {CURSO}.")
    response = verificar_curso_nombre_con_header(CURSO, get_url, {})
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_materias.json")) 
    logger.info("Test MOCM026 realizado.")
    
