import pytest
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajador_aleatorio, enviar_POST_para_GET
from src.utils.logger_config import logger

@pytest.mark.negative
def test_obtener_trabajador_usando_POST_en_lugar_de_GET(get_url):
    logger.info("Inicio de test SVT020.")
    logger.info("Obtener un trabajador existente aleatorio.")
    CODTRABAJADOR = obtener_trabajador_aleatorio (get_url)
    logger.debug(f"Trabajador elegido: {CODTRABAJADOR}.")
    response = enviar_POST_para_GET (get_url, CODTRABAJADOR)
    logger.info(f"Código de respuesta: {response.status_code}.")
    assert response.status_code == 405
    logger.info("Test completado.")
