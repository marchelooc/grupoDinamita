import requests
import pytest
from src.utils.response_500 import response_500
from src.assertions.add import assert_validar_schema_input
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_nombre_largo

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG01: HTTP incorrecto", run=True)
def test_validar_elLimite_maximo_de_caracteres_del_campo_CURSO(get_url):
    logger.info("Iniciando test MOCM008.")
    endpoint = "agregarCurso"
    logger.debug(f"este es el payload generado:{payload_materia_nombre_largo}")
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload_materia_nombre_largo,cargar_schema("schema_materias.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST {url_final}.")
    response = requests.post(url_final, json=payload_materia_nombre_largo)
    response_500(response)
    assert response.status_code == 400
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Test MOCM013 realizado.")
    