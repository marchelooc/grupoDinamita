import pytest
from src.api_infinity_chess.eliminar_trabajador import enviar_DELETE_con_URL_inexistente
from src.api_infinity_chess.obtener_trabajadores import obtener_trabajador_aleatorio
from src.utils.logger_config import logger

@pytest.mark.negative
def test_verificar_que_el_endpoint_mal_escrito_retorne_un_error_404 (get_url):
    logger.info("Iniciando test SVT049.")
    logger.info("Obtener un trabajador existente aleatorio.")
    CODTRABAJADOR = obtener_trabajador_aleatorio (get_url)
    logger.debug(f"Trabajador elegido: {CODTRABAJADOR}.")
    response = enviar_DELETE_con_URL_inexistente (get_url, CODTRABAJADOR)
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 404
    logger.info("Test completado.")


#Verificar que el endpoint mal escrito retorne un error 404