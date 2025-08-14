import requests
import pytest
import random
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.materia import recuperar_cursos_sede

@pytest.mark.functional
def test_validar_obtención_de_todas_las_materias_de_sede_inexistente(get_url):
    logger.info("Iniciando test MOCM002.")
    logger.debug("sede seleccionada: SEDE NO EXISTE")
    response = recuperar_cursos_sede(get_url, "SEDE NO EXISTE")
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_lista_materias_sede.json")) 
    logger.info("Test MOCM002 realizado.")
    
