import pytest
from src.api_infinity_chess.materia import verificar_curso_nombre
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.functional
def test_validar_comportamiento_ante_una_materia_con_nombre_de_curso_inexistente(get_url):
    logger.info("Iniciando test MOCM021.")
    response = verificar_curso_nombre("", get_url)
    logger.debug(f"ESTE ES EL RESPONSE {response}.")
    assert response.status_code == 404
    logger.debug(f"Código de respuesta: {response.status_code}.")
    logger.info("Test MOCM021 realizado.")
