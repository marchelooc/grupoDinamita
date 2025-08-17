import pytest
from src.assertions.add import assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.generador_codigo import generar_codigo
from src.utils.logger_config import logger
from src.api_infinity_chess.cambiar_estado_estudiante import enviar_solicitud
from src.utils.payload.payload_cambiar_estado import payload_habilitado

@pytest.mark.negative
def test_verificar_actualizacion_estudiante_inexistente (get_url):
     logger.info("Iniciando test SSL024.")
     logger.info("Generar un estudiante inexistente.")
     CODESTUDIANTE = generar_codigo()
     logger.debug(f"Estudiante seleccionado: {CODESTUDIANTE}.")
     logger.debug(f"Payload: {payload_habilitado}")
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload_habilitado, cargar_schema("schema_habilitado.json"))
     response = enviar_solicitud (get_url, CODESTUDIANTE,payload_habilitado)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 404
     logger.info("Test completado.")