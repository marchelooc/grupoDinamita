import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_creado
from src.api_infinity_chess.crear_trabajador import enviar_POST, mostrar_trabajador
from src.utils.payload.payload_crear_trabajador import crear_payload_valido
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
def test_verificar_los_datos_del_trabajador_creado (get_url):
    logger.info("Iniciando test SVT007.")
    logger.info("Obtener datos de un trabajador para registrarlo en el sistema.")
    payload = crear_payload_valido()
    logger.debug(f"Payload:{payload}.")
    response = enviar_POST (get_url, payload)
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_trabajador.json"))
    logger.info(f"Codigo de respuesta: {response.status_code}.")
    logger.debug(f"Response:{response.json()}.")
    assert response.status_code == 201
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_trabajador.json"))
    logger.info("Trabajador creado correctamente.")
    mostrar_trabajador(payload)
    tierdown_eliminar_trabajador_creado(get_url, payload) #tierdown
    logger.info("Test completado.")