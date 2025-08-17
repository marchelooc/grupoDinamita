import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_creado
from src.api_infinity_chess.crear_trabajador import enviar_POST,crear_un_trabajador
from src.utils.payload.payload_crear_trabajador import crear_payload_valido, payload_con_codigo_existente
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG002: El sistema no puede validar un registro al ingresar un dato existente", run=True)
def test_crear_un_trabajador_con_un_codigo_que_ya_existe (get_url):
    logger.info("Iniciando test SVT008.")
    payload = crear_payload_valido()
    logger.debug(f"Payload:{payload}.")
    crear_un_trabajador(get_url,payload)
    logger.info("Obtener el codigo del trabajador creado.")
    CODTRABAJADOR = payload.get("CODTRABAJADOR")
    logger.debug(f"El codigo del trabajador creado es: {CODTRABAJADOR}.")
    logger.info("Intentar crear otro trabajador con el código ya existente.")
    payload_2 = payload_con_codigo_existente(payload)
    logger.debug(f"Payload:{payload_2}.")
    response = enviar_POST (get_url, payload_2)
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload_2, cargar_schema("schema_trabajador.json"))
    logger.info(f"Codigo de respuesta al intento con codigo existente: {response.status_code}.")
    tierdown_eliminar_trabajador_creado(get_url, payload) #tierdown
    assert response.status_code == 409
    logger.info("El codgigo del trabajador ya existe.")
    logger.info("Test completado.")
