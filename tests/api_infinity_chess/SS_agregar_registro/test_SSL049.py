import pytest
from src.assertions.add import assert_validar_schema_input , assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger 
from src.api_infinity_chess.registro import enviar_solicitud
from src.utils.payload.payload_registro import crear_payload_valido

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SSBUG004: Sistema no soporta formato text/plain",run=True)
def test_registro_header_Content_Type_text_plain (get_url):
     logger.info("Iniciando test SSL048.")
     payload = crear_payload_valido(get_url)
     logger.debug(f"Payload: {payload}") 
     headers = {
          "Accept": "application/json",
          "Content-Type": "text/plain",
     }
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload, cargar_schema("schema_registro.json"))
     response = enviar_solicitud (get_url,payload,headers)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 201
     logger.debug(f"Response: {response.json()}")
     logger.info("Validando schema del response.")
     assert_validar_response_schema(response,cargar_schema("schema_registro.json"))
     logger.info("Test completado.")