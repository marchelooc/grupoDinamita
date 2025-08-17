import pytest
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_a_eliminar
from src.api_infinity_chess.materia import eliminar_materia

@pytest.mark.negative
@pytest.mark.functional
def test_validar_comportamiento_al_eliminar_una_materia_sin_CODIGOCURSO(get_url):
    logger.info("Iniciando test MOCM033.")
    logger.debug("eliminando una materia sin pasar codigo de curso")
    response = eliminar_materia(get_url, "")
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 404
    logger.info("Test MOCM033 realizado.")
