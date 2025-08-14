import pytest
from src.api_infinity_chess.eliminar_trabajador import enviar_DELETE_con_URL_inexistente
from src.api_infinity_chess.obtener_trabajadores import obtener_codigo_de_trabajador
from src.utils.logger_config import logger

@pytest.mark.negative
def test_verificar_que_el_endpoint_mal_escrito_retorne_un_error_404 (get_url):
    logger.info("Iniciando test SVT049.")
    response = enviar_DELETE_con_URL_inexistente (get_url, obtener_codigo_de_trabajador(get_url))
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 404
    logger.info("Test completado.")