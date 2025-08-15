import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_contra_igual_a_nombre
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador_comp, enviar_PUT
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_actualizar_la_contraseña_a_una_nueva_contraseña_igual_al_nombre_del_trabajador (get_url):
    logger.info("Iniciando de test SVT037.")
    logger.info("Crear nuevo trabajador.")
    info = crear_trabajador_comp(get_url)
    trabajador = info.get("CODTRABAJADOR")
    nombre =  info.get("NOMBRETRABAJADOR")
    payload = crear_payload_para_contra_igual_a_nombre(nombre)
    logger.debug(payload)
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    assert response.status_code == 409
    logger.info("Test completado.")