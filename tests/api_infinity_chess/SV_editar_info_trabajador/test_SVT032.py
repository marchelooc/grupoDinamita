import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar_fecha_mayor
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_actualizar_la_fecha_de_nacimiento_del_trabajador_a_una_fecha_mayor_de_75_años (get_url):
    logger.info("Iniciando de test SVT032.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar_fecha_mayor(trabajador)
    logger.debug(payload)
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    assert response.status_code == 409
    logger.info("Test completado.")