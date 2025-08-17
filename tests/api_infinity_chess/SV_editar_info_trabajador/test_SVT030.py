import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_editado
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar_NOMBRETRABAJADOR
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG011: El sistema permite ingresar numeros en el campo nombre al actualizar los datos", run=True)
def test_actualizar_el_nombre_y_apellido_de_un_trabajador_con_numeros (get_url):
    logger.info("Iniciando de test SVT030.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_actualizar_NOMBRETRABAJADOR(trabajador)
    logger.debug(f"Payload para cambiar nombre:{payload}.")
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_actualizar_trabajador.json"))
    tierdown_eliminar_trabajador_editado(get_url, trabajador)
    assert response.status_code == 422
    logger.info("Test completado.")