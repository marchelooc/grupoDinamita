import pytest
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_a_eliminar
from src.api_infinity_chess.materia import crear_materia, eliminar_materia

@pytest.mark.smoke
def test_validar_eliminación_exitosa_de_una_materia(get_url):
    logger.info("Iniciando test MOCM030.")
    logger.debug("creando curso para eliminar: Mecatronica con cod 2025MECA")   
    crear_materia(get_url, payload_materia_a_eliminar)
    logger.debug("eliminando Mecatronica con cod 2025MECA")
    response = eliminar_materia(get_url, "2025MECA")
    assert response.status_code == 200
    logger.info("Test MOCM030 realizado.")
