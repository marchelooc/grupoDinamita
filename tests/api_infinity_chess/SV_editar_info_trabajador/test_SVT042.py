import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_validar_que_se_devuelva_codigo_200_al_actualizar_datos_correctamente (get_url):
    logger.info("Iniciando de test SVT042.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar(trabajador)
    logger.debug(payload)
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    assert response.status_code == 200
    logger.info("Test completado.")