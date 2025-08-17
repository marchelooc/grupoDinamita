import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import headers_json
from src.api_infinity_chess.materia import obtener_nombre_materia_aleatoria, verificar_curso_nombre_con_header

@pytest.mark.functional
def test_agregar_una_materia_con_headers_de_tipo_json(get_url):
    logger.info("Iniciando test MOCM027.")
    CURSO = obtener_nombre_materia_aleatoria(get_url)
    logger.debug(f"Curso aleatorio seleccionado {CURSO}.")
    response = verificar_curso_nombre_con_header(CURSO, get_url, headers_json)
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 200
    logger.debug(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_materias.json")) 
    logger.info("Test MOCM027 realizado.")
    
