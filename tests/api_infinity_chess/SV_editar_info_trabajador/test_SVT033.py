import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar_rol
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_actualizar_el_rol_a_uno_diferente_de_secretaria_o_maestro (get_url):
    logger.info("Iniciando de test SVT033.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar_rol(trabajador)
    logger.debug(payload)
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    assert response.status_code == 409
    logger.info("Test completado.")