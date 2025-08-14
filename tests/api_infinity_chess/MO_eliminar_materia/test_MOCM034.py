import pytest
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_a_eliminar, headers_json
from src.api_infinity_chess.materia import crear_materia, eliminar_materia_con_header

@pytest.mark.smoke
def test_validar_comportamiento_al_eliminar_una_materia_con_header_json(get_url):
    logger.info("Iniciando test MOCM034.")
    logger.debug("creando curso para eliminar: Mecatronica con cod 2025MECA")   
    crear_materia(get_url, payload_materia_a_eliminar)
    logger.debug("eliminando Mecatronica con cod 2025MECA")
    response = eliminar_materia_con_header(get_url, "2025MECA", headers_json)
    assert response.status_code == 200
    logger.info("Test MOCM034 realizado.")