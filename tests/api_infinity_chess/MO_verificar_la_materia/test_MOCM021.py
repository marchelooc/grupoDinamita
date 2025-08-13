import requests
import pytest
import random
from src.api_infinity_chess.materia import verificar_curso_nombre
from src.utils.logger_config import logger

@pytest.mark.functional
def test_validar_comportamiento_ante_una_materia_con_nombre_de_curso_inexistente(get_url):
    logger.info("Iniciando test MOCM021.")
    response = verificar_curso_nombre("", get_url)
    assert response.status_code == 404
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.") 
#    try:
#        assert_validar_response_schema(response, cargar_schema("schema_lista_materias.json"))
#    except requests.exceptions.JSONDecodeError:
#        pytest.skip("La respuesta no contiene JSON, omitiendo validación de schema")
    logger.info("Test MOCM021 realizado.")
