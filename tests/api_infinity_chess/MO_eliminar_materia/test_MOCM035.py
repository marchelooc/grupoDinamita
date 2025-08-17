import pytest
from src.api_infinity_chess.materia import crear_materia, eliminar_materia_con_header
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_a_eliminar, headers_text
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema

@pytest.mark.functional
def test_validar_comportamiento_al_eliminar_una_materia_con_header_text(get_url):
    logger.info("Iniciando test MOCM035.")
    logger.debug("creando curso para eliminar: Mecatronica con cod 2025MECA")   
    crear_materia(get_url, payload_materia_a_eliminar)
    logger.debug("eliminando Mecatronica con cod 2025MECA")
    response = eliminar_materia_con_header(get_url, "2025MECA", headers_text)
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 200
    logger.info("Validando schema del response")
    assert_validar_response_schema(response,cargar_schema("schema_eliminar_materia.json")) 
    logger.info("Test MOCM035 realizado.")