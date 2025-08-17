import pytest
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT_con_headers
from src.assertions.add import assert_validar_schema_input, assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SVBUG017: El sistema actualiza los datos en formato text plain", run=True)
def test_intentar_actualizar_datos_con_el_content_type_en_formato_TEXT_PLAIN (get_url):
    logger.info("Iniciando de test SVT041.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar(trabajador)
    logger.debug(f"Payload:{payload}.")
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_actualizar_trabajador.json"))
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT_con_headers(get_url, payload, trabajador)
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_actualizar_trabajador.json"))
    assert response.status_code == 415
    logger.info("Test completado.")