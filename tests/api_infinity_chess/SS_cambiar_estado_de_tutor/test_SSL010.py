import pytest
from src.assertions.add import assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.api_infinity_chess.cambiar_estado_tutor import obtener_tutor_aleatorio , enviar_solicitud
from src.utils.payload.payload_cambiar_estado import payload_invalido

@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue SSBUG001: Aceptar valor de estado invalido",run=True)
def test_validación_de_valor_inválido_en_campo_estado (get_url):
     logger.info("Iniciando test SSL010.")
     logger.info("Obtener un tutor aleatorio.")
     CODTUTOR = obtener_tutor_aleatorio (get_url)
     logger.debug(f"Tutor seleccionado: {CODTUTOR}.")
     logger.debug(f"Payload: {payload_invalido}")
     logger.info("Validando schema del payload.")
     assert_validar_schema_input(payload_invalido, cargar_schema("schema_estado.json"))
     response = enviar_solicitud (get_url, CODTUTOR,payload_invalido)
     logger.info(f"Código de respuesta: {response.status_code}.")
     assert response.status_code == 400
     logger.debug(f"Response: {response.json()}")
     logger.info("Test completado.")