import pytest
from src.api_infinity_chess.obtener_trabajadores import obtener_codigo_de_trabajador, enviar_GET_con_URL_inexistente
from src.utils.logger_config import logger

@pytest.mark.negative
def test_verificar_que_la_URL_incorrecta_retorne_error_404(get_url):
    logger.info("Inicio de test SVT004.")
    response = enviar_GET_con_URL_inexistente (get_url, obtener_codigo_de_trabajador(get_url))
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 404
    logger.info("Test completado.")