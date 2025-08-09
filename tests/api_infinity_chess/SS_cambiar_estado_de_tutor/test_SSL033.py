import pytest
from src.assertions.add import assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.cambiar_estado_tutor import  enviar_solicitud
from src.utils.payload.payload_cambiar_estado import payload_activo

@pytest.mark.negative
def test_solicitud_sin_codtutor(get_url):
     logger.info("Iniciando test SSL033.")
     logger.info("Sin CODTUTOR.")
     logger.debug(f"Payload: {payload_activo}") 
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload_activo, cargar_schema("schema_estado.json"))
     response = enviar_solicitud (get_url, "",payload_activo)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 404
     logger.info("Test completado.")