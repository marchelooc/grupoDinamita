import requests
import pytest
from src.utils.response_500 import response_500
from src.assertions.add import assert_validar_schema_input, assert_validar_response_schema
from src.utils.generador_codigo import generar_nom_materia, generar_cod
from src.utils.cargar_schema import cargar_schema
from src.utils.logger_config import logger
from src.utils.payload.payloads_materias import payload_materia_correcta, headers_json

@pytest.mark.smoke
def test_agregar_una_materia_sin_headers_de_tipo_json(get_url):
    logger.info("Iniciando test MOCM023.")
    endpoint = "agregarCurso"
    logger.debug(f"este es el payload generado:{payload_materia_correcta}")
    logger.info("Validando schema del input.")
    assert_validar_schema_input(payload_materia_correcta,cargar_schema("schema_materias.json"))
    url_final = get_url + endpoint
    logger.info(f"Enviando POST {url_final}.")
    response = requests.post(url_final, json=payload_materia_correcta, headers=headers_json)
    response_500(response)
    assert response.status_code == 201
    logger.info(f"Código de respuesta: {response.status_code}.")
    logger.info("Validando schema del response.")
    assert_validar_response_schema(response,cargar_schema("schema_materias.json"))
    url_final = get_url + "eliminarCurso/2025Taller"
    logger.info(f"Enviando DELETE {url_final}.")
    requests.delete(url_final)
    logger.info("Test MOCM023 realizado.")
#mostrar que materia fue creada 