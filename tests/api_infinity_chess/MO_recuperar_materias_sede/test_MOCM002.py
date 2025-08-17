import pytest
from src.utils.logger_config import logger
from src.api_infinity_chess.materia import recuperar_cursos_sede

@pytest.mark.negative
@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=True)
def test_validar_obtención_de_todas_las_materias_de_sede_inexistente(get_url):
    logger.info("Iniciando test MOCM002.")
    logger.debug("sede seleccionada: SEDE NO EXISTE")
    response = recuperar_cursos_sede(get_url, "SEDE NO EXISTE")
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 404
    logger.debug(f"Código de respuesta: {response.status_code}.")
    logger.info("Test MOCM002 realizado.")
    
