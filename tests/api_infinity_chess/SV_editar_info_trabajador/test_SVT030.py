import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar_NOMBRETRABAJADOR
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_actualizar_el_nombre_y_apellido_de_un_trabajador_con_numeros (get_url):
    logger.info("Iniciando de test SVT030.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar_NOMBRETRABAJADOR(trabajador)
    logger.debug(payload)
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    assert response.status_code == 409
    logger.info("Test completado.")