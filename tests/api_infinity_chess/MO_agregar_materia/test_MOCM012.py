import requests
import pytest
from src.assertions.add import assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.api_infinity_chess.materia import existe_materia_repetida, crear_materia_repetida
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_repetida

@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=True)
def test_validar_comportamiento_al_agregar_curso_con_CODCURSO_duplicado(get_url):
    logger.info("Iniciando test MOCM012.")
    endpoint = "agregarCurso"
    logger.debug(f"este es el payload generado:{payload_materia_repetida}")
    if not existe_materia_repetida(get_url, "MateriaRepetida" ):
        logger.info("Creando materia repetida.")    
        crear_materia_repetida(get_url, endpoint)
    logger.info("Validando schema del input.")    
    assert_validar_schema_input(payload_materia_repetida,cargar_schema("schema_materias.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST {url_final}.")
    response = requests.post(url_final, json=payload_materia_repetida)
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 409
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Test MOCM012 realizado.")
    #assert_validarResponseSchema(response,cargar_schema("schema_materia.json")) 
    
