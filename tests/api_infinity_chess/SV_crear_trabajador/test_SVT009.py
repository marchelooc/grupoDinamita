import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_creado
from src.api_infinity_chess.crear_trabajador import enviar_POST, crear_un_trabajador
from src.utils.payload.payload_crear_trabajador import crear_payload_valido, payload_con_nombre_existente
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG002: El sistema no puede validar un registro al ingresar un dato existente", run=True)
def test_crear_un_trabajador_con_un_nombre_que_ya_existe (get_url):
    logger.info("Iniciando test SVT009.")
    payload = crear_payload_valido()
    logger.debug(f"Payload:{payload}.")
    crear_un_trabajador(get_url,payload)
    logger.info("Obtener el nombre del trabajador creado.")
    NOMBRETRABAJADOR = payload.get("NOMBRETRABAJADOR")
    logger.debug(f"El nombre del trabajador creado es: {NOMBRETRABAJADOR}.")
    logger.info("Intentar crear otro trabajador con el nombre existente.")
    payload_2 = payload_con_nombre_existente(payload)
    logger.debug(f"Payload:{payload_2}.")
    response = enviar_POST (get_url, payload_2)
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload_2, cargar_schema("schema_trabajador.json"))
    logger.info(f"Codigo de respuesta al intento con codigo existente: {response.status_code}.")
    tierdown_eliminar_trabajador_creado(get_url, payload) #tierdown
    tierdown_eliminar_trabajador_creado(get_url, payload_2)
    assert response.status_code == 409
    logger.info("El nombre del trabajador ya existe.")
    logger.info("Test completado.")