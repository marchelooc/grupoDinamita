import requests
import pytest
import jsonschema
import random
from src.api_infinity_chess.obtener_tutores import obtener_tutores_activos
from src.assertions.add import assert_validar_response_schema, assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from datetime import date
from src.utils.logger_config import logger
from src.utils.payload.payload_motivo_tutor import crear_payload_motivo_estado_inactivo
from src.api_infinity_chess.obtener_agrear_motivo import peticion_agregar_motivo

@pytest.mark.functional
@pytest.mark.negative
@pytest.mark.xfail(reason="Knwon issue RPBUG003: Crea motivos con estado inactivo",run=True)
def test_RPL005_registro_motivo_con_campo_ESTADO_inactivo (get_url):
    logger.info("Iniciando Test Case RPL005")
    payload = crear_payload_motivo_estado_inactivo (get_url)
    logger.debug(payload)
    logger.info("validando Schema de payload")
    assert_validar_schema_input (payload, cargar_schema("schema_motivo.json"))
    response = peticion_agregar_motivo(get_url, payload)
    assert response.status_code == 422
    logger.info(response.status_code)
    logger.info("Validando response")
    assert_validar_response_schema (response, cargar_schema("schema_motivo.json"))