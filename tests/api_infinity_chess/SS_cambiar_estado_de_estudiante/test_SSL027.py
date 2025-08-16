import pytest
from src.assertions.add import assert_validar_schema_input 
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.cambiar_estado_estudiante import obtener_estudiante_aleatorio , enviar_solicitud
from src.utils.payload.payload_cambiar_estado import payload_sin_body

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SSBUG003: Payload invalido",run=True)
def test_solicitud_sin_body (get_url):
     logger.info("Iniciando test SSL027.")
     logger.info("Obtener un estudiante aleatorio.")
     CODESTUDIANTE = obtener_estudiante_aleatorio (get_url)
     logger.debug(f"Estudiante seleccionado: {CODESTUDIANTE}.")
     logger.debug(f"Payload: {payload_sin_body}")
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload_sin_body, cargar_schema("schema_habilitado.json"))
     response = enviar_solicitud (get_url, CODESTUDIANTE,payload_sin_body)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 400
     logger.debug(f"Response: {response.json()}")
     logger.info("Test completado.")