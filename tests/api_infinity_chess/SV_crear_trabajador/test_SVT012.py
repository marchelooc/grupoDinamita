import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_creado
from src.api_infinity_chess.crear_trabajador import enviar_POST
from src.utils.payload.payload_crear_trabajador import payload_con_rol_invalido
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SVBUG004: El sistema acepta diferentes roles a los establecidos", run=True)
def test_crear_trabajador_con_rol_invalido (get_url):
    logger.info("Iniciando test SVT012.")
    logger.info("Obtener datos de un trabajador con rol invalido.")
    payload = payload_con_rol_invalido()
    logger.debug(f"Payload:{payload}.")
    response = enviar_POST (get_url, payload)
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json"))
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))
    logger.info("El rol del trabajador no esta permitido.")
    logger.debug(f"Response:{response.json()}.")
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    tierdown_eliminar_trabajador_creado(get_url, payload) #tierdown
    assert response.status_code == 422
    logger.info("Test completado.")