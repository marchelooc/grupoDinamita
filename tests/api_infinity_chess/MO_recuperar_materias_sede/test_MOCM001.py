import pytest
from src.utils.logger_config import logger
from src.api_infinity_chess.materia import recuperar_cursos_sede

@pytest.mark.smoke
@pytest.mark.functional
def test_validar_obtención_de_todas_las_materias_de_una_sede(get_url):
    logger.info("Iniciando test MOCM001.")
    logger.debug("sede seleccionada: Modulo 4")
    response = recuperar_cursos_sede(get_url, "Modulo 4")
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 200
    logger.debug(f"Código de respuesta: {response.status_code}.")
    logger.info("Test MOCM001 realizado.")