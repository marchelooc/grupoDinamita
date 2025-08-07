import pytest
from src.assertions.add import assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.cambiar_estado_tutor import obtenerTutorAleatorio , enviarSolicitud
from src.utils.payload.payload_cambiar_estado import payload_vacio

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue SSBUG002: Aceptar valor de estado vacio",run=True)
def test_validación_de_valor_inválido_en_campo_estado (get_url):
     logger.info("Iniciando test SSL011.")
     logger.info("Obtener un tutor aleatorio.")
     CODTUTOR = obtenerTutorAleatorio (get_url)
     logger.debug(f"Tutor seleccionado: {CODTUTOR}.")
     logger.debug(f"Payload: {payload_vacio}")
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload_vacio, cargar_schema("schema_estado.json"))
     response = enviarSolicitud (get_url, CODTUTOR,payload_vacio)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 400
     logger.debug(f"Response: {response.json()}")
     logger.info("Test completado.")