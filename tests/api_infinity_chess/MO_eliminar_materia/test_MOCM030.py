import pytest
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import generar_materia_aleatoria
from src.api_infinity_chess.materia import crear_materia, eliminar_materia
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema

@pytest.mark.smoke
@pytest.mark.functional
def test_validar_eliminación_exitosa_de_una_materia(get_url):
    logger.info("Iniciando test MOCM030.")
    payload = generar_materia_aleatoria()
    logger.info(f"creando curso para eliminar: {payload['CURSO']}")   
    crear_materia(get_url, payload)
    logger.debug(f"eliminando {payload['CURSO']}")
    response = eliminar_materia(get_url, payload['CODCURSO'])
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 200
    logger.info("Validando schema del response")
    assert_validar_response_schema(response,cargar_schema("schema_eliminar_materia.json")) 
    logger.info("Test MOCM030 realizado.")