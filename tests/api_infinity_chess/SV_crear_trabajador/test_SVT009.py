import pytest
from src.api_infinity_chess.crear_trabajador import enviar_POST, tierdown_enviar_DELETE
from src.utils.payload.payload_crear_trabajador import crear_payload_valido, payload_con_nombre_existente
from src.utils.response_500 import response_500
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG002: El sistema no puede validar un registro al ingresar un dato existente", run=True)
def test_crear_un_trabajador_con_un_nombre_que_ya_existe (get_url):
    logger.info("Iniciando test SVT009.")
    logger.info("Obtener datos de un trabajador para registrarlo en el sistema.")
    payload = crear_payload_valido()
    logger.debug(payload)
    response = enviar_POST (get_url, payload)
    response_500(response)
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json"))
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    assert response.status_code == 201
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))
    logger.info("Trabajador creado correctamente.")
    logger.info("Obtener el nombre del trabajador creado.")
    NOMBRETRABAJADOR = payload.get("NOMBRETRABAJADOR")
    logger.debug(f"El nombre del trabajador creado es: {NOMBRETRABAJADOR}.")
    logger.info("Intentar crear otro trabajador con el nombre existente.")
    payload_2 = payload_con_nombre_existente(payload)
    logger.debug(payload_2)
    response = enviar_POST (get_url, payload_2)
    response_500(response)
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload_2, cargar_schema("schema_trabajador.json"))
    logger.info(f"Codigo de respuesta al intento con codigo existente: {response.status_code}.")
    assert response.status_code == 409
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))
    logger.info("El nombre del trabajador ya existe.")
    #tierdown
    logger.info("Obtener al trabajador creado.")
    CODTRABAJADOR = payload.get("CODTRABAJADOR")
    logger.debug(f"El codigo del trabajador creado es: {CODTRABAJADOR}.")
    response = tierdown_enviar_DELETE (get_url, CODTRABAJADOR)
    logger.info(f"Codigo de respuesta DELETE: {response.status_code}")
    assert response.status_code == 200
    logger.info("Test completado.")