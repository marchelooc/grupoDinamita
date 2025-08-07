import pytest
from src.assertions.add import assert_validar_schema_input , assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger 
from src.api_infinity_chess.cambiar_estado_tutor import obtenerTutorAleatorio , enviarSolicitud
from src.utils.payload.payload_cambiar_estado import payload_inactivo

@pytest.mark.smoke
def test_cambio_de_estado_de_tutor_inactivo (get_url):
     logger.info("Iniciando test SSL007.")
     logger.info("Obtener un tutor aleatorio.")
     CODTUTOR = obtenerTutorAleatorio (get_url)
     logger.debug(f"Tutor seleccionado: {CODTUTOR}.")
     logger.debug(f"Payload: {payload_inactivo}") 
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload_inactivo, cargar_schema("schema_estado.json"))
     response = enviarSolicitud (get_url, CODTUTOR,payload_inactivo)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 200
     logger.info("Validando schema del response.")
     assert_validar_response_schema(response,cargar_schema("schema_tutor.json"))
     logger.info("Test completado.")