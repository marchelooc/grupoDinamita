import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_editado
from src.utils.payload.payload_crear_trabajador import crear_payload_para_con_campos_vacios
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG015: El sistema permite dejar campos obligatorios vacios al actualizar los datos", run=True)
def test_intentar_actualizar_datos_sin_enviar_un_campo_obligatorio_en_el_body_del_JSON (get_url):
    logger.info("Iniciando de test SVT039.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_con_campos_vacios(trabajador)
    logger.debug(f"Payload para cambiar datos:{payload}.")
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_actualizar_trabajador.json"))
    assert response.status_code == 422
    tierdown_eliminar_trabajador_editado(get_url, trabajador)
    logger.info("Test completado.")