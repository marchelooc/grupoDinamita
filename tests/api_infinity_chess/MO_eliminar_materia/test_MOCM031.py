import pytest
from src.utils.logger_config import logger
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.api_infinity_chess.materia import eliminar_materia

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=True)
def test_validar_comportamiento_al_eliminar_materia_inexistente(get_url):
    logger.info("Iniciando test MOCM031.")
    logger.debug("eliminando materia inexistente con cod 2030NOEXIST")
    response = eliminar_materia(get_url, "2030NOEXIST")
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 404
    logger.info("Validando schema del response")
    assert_validar_response_schema(response,cargar_schema("schema_eliminar_materia.json")) 
    logger.info("Test MOCM031 realizado.")