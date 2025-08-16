import pytest
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger 
from src.utils.payload.payload_motivo_tutor import crear_payload_motivo_tutor_inexistente
from src.api_infinity_chess.obtener_agrear_motivo import peticion_agregar_motivo

@pytest.mark.functional
@pytest.mark.negative
#@pytest.mark.xfail(reason="Knwon issue RPBUG008: El backend no valida tutores inexistentes",run=True)
def test_RPL004_registro_motivo_con_tutor_inexistente (get_url):
    logger.info("Iniciando Test Case RPL004")
    payload = crear_payload_motivo_tutor_inexistente ()
    logger.debug(payload)
    logger.info("validando Schema de payload")
    assert_validar_schema_input (payload, cargar_schema("schema_motivo.json"))
    response = peticion_agregar_motivo(get_url, payload)
    assert response.status_code == 404
    logger.info(response.status_code)
    logger.info("Validando response")
    assert_validar_response_schema (response, cargar_schema("schema_motivo.json"))