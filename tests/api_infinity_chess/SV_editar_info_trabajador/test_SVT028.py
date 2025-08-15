import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar_CODTRABAJADOR
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.utils.logger_config import logger

@pytest.mark.smoke
@pytest.mark.xfail(reason="Knwon issue SVBUG010: Se devuelve un codigo 200 indicando que se hizo el cambio", run=True)
def test_actualizar_el_CODTRABAJADOR_de_un_trabajador_existente (get_url):
    logger.info("Iniciando de test SVT027.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar_CODTRABAJADOR(trabajador)
    logger.debug(payload)
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    assert response.status_code == 409
    logger.info("Test completado.")