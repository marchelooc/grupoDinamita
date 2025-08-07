import pytest
from src.assertions.add import assert_validar_schema_input, assert_validar_response_schema
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger 
from src.api_infinity_chess.cambiar_estado_tutor import obtenerTutorAleatorio , enviarSolicitud
from src.utils.payload.payload_cambiar_estado import payload_activo

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SSBUG004: Sistema no soporta formato text/plain",run=True)
def test_solicitud_con_headers_Content_Type_text_plain(get_url):
     logger.info("Iniciando test SSL014.")
     logger.info("Obtener un tutor aleatorio.")
     CODTUTOR = obtenerTutorAleatorio (get_url)
     logger.debug(f"Tutor seleccionado: {CODTUTOR}.")
     logger.debug(f"Payload: {payload_activo}")
     headers = {
          "Accept": "application/json",
          "Content-Type": "text/plain",
     }
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload_activo, cargar_schema("schema_estado.json"))
     response = enviarSolicitud (get_url, CODTUTOR,payload_activo,headers)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 200
     logger.debug(f"Response: {response.json()}")
     logger.info("Validando schema del response.")
     assert_validar_response_schema(response,cargar_schema("schema_tutor.json"))
     logger.info("Test completado.")