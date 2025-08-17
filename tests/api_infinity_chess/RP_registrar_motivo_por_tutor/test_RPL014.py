import pytest
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payload_motivo_tutor import crear_payload_motivo_tutor_vacio
from src.api_infinity_chess.obtener_agrear_motivo import peticion_agregar_motivo

@pytest.mark.functional
@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue RPBUG004: Crea motivos con el codigo de tutor vacio",run=True)
def test_RPL014_registro_motivo_con_campo_CODTUTOR_vacio (get_url):
    logger.info("Iniciando Test Case RPL014")
    payload = crear_payload_motivo_tutor_vacio ()
    logger.debug(payload)
    logger.info("validando Schema de payload")
    assert_validar_schema_input (payload, cargar_schema("schema_motivo.json"))
    response = peticion_agregar_motivo(get_url, payload)
    assert response.status_code == 422
    logger.info(response.status_code)
    logger.info("Validando response")
    assert_validar_response_schema (response, cargar_schema("schema_motivo.json"))