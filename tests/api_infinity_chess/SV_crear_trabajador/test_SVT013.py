import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_creado
from src.api_infinity_chess.crear_trabajador import enviar_POST
from src.utils.payload.payload_crear_trabajador import payload_con_contraseña_corta
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SVBUG005: El sistema acepta contraseñas invalidas", run=True)
def test_crear_trabajador_con_contraseña_menor_8_caracteres (get_url):
    logger.info("Iniciando test SVT013.")
    logger.info("Obtener datos de un trabajador con contraseña invalida.")
    payload = payload_con_contraseña_corta()
    logger.debug(f"Payload:{payload}.")
    response = enviar_POST (get_url, payload)
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json"))
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))
    logger.info("La contraseña del trabajador es invalida.")
    logger.debug(f"Response:{response.json()}.")
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    tierdown_eliminar_trabajador_creado(get_url, payload) #tierdown
    assert response.status_code == 422
    logger.info("Test completado.")