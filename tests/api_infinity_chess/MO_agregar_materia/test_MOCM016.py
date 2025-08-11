import requests
import pytest
from src.utils.response_500 import response_500
from src.assertions.add import assert_validar_schema_input
from src.utils.generador_codigo import generar_nom_materia, generar_cod
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_nombre_invalido

@pytest.mark.functional
@pytest.mark.xfail(reason="Knwon issue MOCBUG04: Materia agregada con nombre de materia inválida", run=True)
def test_validar_comportamiento_CURSO_con_caracteres_especiales(get_url):
    logger.info("Iniciando test MOCM016.")
    endpoint = "agregarCurso"
    logger.debug(f"este es el payload generado:{payload_materia_nombre_invalido}")
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload_materia_nombre_invalido,cargar_schema("schema_materias.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST {url_final}.")
    response = requests.post(url_final, json=payload_materia_nombre_invalido)
    response_500(response)
    assert response.status_code == 400
    logger.info(f"Código de respuesta: {response.status_code}.")
    url_final = get_url + "eliminarCurso/2025SOCIALES"
    logger.info(f"Enviando DELETE {url_final}.")
    requests.delete(url_final)
    logger.info("Test MOCM015 realizado.")
    