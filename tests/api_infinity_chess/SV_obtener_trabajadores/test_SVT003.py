import pytest
from src.api_infinity_chess.obtener_trabajadores import enviar_GET_sin_CODTRABAJADOR
from src.utils.logger_config import logger

@pytest.mark.negative
def test_obtener_trabajador_sin_enviar_Id(get_url):
    logger.info("Inicio de test SVT003.")
    response = enviar_GET_sin_CODTRABAJADOR (get_url)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 404
    logger.info("Test completado.")