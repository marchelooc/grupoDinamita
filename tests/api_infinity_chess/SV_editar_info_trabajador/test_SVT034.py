import pytest
from src.api_infinity_chess.eliminar_trabajador import tierdown_eliminar_trabajador_editado
from src.utils.payload.payload_crear_trabajador import crear_payload_para_contra_sin_numeros
from src.api_infinity_chess.actualizar_trabajador import crear_trabajador, enviar_PUT
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SVBUG014: El sistema permite ingresar contraseñas invalidas en el campo contraseña al actualizar los datos", run=True)
def test_actualizar_la_contraseña_a_una_nueva_contraseña_sin_caracteres_alfanumericos (get_url):
    logger.info("Iniciando de test SVT034.")
    logger.info("Crear nuevo trabajador.")
    trabajador = crear_trabajador(get_url)
    payload = crear_payload_para_contra_sin_numeros(trabajador)
    logger.debug(f"Payload para cambiar contraseña:{payload}.")
    logger.info ("Actualizar datos del trabajador creado")
    response = enviar_PUT(get_url, payload, trabajador)
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_actualizar_trabajador.json"))
    assert response.status_code == 409
    tierdown_eliminar_trabajador_editado(get_url, trabajador)
    logger.info("Test completado.")