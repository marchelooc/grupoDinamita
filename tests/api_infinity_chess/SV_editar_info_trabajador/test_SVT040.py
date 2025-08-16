import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_editado
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT_sin_payload
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SVBUG016: El sistema actualiza los datos sin payload", run=True)
def test_intentar_actualizar_datos_sin_enviar_el_body_del_JSON (get_url):
    logger.info("Iniciando de test SVT040.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT_sin_payload(get_url, trabajador)
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_actualizar_trabajador.json"))
    assert response.status_code == 422
    tierdown_eliminar_trabajador_editado(get_url, trabajador)
    logger.info("Test completado.")
