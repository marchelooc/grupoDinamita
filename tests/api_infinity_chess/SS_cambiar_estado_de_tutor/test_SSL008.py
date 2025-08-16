import pytest
from src.assertions.add import assert_validar_schema_input , assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger 
from src.api_infinity_chess.cambiar_estado_tutor import obtener_tutor_aleatorio , enviar_solicitud
from src.utils.payload.payload_cambiar_estado import payload_activo

@pytest.mark.smoke
def test_cambio_de_estado_de_tutor_activo (get_url):
     logger.info("Iniciando test SSL008.")
     logger.info("Obtener un tutor aleatorio.")
     CODTUTOR = obtener_tutor_aleatorio (get_url)
     logger.debug(f"Tutor seleccionado: {CODTUTOR}.")
     logger.debug(f"Payload: {payload_activo}") 
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload_activo, cargar_schema("schema_estado.json"))
     response = enviar_solicitud (get_url, CODTUTOR,payload_activo)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 200
     logger.debug(f"Response: {response.json()}")
     logger.info("Validando schema del response.")
     assert_validar_response_schema(response,cargar_schema("schema_tutor.json"))
     logger.info("Test completado.")