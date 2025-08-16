import pytest
from src.api_infinity_chess.obtener_trabajadores import obtener_codigo_de_trabajador_inexistente
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar
from src.api_infinity_chess.actualizar_trabajador import enviar_PUT
from src.assertions.add import assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
def test_intentar_actualizar_un_trabajador_con_un_CODTRABAJADOR_inexistente (get_url):
    logger.info("Iniciando de test SVT026.")
    logger.info("Crear nuevo CODTRABAJADOR inexistente.")
    trabajador = obtener_codigo_de_trabajador_inexistente()#precondicion
    payload = crear_payload_para_actualizar(trabajador)
    logger.debug(f"Payload para cambiar datos:{payload}.")
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_actualizar_trabajador.json"))
    logger.info ("Intentar actualizar datos del trabajador")
    response = enviar_PUT(get_url, payload, trabajador)
    assert response.status_code == 404
    logger.info("Test completado.")