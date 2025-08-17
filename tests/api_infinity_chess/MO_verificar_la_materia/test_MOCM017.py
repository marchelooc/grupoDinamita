import pytest
from src.api_infinity_chess.materia import obtener_nombre_materia_aleatoria, verificar_curso_nombre
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_validar_que_se_recuperen_la_materia_con_nombre_de_curso(get_url):
    logger.info("Iniciando test MOCM017.")
    CURSO = obtener_nombre_materia_aleatoria(get_url)
    logger.debug(f"Curso aleatorio seleccionado {CURSO}.")
    response = verificar_curso_nombre(CURSO, get_url)
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 200
    logger.debug(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_materias.json")) 
    logger.info("Test MOCM017 realizado.")
    
