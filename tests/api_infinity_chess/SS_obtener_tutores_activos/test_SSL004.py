import pytest
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_tutores import enviar_solicitud

@pytest.mark.functional
def test_verificación_del_código_de_respuesta(get_url):
    logger.info("Iniciando test SSL004.")
    response = enviar_solicitud(get_url)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 200
    logger.debug(f"Response: {response.json()}")
    logger.info("Test completado.")