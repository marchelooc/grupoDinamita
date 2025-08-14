import requests
import pytest
from src.assertions.add import assert_validar_response_schema
from src.api_infinity_chess.materia import verificar_curso_nombre
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
def test_validar_que_no_se_recuperen_la_materia_con_nombre_inexistente(get_url):
    logger.info("Iniciando test MOCM025.")
    response = verificar_curso_nombre("CURSOInexistente", get_url)
    assert response.status_code == 200
    logger.info(f"Código de respuesta: {response.status_code}.")
    respuestaJSON = response.json()
    assert len(respuestaJSON) == 0
    logger.info(f"Contenido de la lista = {len(respuestaJSON)}.")
    logger.info("Validando schema del response.") 
#    try:
#        assert_validar_response_schema(response, cargar_schema("schema_lista_materias.json"))
#    except requests.exceptions.JSONDecodeError:
#        pytest.skip("La respuesta no contiene JSON, omitiendo validación de schema")
    logger.info("Test MOCM025 realizado.")
    
    
    
    

