import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_creado
from src.api_infinity_chess.crear_trabajador import enviar_POST
from src.utils.payload.payload_crear_trabajador import crear_payload_fecha_menor
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG003: El sistema registra fechas invalidas", run=True)
def test_crear_trabajador_menor_de_18_años (get_url):
    logger.info("Iniciando test SVT010.")
    logger.info("Obtener datos de un trabajador con fecha de nacimiento invalida.")
    payload = crear_payload_fecha_menor()
    logger.debug(f"Payload:{payload}.")
    response = enviar_POST (get_url, payload)
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json"))
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))
    logger.info("La fecha de nacimiento del trabajador no es valida.")
    logger.debug(f"Response:{response.json()}.")
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    tierdown_eliminar_trabajador_creado(get_url, payload) #tierdown
    assert response.status_code == 422
    logger.info("Test completado.")