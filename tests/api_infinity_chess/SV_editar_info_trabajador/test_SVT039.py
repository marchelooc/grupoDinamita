import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_con_campos_vacios
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_intentar_actualizar_datos_sin_enviar_un_campo_obligatorio_en_el_body_del_JSON (get_url):
    logger.info("Iniciando de test SVT039.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_con_campos_vacios(trabajador)
    logger.debug(payload)
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    assert response.status_code == 409
    logger.info("Test completado.")