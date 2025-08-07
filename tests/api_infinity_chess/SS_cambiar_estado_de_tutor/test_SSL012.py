import pytest
from src.assertions.add import assert_validar_schema_input 
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.cambiar_estado_tutor import obtenerTutorAleatorio , enviarSolicitud
from src.utils.payload.payload_cambiar_estado import payload_sin_body

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SSBUG003: Payload invalido",run=True)
def test_solicitud_sin_body (get_url):
     logger.info("Iniciando test SSL012.")
     logger.info("Obtener un tutor aleatorio.")
     CODTUTOR = obtenerTutorAleatorio (get_url)
     logger.debug(f"Tutor seleccionado: {CODTUTOR}.")
     logger.debug(f"Payload: {payload_sin_body}")
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload_sin_body, cargar_schema("schema_estado.json"))
     response = enviarSolicitud (get_url, CODTUTOR,payload_sin_body)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 400
     logger.debug(f"Response: {response.json()}")
     logger.info("Test completado.")