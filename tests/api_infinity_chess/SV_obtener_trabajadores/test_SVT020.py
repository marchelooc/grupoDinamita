import pytest
from src.api_infinity_chess.obtener_trabajadores import obtener_codigo_de_trabajador, enviar_POST_para_GET
from src.utils.logger_config import logger

@pytest.mark.negative
def test_obtener_trabajador_usando_POST_en_lugar_de_GET(get_url):
    logger.info("Inicio de test SVT020.")
    response = enviar_POST_para_GET (get_url, obtener_codigo_de_trabajador(get_url))
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 405
    logger.info("Test completado.")
