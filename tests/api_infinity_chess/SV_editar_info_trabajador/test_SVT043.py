import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT_con_endpoint_mal_escrito
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_verificar_que_el_endpoint_mal_escrito_retorne_un_error_404 (get_url):
    logger.info("Iniciando de test SVT043.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar(trabajador)
    logger.debug(payload)
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT_con_endpoint_mal_escrito(get_url, payload, trabajador)
    assert response.status_code == 404
    logger.info("Test completado.")