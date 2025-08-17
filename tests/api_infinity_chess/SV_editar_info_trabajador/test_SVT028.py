import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_editado
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar_CODTRABAJADOR
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SVBUG010: Se devuelve un codigo 200 indicando que se hizo el cambio", run=True)
def test_actualizar_el_CODTRABAJADOR_de_un_trabajador_existente (get_url):
    logger.info("Iniciando de test SVT027.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar_CODTRABAJADOR(trabajador)
    logger.debug(f"Payload para actualizar el codigo:{payload}.")
    response = enviar_PUT(get_url, payload, trabajador)
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_actualizar_trabajador.json"))
    tierdown_eliminar_trabajador_editado(get_url, trabajador)
    assert response.status_code == 409
    logger.info("Test completado.")