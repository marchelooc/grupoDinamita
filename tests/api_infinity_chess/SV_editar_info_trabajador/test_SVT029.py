import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_editado
from src.api_infinity_chess.obtener_trabajadores import obtener_nombre_de_trabajador
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar_NOMBRETRABAJADOR_repetido
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.functional
def test_actualizar_el_nombre_y_apellido_de_un_trabajador_con_uno_que_ya_existe_en_el_sistema (get_url):
    logger.info("Iniciando de test SVT029.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    trabajador_2 = obtener_nombre_de_trabajador(get_url)
    payload = crear_payload_para_actualizar_NOMBRETRABAJADOR_repetido(trabajador_2)
    logger.debug(f"Payload para cambiar el nombre:{payload}.")
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_actualizar_trabajador.json"))
    assert response.status_code == 200
    tierdown_eliminar_trabajador_editado(get_url, trabajador)
    logger.info("Test completado.")