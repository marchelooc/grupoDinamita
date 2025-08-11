import pytest
from src.utils.logger_config import logger
from src.api_infinity_chess.obtener_estudiantes import enviar_solicitud

@pytest.mark.negative
def test_solicitud_sin_codestudiante(get_url):
     logger.info("Iniciando test SSL032.")
     logger.info("Sin CODESTUDIANTE.")
     response = enviar_solicitud(get_url,"")
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 404
     logger.info("Test completado.")