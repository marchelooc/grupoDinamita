import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_editado
from src.utils.payload.payload_crear_trabajador import crear_payload_para_actualizar
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.smoke
def test_actualizar_todos_los_datos_de_un_trabajador_existente_con_valores_validos (get_url):
    logger.info("Iniciando de test SVT027.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)#precondicion
    payload = crear_payload_para_actualizar(trabajador)
    logger.debug(f"Payload para cambiar datos:{payload}.")
    logger.info("Validando schema de entrada del payload.")
    assert_validar_schema_input(payload, cargar_schema("schema_actualizar_trabajador.json"))
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    logger.debug(f"Response:{response.json()}.")
    assert response.status_code == 200
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_actualizar_trabajador.json"))
    tierdown_eliminar_trabajador_editado(get_url, trabajador) #tierdown
    logger.info("Test completado.")