import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_contra_corta
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_actualizar_la_contraseña_a_una_nueva_contraseña_sin_caracteres_alfanumericos (get_url):
    logger.info("Iniciando de test SVT035.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_contra_corta(trabajador)
    logger.debug(payload)
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    assert response.status_code == 409
    logger.info("Test completado.")