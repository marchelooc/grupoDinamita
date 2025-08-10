import pytest
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajador_aleatorio, enviar_GET_con_URL_inexistente
from src.utils.logger_config import logger

@pytest.mark.negative
def test_verificar_que_la_URL_incorrecta_retorne_error_404(get_url):
    logger.info("Inicio de test SVT004.")
    logger.info("Obtener un trabajador existente aleatorio.")
    CODTRABAJADOR = obtener_trabajador_aleatorio (get_url)
    logger.debug(f"Trabajador elegido: {CODTRABAJADOR}.")
    response = enviar_GET_con_URL_inexistente (get_url, CODTRABAJADOR)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 404
    logger.info("Test completado.")