import pytest
from src.utils.logger_config import logger
from src.api_infinity_chess.materia import recuperar_cursos_sede

@pytest.mark.negative
@pytest.mark.functional
def test_validar_comportamiento_al_recuperar_cursos_de_sede_sin_nombre(get_url):
    logger.info("Iniciando test MOCM003.")
    logger.debug("sede seleccionada: vacio")
    response = recuperar_cursos_sede(get_url, "")
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 404
    logger.debug(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    logger.info("Test MOCM003 realizado.")

    
