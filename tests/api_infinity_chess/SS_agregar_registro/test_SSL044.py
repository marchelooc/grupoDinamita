import pytest
from src.assertions.add import assert_validar_schema_input , assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger 
from src.api_infinity_chess.registro import enviar_solicitud
from src.utils.payload.payload_registro import crear_payload_habilitado_invalido

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SSBUG006: Sistema no valida datos del body",run=True)
def test_registro_habilitado_invalido (get_url):
     logger.info("Iniciando test SSL044.")
     payload = crear_payload_habilitado_invalido(get_url)
     logger.debug(f"Payload: {payload}")
     response = enviar_solicitud (get_url,payload)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 201
     logger.debug(f"Response: {response.json()}")
     logger.info("Validando schema del response.")
     assert_validar_response_schema(response,cargar_schema("schema_registro.json"))
     logger.info("Test completado.")