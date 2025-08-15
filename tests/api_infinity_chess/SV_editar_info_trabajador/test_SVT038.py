import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_POST_por_PUT
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_actualizar_los_datos_de_un_trabajador_usando_POST (get_url):
    logger.info("Iniciando de test SVT038.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar(trabajador)
    logger.debug(payload)
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_POST_por_PUT(get_url, payload)
    assert response.status_code == 404
    logger.info("Test completado.")