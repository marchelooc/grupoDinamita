import pytest
from src.assertions.add import assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger 
from src.api_infinity_chess.registro import enviar_solicitud
from src.utils.payload.payload_registro import payload_vacio

@pytest.mark.negative
def test_registro_con_datos_vacios (get_url):
     logger.info("Iniciando test SSL036.")
     payload = payload_vacio
     logger.debug(f"Payload: {payload}") 
     response = enviar_solicitud (get_url,payload)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 400
     logger.debug(f"Response: {response.json()}")
     logger.info("Validando schema del response.")
     assert_validar_response_schema(response,cargar_schema("schema_registro.json"))
     logger.info("Test completado.")