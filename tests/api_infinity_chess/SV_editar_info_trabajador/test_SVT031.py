import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_editado
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar_fecha_menor
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG012: El sistema permite actualizar la fecha de nacimiento a una fecha invalida", run=True)
def test_actualizar_la_fecha_de_nacimiento_del_trabajador_a_una_fecha_menor_de_18_años (get_url):
    logger.info("Iniciando de test SVT031.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar_fecha_menor(trabajador)
    logger.debug(f"Payload para cambiar fecha de nacimiento:{payload}.")
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_actualizar_trabajador.json"))
    assert response.status_code == 422
    tierdown_eliminar_trabajador_editado(get_url, trabajador)
    logger.info("Test completado.")