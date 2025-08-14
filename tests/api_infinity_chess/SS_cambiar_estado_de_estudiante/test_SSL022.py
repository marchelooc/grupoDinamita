import pytest
from src.assertions.add import assert_validar_schema_input , assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger 
from src.api_infinity_chess.cambiar_estado_estudiante import obtener_estudiante_aleatorio , enviar_solicitud
from src.utils.payload.payload_cambiar_estado import payload_deshabilitado

@pytest.mark.smoke
def test_cambio_de_estado_de_estudiante_deshabilitado (get_url):
     logger.info("Iniciando test SSL022.")
     logger.info("Obtener un estudiante aleatorio.")
     CODESTUDIANTE = obtener_estudiante_aleatorio (get_url)
     logger.debug(f"Estudiante seleccionado: {CODESTUDIANTE}.")
     logger.debug(f"Payload: {payload_deshabilitado}") 
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload_deshabilitado, cargar_schema("schema_habilitado.json"))
     response = enviar_solicitud (get_url, CODESTUDIANTE,payload_deshabilitado)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 200
     logger.debug(f"Response: {response.json()}")
     logger.info("Validando schema del response.")
     assert_validar_response_schema(response,cargar_schema("schema_estudiante.json"))
     logger.info("Test completado.")