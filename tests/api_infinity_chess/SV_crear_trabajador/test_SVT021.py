import pytest
from src.api_infinity_chess.crear_trabajador import enviar_POST, tierdown_enviar_DELETE
from src.utils.payload.payload_crear_trabajador import payload_con_nombre_invalido
from src.utils.response_500 import response_500
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SVBUG008: El sistema no valida el nombre de un trabajador", run=True)
def test_crear_trabajador_con_numeros_en_el_campo_nombre (get_url):
    logger.info("Iniciando test SVT021.")
    logger.info("Obtener datos de un trabajador con nombre invalido.")
    payload = payload_con_nombre_invalido()
    logger.debug(payload)
    response = enviar_POST (get_url, payload)
    response_500(response)
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json"))
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))
    logger.info("El nombre del trabajador es invalido.")
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 422
    #tierdown
    logger.info("Obtener al trabajador creado.")
    CODTRABAJADOR = payload.get("CODTRABAJADOR")
    logger.debug(f"El codigo del trabajador creado es: {CODTRABAJADOR}.")
    response = tierdown_enviar_DELETE (get_url, CODTRABAJADOR)
    logger.info(f"Codigo de respuesta DELETE: {response.status_code}")
    assert response.status_code == 200
    logger.info("Test completado.")