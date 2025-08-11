import pytest
from src.api_infinity_chess.crear_trabajador import enviar_POST_sin_body
from src.utils.response_500 import response_500
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG009: El sistema no responde correctamente a una solicitud POST sin body", run=True)
def test_crear_un_trabajador_sin_body_para_el_post (get_url):
    logger.info("Iniciando test SVT022.")
    logger.info("Realizar la solicitud POST sin body.")
    response = enviar_POST_sin_body (get_url)
    response_500(response)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 400
    logger.info("Test completado.")
